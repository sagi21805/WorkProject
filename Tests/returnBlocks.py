import numpy as np
from skimage.util import view_as_blocks


def viewBlocks(image, block_size=2, cval=0, func_kwargs=None):


    if np.isscalar(block_size):
        block_size = (block_size,) * image.ndim
    elif len(block_size) != image.ndim:
        raise ValueError("`block_size` must be a scalar or have "
                         "the same length as `image.shape`")

    if func_kwargs is None:
        func_kwargs = {}

    pad_width = []
    for i in range(len(block_size)):
        if block_size[i] < 1:
            raise ValueError("Down-sampling factors must be >= 1. Use "
                             "`skimage.transform.resize` to up-sample an "
                             "image.")
        if image.shape[i] % block_size[i] != 0:
            after_width = block_size[i] - (image.shape[i] % block_size[i])
        else:
            after_width = 0
        pad_width.append((0, after_width))
        
    image = np.pad(image, pad_width=pad_width, mode='constant',
                   constant_values=cval)
    
    print(pad_width)

    blocked = view_as_blocks(image, block_size)
    
    return blocked
