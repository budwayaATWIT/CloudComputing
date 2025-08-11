import sys
import io
import boto3
import redis
import smtplib
from botocore.client import Config
from email.mime.text import MIMEText


def demo_minio():
    print("\n[MinIO] Creating bucket, uploading, then reading an object...")
    s3 = boto3.client(
        "s3",
        endpoint_url="http://localhost:9000",
        aws_access_key_id="minio",
        aws_secret_access_key="minio12345",
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )

    bucket = "lab-bucket"
    key = "hello.txt"
    data = b"Hello from Lab local cloud services!"

    # create bucket if not exists
    try:
        s3.head_bucket(Bucket=bucket)
        print(f"Bucket '{bucket}' already exists")
    except Exception:
        s3.create_bucket(Bucket=bucket)
        print(f"Created bucket '{bucket}'")

    s3.put_object(Bucket=bucket, Key=key, Body=data)
    print(f"Uploaded object '{key}'")

    obj = s3.get_object(Bucket=bucket, Key=key)
    body = obj["Body"].read().decode("utf-8")
    print("Downloaded object contents:", body)

def demo_redis():
    print("\n[Redis] Setting and getting a key...")
    r = redis.Redis(host="localhost", port=6379, db=0)
    r.set("lab:key", "cloud-computing")
    val = r.get("lab:key")
    print("lab:key =", val.decode("utf-8"))


def demo_postfix():
    print("\n[Postfix] Sending a test email via local Postfix...")
  
    msg = MIMEText("Hello from the Lab driver via Postfix!")
    msg["Subject"] = "Lab SMTP Test"
    msg["From"] = "budwaya@wit.edu"
    msg["To"] = "budwaya@wit.edu"

    with smtplib.SMTP("localhost", 2525, timeout=10) as smtp:
        smtp.send_message(msg)

    print("Email submitted to Postfix. Check container logs to confirm receipt:")
    print("  docker logs -f postfix_local  (look for 'postfix' log lines)")

def menu():
    print("\n=== Local Cloud Services Driver ===")
    print("1) MinIO (S3) demo")
    print("2) Redis demo")
    print("3) Postfix (SMTP) demo")
    print("0) Exit")

def main():
    while True:
        menu()
        choice = input("Select: ").strip()
        if choice == "0":
            break
        try:
            if choice == "1":
                demo_minio()
            elif choice == "2":
                demo_redis()
            elif choice == "3":
                demo_postfix()
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
