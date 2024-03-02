import numpy as np


def negative_transform(image):
    """Invert the pixel values of the input image

    Args:
        image (ndarray): Input image to be transformed

    Raises:
        TypeError: If the input is not a numpy array
        ValueError: If the input is not a grayscale or color image

    Returns:
        ndarray: Transformed image
    """

    # check the image type
    if not isinstance(image, np.ndarray):
        raise TypeError(
            f"Input should be a numpy array. Expected <class 'numpy.ndarray'>, but got {type(image)}"
        )

    # check the image shape
    if len(image.shape) == 2:
        return 255 - image
    elif len(image.shape) == 3:
        # need to tackle each channel separately
        transformed_img = np.zeros_like(image)
        for i in range(image.shape[2]):
            transformed_img[:, :, i] = 255 - image[:, :, i]

        return transformed_img
    else:
        raise ValueError(
            f"Input should be a grayscale or color image. Got {len(image.shape)} dimensions"
        )
