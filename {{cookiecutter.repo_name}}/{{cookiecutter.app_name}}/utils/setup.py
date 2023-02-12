import logging
import logging.config

from rich.console import Console
from rich.logging import RichHandler

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"rich": {"format": "%(message)s", "datefmt": "[%X]"}},
    "handlers": {
        "rich": {
            "class": "rich.logging.RichHandler",
            "formatter": "rich",
            "rich_tracebacks": True,
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "{{ cookiecutter.app_name }}.log",
            "formatter": "rich",
            "mode": "a",
        },
    },
    "loggers": {"": {"handlers": ["rich", "file"], "level": "INFO"}},
}

logging.config.dictConfig(LOGGING_CONFIG)
log = logging.getLogger("")

console = Console()
print = console.print
