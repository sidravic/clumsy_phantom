from starlette.applications import Starlette
from config.routes import routes
from config.env_vars import config
from services.download_model import download_model_from_s3

env = config('ENV')

if (not env == 'development') or (not env == 'test'):
    debug = False
else:
    debug = True


def startup():
    print('launched on port 3002')





app = Starlette(debug=debug, routes=routes, on_startup=[startup, download_model_from_s3])