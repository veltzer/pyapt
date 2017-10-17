import click
from pylogconf import setup

from core.core import read_config


@click.command()
def main():
    """
    This script will update your apt-key, apt-configuration, update apt, and install
    all required package in the list.
    """
    setup()
    read_config()


if __name__ == "__main__":
    main()
