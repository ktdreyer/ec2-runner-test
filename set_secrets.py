#!/usr/bin/env python3
import os
import subprocess


def main():
    # Read AWS credentials from environment variables
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    aws_session_token = os.environ.get("AWS_SESSION_TOKEN")

    # Verify all required credentials are present
    if not aws_access_key_id:
        raise SystemExit("Error: AWS_ACCESS_KEY_ID environment variable is not set")

    if not aws_secret_access_key:
        raise SystemExit("Error: AWS_SECRET_ACCESS_KEY environment variable is not set")

    if not aws_session_token:
        raise SystemExit("Error: AWS_SESSION_TOKEN environment variable is not set")

    subprocess.run(
        ["gh", "secret", "set", "AWS_ACCESS_KEY_ID"],
        input=aws_access_key_id.encode(),
        check=True,
    )
    subprocess.run(
        ["gh", "secret", "set", "AWS_SECRET_ACCESS_KEY"],
        input=aws_secret_access_key.encode(),
        check=True,
    )
    subprocess.run(
        ["gh", "secret", "set", "AWS_SESSION_TOKEN"],
        input=aws_session_token.encode(),
        check=True,
    )

    print("Secrets set successfully from environment variables.")


if __name__ == "__main__":
    main()
