class BaseExcept(Exception):
    """异常基类"""
    pass


class ApiError(BaseExcept):
    """触发Api异常，直接中止后续执行并返回JSON格式错误。

    触发异常::

        @app.route("/test")
        def test():
            raise ApiError("Some message")

    应用自动捕获ApiError异常并返回JSON类型响应::

        {"code": -1, "msg": "Some message"}

    :param str message: 错误信息
    :param int code: 非0错误码
    :param int status_code: 请求响应码，如200、403、404

    """

    def __init__(self, message, code=-1, status_code=200):
        super(ApiError, self).__init__()
        self.code = code
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        rv = dict(code=self.code, msg=self.message)
        return rv
