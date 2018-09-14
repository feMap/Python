# -*- coding: utf-8 -*-

from matplotlib.cm import ScalarMappable
from IPython.display import Image

def func(x, y, a):
    return (x*x - y*y) * np.sin((x + y) / a) / (x*x + y*y)

def make_image(x, y, a, dtype="uint8"):
    z = func(x, y, a)
    img_rgba = ScalarMappable(cmap="jet").to_rgba(z)
    img = (img_rgba[:, :, 2::-1] * np.iinfo(dtype).max).astype
    return img

