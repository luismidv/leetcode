import numpy as np
"""
What it does: rescales all pixel values to the range [0,1].
Example: an image with values in [0, 255] becomes [0.0, 1.0].
Why [0,1]?
Many models (CNNs, computer vision transformers) are trained assuming input in this range.
Activation functions like sigmoid or ReLU behave more stably when inputs are small.
"""
def min_max_normalize(image):
    min_value = np.min(image)
    max_value = np.max(image)

    if max_value == min_value:
        return np.zeros_like(image, dtype == float)
    else:
        return (image - min_value)/(max_value - min_value)

"""
What it does: shifts data to have mean 0 and standard deviation 1.
Why?
Removes differences in brightness/contrast across images.
Essential for algorithms that assume data is Gaussian-like (e.g., PCA, k-means, linear models).
Why mean 0, std 1 specifically?
Centering at 0 makes the math work better (gradient descent oscillates less).
Scaling to unit variance makes every feature contribute equally.
"""
def z_score_normalize(image):
    mean = np.mean(image)
    std = np.std(image)

    if std == 0:
        return np.zeros_like(image)
    else:
        return (image-mean)/std

img = np.array(
    [
        [0,128,255],
        [64,192,32]], dtype=np.uint8)

min_max_normalize(img)
z_score_normalize(img)