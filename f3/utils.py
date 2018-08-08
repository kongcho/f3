import numpy as np

# helper function for improve_aperture, pads any image to desired shape with pad_val
def pad_img(img, desired_shape, positions, pad_val=0):
    if len(desired_shape) != len(positions):
        logger.error("pad_img: odd required shape dimensions")
        return img
    pads = []
    for i, position in enumerate(positions):
        pad_len = desired_shape[i] - position - img.shape[i]
        if pad_len < 0 or position < 0:
            return img
        pads.append((position, pad_len))
    return np.pad(img, pads, mode='constant', constant_values=pad_val)


# function, pads image to fit desired_shape and fill up extra space with pad_val
def pad_img_wrap(img, desired_shape, sides, pad_val=0):
    offset_x = 0
    offset_y = 0
    if "Top" in sides:
        offset_y += desired_shape[0]-img.shape[0]
    if "Left" in sides:
        offset_x += desired_shape[1]-img.shape[1]
    img = pad_img(img, desired_shape, (offset_y, offset_x), pad_val)
    return img
