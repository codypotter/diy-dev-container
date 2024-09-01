import psycopg2
import boto3
import json
import os

def get_db_credentials():
    secret_name = os.getenv("SECRET_NAME")
    region_name = os.getenv("AWS_REGION", "us-east-1")

    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response["SecretString"])

    return secret

def lambda_handler(event, context):
    try:
        creds = get_db_credentials()
        connection = psycopg2.connect(
            user=creds["DB_USER"],
            password=creds["DB_PASSWORD"],
            host=creds["DB_HOST"],
            port=creds.get("DB_PORT", "5432"),
            database=creds["DB_NAME"]
        )

        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        return {
            'statusCode': 200,
            'body': f"You are connected to - {record}\n"
        }

    except Exception as error:
        return {
            'statusCode': 500,
            'body': f"Error while connecting to PostgreSQL: {error}"
        }
    finally:
        if connection:
            cursor.close()
            connection.close()
