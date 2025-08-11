# Lab 8 – Local Cloud Services with Docker Compose and Python Driver

## Introduction
This project sets up a suite of local cloud-like services using Docker Compose and demonstrates programmatic access through a Python command-line driver.  

The services implemented include:
- **MinIO** – S3-compatible object storage
- **Redis** – in-memory key-value store (shared memory)
- **Postfix** – SMTP email server

---

## Description
Lab 8 demonstrates how to provision and interact with common cloud services locally using Docker containers.  

- **MinIO**: Provides an S3-compatible object storage endpoint.
- **Redis**: Acts as a shared memory/cache using a key-value store.
- **Postfix**: Accepts and queues SMTP email messages.

A standalone Python driver (`driver_cloud.py`) is used to:
1. Connect to MinIO, create a bucket, upload, and retrieve an object.
2. Connect to Redis, store and retrieve a value.
3. Connect to Postfix and send a test email.

---

## Design
- **Docker Compose** orchestrates all three services on standard ports.
- **MinIO** data is persisted in a bind-mounted folder.
- **Redis** data is persisted in a bind-mounted folder.
- **Postfix** is configured for local email submission with no external relay.
- **Python Driver** uses:
  - `boto3` for MinIO (S3 API)
  - `redis` Python client
  - `smtplib` from Python standard library

---

## How to Run

### Install Prerequisites
- [Docker Desktop](https://www.docker.com/)
- Python 3.x
- Python dependencies:
  ```bash
  pip install boto3 redis

## CLONE REPO
  git clone https://github.com/your-username/CloudComputing.git
cd CloudComputing/Lab8

## Start
docker-compose up -d
docker ps

## Run Driver
python driver.py
