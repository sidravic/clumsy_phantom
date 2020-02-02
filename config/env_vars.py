import os
from starlette.config import Config

ENV = os.environ['ENV']
print(f'ENV is {ENV}')
config = Config(f'{ENV}.env')