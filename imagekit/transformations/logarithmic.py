import numpy as np


def logarithmic_transform(image, c=1):
    """Apply logarithmic transformation to the input image

    Formula:
        s = c * log(1 + r)

    Args:
        image (ndarray): Input image to be transformed
        c (float): Constant value to scale the logarithmic transformation

    Raises:
        TypeError: If the input is not a numpy array
        ValueError: If the input is not a grayscale or color image

    Returns:
        np.ndarray: Transformed image
    """

    # if image not numpy array return error
    if not isinstance(image, np.ndarray):
        raise TypeError(
            f"Input should be a numpy array. Expected <class 'numpy.ndarray'>, but got {type(image)}"
        )

    # if image not grayscale or color return error
    if len(image.shape) not in [2, 3]:
        raise ValueError(
            f"Input should be a grayscale or color image. Got {len(image.shape)} dimensions"
        )

    # Normalizing the image
    image = image / 255.0

    # Applying the logarithmic transformation
    transformed_img = c * np.log(1 + image)
    transformed_img = (transformed_img * 255.0).astype(np.uint8)

    return transformed_img
