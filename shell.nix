{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python311
    pkgs.python311Packages.psycopg2
    pkgs.python311Packages.boto3
    pkgs.postgresql
    pkgs.neovim
    pkgs.git
  ];

  shellHook = ''
    export DATABASE_URL="postgresql://user:password@localhost:5432/mydatabase"
    echo "Environment ready! Run ./dev to get started."
  '';
}

