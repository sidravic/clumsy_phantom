import boto3
from fastai.core import Path
from config.env_vars import config


def download_model_from_s3():
    print('Downloading model...')

    bucket = config('BUCKET')
    key = config('MODEL_KEY')

    s3_access_key = config('S3_ACCESS_KEY')
    s3_secret_accesskey = config('S3_SECRET_ACCESS_KEY')

    filename = key.split('/')[-1]
    model_path = Path(f'./fastai_models/{filename}')

    if not model_path.exists():
        print(f'Downloading file to {model_path.__str__()}')
        s3_client = boto3.client('s3',
                                 aws_access_key_id=s3_access_key,
                                 aws_secret_access_key=s3_secret_accesskey)

        s3_client.download_file(bucket, key, model_path.__str__())
        print(f'Download complete.')
    else:
        print(f'{model_path} exists.')

