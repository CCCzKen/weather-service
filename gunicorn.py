import multiprocessing

_file_name = "weather_service"
_log_path = "/data/logs"

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
timeout = 100

loglevel = 'info'

access_log_format = '%({X_Real_IP}i)s %(l)s %(t)s "%(r)s" %(s)s %(b)s "%(a)s" %(D)sms'
pidfile = '%s/%s.pid' % (_log_path, _file_name)
