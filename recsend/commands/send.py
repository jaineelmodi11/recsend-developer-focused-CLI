import os
import sys
import json
import yaml
import click
from recsend.utils.http_client import HttpClient

@click.command("send", help="Send a request defined in JSON/YAML")
@click.option("-f", "--file", "path", required=True, type=click.Path(exists=True))
@click.option("-c", "--color", is_flag=True, help="Colorize JSON output")
def send_request_cmd(path, color):
    # Determine file extension
    ext = os.path.splitext(path)[1].lower()
    # Load data from file
    with open(path, 'r') as fp:
        data = yaml.safe_load(fp) if ext in (".yml", ".yaml") else json.load(fp)

    # Send HTTP request
    client = HttpClient()
    response = client.request(
        method=data["method"],
        url=data["url"],
        headers=data.get("headers"),
        json=data.get("body")
    )

    # Output response body to stdout
    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        body = response.json()
        formatted = json.dumps(body, indent=2)
    else:
        formatted = response.text

    if color and "application/json" in content_type:
        click.echo(click.style(formatted, fg="green"))
    else:
        click.echo(formatted)

    # Output status and headers to stderr
    click.echo(f"Status: {response.status_code}", err=True)
    for key, value in response.headers.items():
        click.echo(f"{key}: {value}", err=True)
