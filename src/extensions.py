from flask_redis import FlaskRedis


redis = FlaskRedis(config_prefix="REDIS", decode_responses=True)
