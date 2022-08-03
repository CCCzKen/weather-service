from src import flask_app as app


if __name__ == '__main__':
    app.debug = app.config['DEBUG']  # 调试模式, DEBUG = True
    app.run(host='0.0.0.0', port=5000)  # 端口号必须为整型
