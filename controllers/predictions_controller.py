from config.env_vars import config
from fastai.core import Path, download_url
from starlette.responses import JSONResponse
from urllib.request import urlopen
from controllers.base_controller import ValidationError
from services.predict import classify

VALID_IMAGE_FORMATS = ['image/jpg', 'image/jpeg']
PREDICTION_IMAGES_PATH = Path('./prediction_images')


async def validate_and_download_image(request_params):
    image_url = request_params['image_url']

    if not image_url:
        raise ValidationError('image_url cannot be blank', 'image_url_blank')

    try:
        url = urlopen(image_url)
    except Exception as e:
        raise ValidationError('invalid url', str(e))

    meta = url.info()

    if not meta['content-type'] in VALID_IMAGE_FORMATS:
        raise ValidationError('invalid image format', 'invalid_image_format')

    filename = image_url.split('/')[-1].split('?')[0]
    file_path = PREDICTION_IMAGES_PATH / f'{filename}'
    download_url(image_url, dest=file_path, overwrite=False)
    return file_path


def load_learner():
    model_name = config('MODEL_NAME')
    model_path = Path('./fastai_models')

    learner = load_learner(path=model_path, file=model_name)
    return learner


async def predict(request):
    request_params = await request.json()
    print(request_params)
    try:
        image_path = await validate_and_download_image(request_params)
        prediction_scores = await classify(image_path)
        return JSONResponse({'api_version': 1.0,
                             'data': {
                                 'image_url': request_params,
                                 'image_path': image_path.__str__(),
                                 'prediction_scores': prediction_scores
                             }, 'errors': {

            },
                             'success': True})
    except ValidationError as e:
        return JSONResponse({'api_version': 1.0,
                             'data': {
                                 'image_url': request_params,
                                 'image_path': None
                             },
                             'errors': {
                                'message': str(e)
                             },
                             'success': False})
