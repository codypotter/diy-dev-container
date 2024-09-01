# DIY Dev Container Project

This project is a simple development setup using Docker Compose for managing a PostgreSQL database and Nix for handling the development environment. It includes a Python script that connects to the PostgreSQL database.

## Prerequisites

Before getting started, ensure you have the following tools installed

- Nix - used to manage the development environment
- Docker & Docker Compose - Used to manage and run the PostgreSQL database.

## Getting Started

### 0. Start the Development Environment

```sh
./dev env
```

### 1. Start the PostgreSQL Database

```sh
./dev up
```

### 2. Run the Python App

```sh
./dev run
```

### 3. Stop the Database

```sh
./dev down
```

