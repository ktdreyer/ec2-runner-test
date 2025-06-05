#!/usr/bin/env python3
import sys
import os
import configparser
import subprocess

CRED_FILE = os.path.expanduser("~/.aws/credentials")


def main():
    profile = sys.argv[1] if len(sys.argv) > 1 else "saml"

    config = configparser.RawConfigParser()
    config.read(CRED_FILE)

    if profile not in config:
        print(f"Profile '{profile}' not found in {CRED_FILE}")
        sys.exit(1)

    aws_access_key_id = config[profile]["aws_access_key_id"]
    aws_secret_access_key = config[profile]["aws_secret_access_key"]
    aws_session_token = config[profile]["aws_session_token"]

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

    print(f"Secrets set for profile '{profile}'.")


if __name__ == "__main__":
    main()
