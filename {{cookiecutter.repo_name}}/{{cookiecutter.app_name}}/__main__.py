#!/usr/bin/env python3

import click
from click_extra import config_option

from .utils.display import configure_logging, log, print
from .utils.helpers import *

# Setting context settings for click
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help", "help"])

# Modify no_args_is_help to False to allow for no arguments to be passed to the command.
@click.command(no_args_is_help=True, context_settings=CONTEXT_SETTINGS)
@click.option("--debug", "-d", is_flag=True, help="Enable debug mode.")
@config_option(default="config.yaml", help="Path to config file.")
def main(debug: bool) -> None:
    """{{cookiecutter.app_name}}"""
    configure_logging(debug)
    pass


if __name__ == "__main__":
    main()
