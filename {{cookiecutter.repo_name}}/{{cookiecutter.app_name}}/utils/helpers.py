import json
import os
import random

import click
import validators


def validate_url(ctx, param, value):
    """Validate a URL in click context."""
    if not validators.url(value):
        raise click.BadParameter("Invalid URL")
    return value

def validate_email(ctx, param, value):
    """Validate an email in click context."""
    if not validators.email(value):
        raise click.BadParameter("Invalid email")
    return value

def validate_ip(ctx, param, value):
    """Validate an IP address in click context."""
    if not validators.ipv4(value) and not validators.ipv6(value):
        raise click.BadParameter("Invalid IP address")
    return value

def validate_domain(ctx, param, value):
    """Validate a domain in click context."""
    if not validators.domain(value):
        raise click.BadParameter("Invalid domain")
    return value

def file_exists(path):
    """Check if a file exists."""
    if not os.path.exists(path):
        raise Exception(f"File {path} does not exist!")
    return path

def read_file(path, check_exists=True):
    """Read a file and return a list of lines."""
    if check_exists:
        file_exists(path)
    return [line.strip() for line in open(path)]

def write_list_to_file(path: str, content: list[str]):
    """Write content to a file."""
    with open(path, "w") as f:
        for line in content:
            f.write(line + "\n")

def dump_json_to_file(path: str, content: dict, pretty: bool = False):
    """Dump a dictionary to a JSON file."""
    with open(path, "w") as f:
        if pretty:
            json.dump(content, f, indent=4)
        else:
            json.dump(content, f)

def load_json_from_file(path: str, file_exists: bool = True):
    """Load a JSON file and return a dictionary."""
    if file_exists:
        file_exists(path)
    with open(path, "r") as f:
        return json.load(f)

def get_random_user_agent():
    """Get a random user agent."""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    ]
    return random.choice(user_agents)

def create_directory(path: str) -> bool:
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        return True
    return False


def get_env_variable(key: str, default=None):
    """Get an environment variable or return a default value."""
    try:
        return os.getenv(key, default)
    except Exception as e:
        raise e
