def rotations(src: MyImage) -> MyImage:
    """Returns an image containing the 4 rotations of src.
    The new image has twice the dimensions of src. src is not modified.
    Args:
    - src: the image whose rotations have to be stored and returned.
    Returns:
    an image twice the size of src and containing the 4 rotations of src.
    """
    result = MyImage((src.size[0]*2, src.size[1]*2))
    copy1: MyImage = copy.deepcopy(src)

    for count in range(4):
        copy2: MyImage = copy.deepcopy(copy1)
        rotated = degrees90(copy2)
        copy1 = copy2
        for i in range(src.size[0]):
            for j in range(src.size[1]):
                x = rotated.get(i, j)
                if count == 0:
                    result.set(i, j, x)
                elif count == 1:
                    result.set(i+src.size[1], j, x)
                elif count == 2:
                    result.set(i+src.size[1], j+src.size[1], x)
                elif count == 3:
                    result.set(i, j+src.size[1], x)

    return result


def degrees90(locimage: MyImage) -> MyImage:

    n = locimage.size[0]
    for x in range(0, int(n/2)):
        for y in range(x, n-x-1):
            temp = locimage.get(x, y)
            locimage.set(x, y, locimage.get(y, n-1-x))
            locimage.set(y, n-1-x, locimage.get(n-1-x, n-1-y))
            locimage.set(n-1-x, n-1-y, locimage.get(n-1-y, x))
            locimage.set(n-1-y, x, temp)

    return locimage
