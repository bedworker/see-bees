from fastai.vision.all import untar_data, URLs, ImageDataLoaders, get_image_files, Resize, error_rate, vision_learner, resnet34, PILImage
# from fastai.text.all import *
# from fastai.collab import *
# from fastai.tabular.all import *

path = untar_data(URLs.PETS)/'images'

def is_cat(x): return x[0].isupper()
dls = ImageDataLoaders.from_name_func(
    path, get_image_files(path), valid_pct=0.2, seed=42,
    label_func=is_cat, item_tfms=Resize(224), bs=8)

learn = vision_learner(dls, resnet34, metrics=error_rate)
# learn.fine_tune(1)

img = PILImage.create('./cat.jpg')
is_cat,_,probs = learn.predict(img)
print(f"Is this a cat?: {is_cat}.")
print(f"Probability it's a cat: {probs[1].item():.6f}")
