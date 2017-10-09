import click
from pylogconf import setup


@click.command()
def main():
    """
    This script will update your apt-key, apt-configuration, update apt, and install
    all required package in the list.
    """
    setup()


if __name__ == "__main__":
    main()
