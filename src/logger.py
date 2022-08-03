import os


def init_logging_logger(filepath):
    config = {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s %(levelname)s] [in %(pathname)s:%(lineno)d]\n%(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "default"
            },
            # "info_handler": {
            #     "level": "INFO",
            #     "formatter": "default",
            #     "filename": os.path.join(LOG_FILEPATH, "app.info.log"),
            #     "class": "logging.FileHandler",
            # },
            "error_handler": {
                "level": "ERROR",
                "formatter": "default",
                "filename": os.path.join(filepath, "app.error.log"),
                "class": "logging.FileHandler",
            },
        },
        "root": {
            # "level": "INFO",
            # "handlers": ["console", "info_handler", "error_handler"],
            "level": "ERROR",
            "handlers": ["console", "error_handler"],
            "propagate": False
        }
    }

    return config
