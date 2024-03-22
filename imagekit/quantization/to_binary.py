from imagekit.common import check_image


def to_binary(im, threshold=127):
    """Converts an image to binary image

    Args:
        im (np.ndarray): Input image
        threshold (int): Threshold value

    Returns:
        np.ndarray: Binary image
    """

    check_image(im)

    im[im > threshold] = 255
    im[im <= threshold] = 0

    return im
