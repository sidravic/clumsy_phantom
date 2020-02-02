from starlette.routing import Route, Mount
from controllers.welcome_controller import homepage
from controllers.predictions_controller import predict

routes = [
    Route('/', homepage),
    Mount('/api/v1', routes=[
      Route('/predict', endpoint=predict, methods=['POST'])
    ])
]