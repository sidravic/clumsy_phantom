from config.env_vars import config
from fastai.core import Path
from fastai.basic_train import load_learner
from fastai.vision.image import open_image

model_name = config('MODEL_NAME')
model_path = Path('./fastai_models')
learner = load_learner(path=model_path, file=model_name)

PREDICTION_IMAGES_PATH = Path('./prediction_images')


async def classify(img_path):
    img = open_image(img_path)
    first, klass, losses = learner.predict(img)
    sorted_scores = sorted(zip(learner.data.classes, map(float, losses)), key=lambda p: p[1], reverse=True)
    return sorted_scores[:10]