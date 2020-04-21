# Clumsy Phantom

Clumsy Phantom is a starter setup to serve Fastai-Pytorch models. The code base here is designed to run an image classifier response for the models stored in the `fastai_models` directory. It uses fastai libraries for loading the learner but this can be easily replaced with any other library. 

1. Images used for prediction are stored in a predictions folder but this can be replaced with storing them on s3
2. The entire stack is designed to work well with [First Hammer](https://github.com/sidravic/first-hammar)
