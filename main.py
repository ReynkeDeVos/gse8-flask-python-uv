import typer


def create_greeting(first_name: str, last_name: str) -> str:
    """Create the greeting used by both the CLI and the web application."""
    return f"Hallo, {first_name.strip()} {last_name.strip()}!"


def main(name: str, lastname: str):
    typer.echo(create_greeting(name, lastname))


if __name__ == "__main__":
    typer.run(main)
