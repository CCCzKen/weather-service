import os
import logging
from logging.config import dictConfig

from flask import Flask, jsonify
from flasgger import Swagger

from config import current_config
from src.urls import routers
from src.extensions import redis
from src.utils.exceptions import ApiError
from src.logger import init_logging_logger


logger = logging.getLogger(__name__)


def create_app():
    """创建app"""
    app = Flask(__name__)
    app.config.from_object(current_config)
    config_log(app)
    configure_error_handlers(app)
    configure_extensions(app)
    configure_blueprint(app)
    configure_swagger(app)
    return app


def config_log(app):
    # 日志文件目录
    log_filepath = app.config.setdefault("LOG_FILEPATH", os.path.join(os.path.dirname(__file__), "../logs"))
    # 判断日志文件目录是否存在,不存在则创建
    if not os.path.exists(log_filepath):
        os.makedirs(log_filepath)

    # 日志配置
    dictConfig(init_logging_logger(app.config['LOG_FILEPATH']))


def configure_blueprint(app):
    for blueprint, url_prefix in routers:
        app.register_blueprint(blueprint, url_prefix=url_prefix)


def configure_extensions(app):
    redis.init_app(app)


def configure_swagger(app):
    Swagger(app)


def configure_error_handlers(app):
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify(dict(code=401, msg=str(error)))

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify(dict(code=403, msg=str(error)))

    @app.errorhandler(422)
    def param_invalid(error):
        return jsonify(dict(code=422, msg=str(error)))

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify(dict(code=404, msg=str(error)))

    @app.errorhandler(500)
    def server_error(error):
        logger.error(error)
        return jsonify(dict(code=500, msg=str(error)))

    @app.errorhandler(ApiError)
    def handle_api_error(e):
        response = jsonify(e.to_dict())
        response.status_code = e.status_code
        return response


flask_app = create_app()
