#!/usr/bin/env python3

import click
from click_extra import config_option

from .utils.setup import log, print

# Setting context settings for click
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help", "help"])

@click.command(no_args_is_help=True, context_settings=CONTEXT_SETTINGS)
@config_option(default="config.yaml", help="Path to config file.")
def main() -> None:
    """{{cookiecutter.app_name}}"""
    pass


if __name__ == "__main__":
    main()
