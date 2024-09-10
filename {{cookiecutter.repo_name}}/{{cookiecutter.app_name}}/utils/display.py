import json
import logging
import logging.config

from rich.console import Console
from rich.logging import RichHandler


class JsonFormatter(logging.Formatter):
    def format(self, record):
        record.asctime = self.formatTime(record) 
        log_record = {
            "timestamp": record.asctime,
            "level": record.levelname,
            "name": record.name,
            "msg": record.getMessage()
        }
        return json.dumps(log_record)

def configure_logging(debug=False):
    use_json = "{{cookiecutter.logging_format}}" == "JSON"
    level = 'DEBUG' if debug else 'INFO'
    formatter = 'json' if use_json else 'rich'
    handlers = {
        "rich": {
            "class": "rich.logging.RichHandler",
            "formatter": formatter,
            "rich_tracebacks": True,
            "level": level,
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "{{ cookiecutter.app_name }}.log",
            "formatter": formatter,
            "mode": "a",
            "level": level,
        },
    } if not use_json else {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
        }
    }

    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "rich": {"format": "%(message)s", "datefmt": "[%X]"},
            "json": {"()": JsonFormatter}
        },
        "handlers": handlers,
        "loggers": {"": {"handlers": list(handlers.keys()), "level": level}},
    }
    logging.config.dictConfig(LOGGING_CONFIG)

log = logging.getLogger("")
console = Console()
print = console.print