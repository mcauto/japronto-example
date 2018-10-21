from japronto import Application
from logging.config import dictConfig
import os
APP_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(APP_DIR)
LOG_PATH = os.path.abspath(APP_DIR)+"/log"

app = Application()

class App():
    def route(url, methods=['GET', 'POST', 'DELETE', 'UPDATE'], *args, **kwargs):
        def decorator(fn):
            for method in methods:
                app.router.add_route(
                    url, fn, method=method.upper(), *args, **kwargs)
            return fn
        return decorator

    @route("/")
    def handleRoot(request):
        return request.Response(text="pyBanca")
