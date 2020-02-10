from PIL import Image
import array as arr
import copy


class MyListIterator:
    ''' Iterator class to make MyList iterable.
    https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
    '''

    def __init__(self, lst, pointer=False):
        # MyList object reference
        if pointer:
            self._lst: PointerList = lst
        else:
            self._lst: ArrayList = lst
        # member variable to keep track of current index
        self._index: int = 0

    def __next__(self):
        ''''Returns the next value from the stored MyList instance.'''
        if self._index < len(self._lst):
            value = self._lst[self._index]
            self._index += 1
            return value
        # End of Iteration
        raise StopIteration


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class PointerList:
    def __init__(self, size: int, value=None) -> None:
        """Creates a list of the given size, optionally intializing elements to value.
        The list is static. It only has space for size elements.
        Args:
        - size: size of the list; space is reserved for these many elements. 
        - value: the optional initial value of the created elements.
        Returns:
        none
        """
        self.size = size
        self.head = Node(value)  # head for the linkedlist
        temp: Node = self.head  # temporary node for iteration
        for _ in range(size):
            NewNode = Node(value)  # new node to be added to the list
            temp.next = NewNode
            temp = NewNode  # new node becomes the temporary node

    def __len__(self) -> int:
        '''Returns the size of the list. Allows len() to be called on it.
        Ref: https://stackoverflow.com/q/7642434/1382487
        Args:
        Returns:
        the size of the list.
        '''
        return self.size

    def __getitem__(self, i: int):
        '''Returns the value at index, i. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487
        Args:
        - i: the index from which to retrieve the value.
        Returns:
        the value at index i.
        '''
        # Ensure bounds.
        assert 0 <= i < len(self),\
            f'Getting invalid list index {i} from list of size {len(self)}'
        temp: Node = self.head
        for _ in range(i):  # traverse till i and return the current node
            temp = temp.next
        return (temp.data)

    def __setitem__(self, i: int, value) -> None:
        '''Sets the element at index, i, to value. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487
        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set
        Returns:
        none
        '''
        # Ensure bounds.
        assert 0 <= i < len(self),\
            f'Getting invalid list index {i} from list of size {len(self)}'
        temp: Node = self.head
        for _ in range(i):
            temp = temp.next
        temp.data = value

    def __iter__(self) -> MyListIterator:
        '''Returns an iterator that allows iteration over this list.
        Ref: https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
        Args:
        Returns:
        an iterator that allows iteration over this list.
        '''
        return MyListIterator(self, True)

    def get(self, i: int):
        '''Returns the value at index, i.
        Alternate to use of indexing syntax.
        Args:
        - i: the index from which to retrieve the value.
        Returns:
        the value at index i.
        '''
        return self[i]

    def set(self, i: int, value) -> None:
        '''Sets the element at index, i, to value.
        Alternate to use of indexing syntax.
        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set
        Returns:
        none
        '''
        self[i] = value


class ArrayList:
    '''A list interface.'''

    def __init__(self, size: int, value=None) -> None:
        """Creates a list of the given size, optionally intializing elements to value.
        The list is static. It only has space for size elements.
        Args:
        - size: size of the list; space is reserved for these many elements. 
        - value: the optional initial value of the created elements.
        Returns:
        none
        """
        self.size = size
        self.ArrayRed = arr.array('i', [])
        self.ArrayGreen = arr.array('i', [])
        self.ArrayBlue = arr.array('i', [])
        for _ in range(size):
            self.ArrayRed.append(value[0])
            self.ArrayGreen.append(value[1])
            self.ArrayBlue.append(value[2])

    def __len__(self) -> int:
        '''Returns the size of the list. Allows len() to be called on it.
        Ref: https://stackoverflow.com/q/7642434/1382487
        Args:
        Returns:
        the size of the list.
        '''
        return self.size

    def __getitem__(self, i: int):
        '''Returns the value at index, i. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487
        Args:
        - i: the index from which to retrieve the value.
        Returns:
        the value at index i.
        '''
        # Ensure bounds.
        assert 0 <= i < len(self),\
            f'Getting invalid list index {i} from list of size {len(self)}'
        return (self.ArrayRed[i], self.ArrayGreen[i], self.ArrayBlue[i])

    def __setitem__(self, i: int, value) -> None:
        '''Sets the element at index, i, to value. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487
        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set
        Returns:
        none
        '''
        # Ensure bounds.
        assert 0 <= i < len(self),\
            f'Getting invalid list index {i} from list of size {len(self)}'
        self.ArrayRed[i] = value[0]
        self.ArrayGreen[i] = value[1]
        self.ArrayBlue[i] = value[2]

    def __iter__(self) -> MyListIterator:
        '''Returns an iterator that allows iteration over this list.
        Ref: https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
        Args:
        Returns:
        an iterator that allows iteration over this list.
        '''
        return MyListIterator(self)

    def get(self, i: int):
        '''Returns the value at index, i.
        Alternate to use of indexing syntax.
        Args:
        - i: the index from which to retrieve the value.
        Returns:
        the value at index i.
        '''
        return self[i]

    def set(self, i: int, value) -> None:
        '''Sets the element at index, i, to value.
        Alternate to use of indexing syntax.
        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set
        Returns:
        none
        '''
        self[i] = value


class MyImage:
    """ Holds a flattened RGB image and its dimensions.
    """

    def __init__(self, size: (int, int), pointer=False) -> None:
        """Initializes a black image of the given size.
        Args:
        - size: (width, height) specifies the dimensions to create.
        Returns:
        none
        """
        # Save size, create a list of the desired size with black pixels.
        self.pointer = pointer
        width, height = self.size = size
        if pointer:
            self.pixels: PointerList = PointerList(
                width * height, value=(0, 0, 0))
        else:
            self.pixels: ArrayList = ArrayList(width * height, value=(0, 0, 0))

    def _get_index(self, r: int, c: int) -> int:
        """Returns the list index for the given row, column coordinates.
        This is an internal function for use in class methods only. It should
        not be used or called from outside the class.
        Args:
        - r: the row coordinate
        - c: the column coordinate
        Returns:
        the list index corresponding to the given row and column coordinates
        """
        # Confirm bounds, compute and return list index.
        width, height = self.size
        assert 0 <= r < height and 0 <= c < width, "Bad image coordinates: "\
            f"(r, c): ({r}, {c}) for image of size: {self.size}"
        return r*width + c

    def open(path: str, pointer=False):
        """Creates and returns an image containing from the information at file path.
        The image format is inferred from the file name. The read image is
        converted to RGB as our type only stores RGB.
        Args:
        - path: path to the file containing image information
        Returns:
        the image created using the information from file path.
        """
        # Use PIL to read the image information and store it in our instance.
        img: PIL.Image = Image.open(path)
        myimg: MyImage = MyImage(img.size, pointer)
        width, height = img.size
        # Covert image to RGB. https://stackoverflow.com/a/11064935/1382487
        img: PIL.Image = img.convert('RGB')
        # Get list of pixel values (https://stackoverflow.com/a/1109747/1382487),
        # copy to our instance and return it.
        for i, rgb in enumerate(list(img.getdata())):
            myimg.pixels.set(i, rgb)
        return myimg

    def save(self, path: str) -> None:
        """Saves the image to the given file path.
        The image format is inferred from the file name.
        Args:
        - path: the image has to be saved here.
        Returns:
        none
        """
        # Use PIL to write the image.
        img: PIL.Image = Image.new("RGB", self.size)
        img.putdata([rgb for rgb in self.pixels])
        img.save(path)

    def get(self, r: int, c: int) -> (int, int, int):
        """Returns the value of the pixel at the given row and column coordinates.
        Args:
        - r: the row coordinate
        - c: the column coordinate
        Returns:
        the stored RGB value of the pixel at the given row and column coordinates.
        """
        return self.pixels[self._get_index(r, c)]

    def set(self, r: int, c: int, rgb: (int, int, int)) -> None:
        """Write the rgb value at the pixel at the given row and column coordinates.
        Args:
        - r: the row coordinate
        - c: the column coordinate
        - rgb: the rgb value to write
        Returns:
        none
        """
        self.pixels[self._get_index(r, c)] = rgb

    def show(self) -> None:
        """Display the image in a GUI window.
        Args:
        Returns:
        none
        """
        # Use PIL to display the image.
        img: PIL.Image = Image.new("RGB", self.size)
        img.putdata([rgb for rgb in self.pixels])
        img.show()


def remove_channel(src: MyImage, red: bool = False, green: bool = False,
                   blue: bool = False) -> MyImage:
    """Returns a copy of src in which the indicated channels are suppressed.
    Suppresses the red channel if no channel is indicated. src is not modified.
    Args:
    - src: the image whose copy the indicated channels have to be suppressed.
    - red: suppress the red channel if this is True.
    - green: suppress the green channel if this is True.
    - blue: suppress the blue channel if this is True.
    Returns:
    a copy of src with the indicated channels suppressed.
    """
    i = 0 # iterator for writing on our image
    localImage = MyImage(src.size, src.pointer) #creating a new image so as to keep the 
                                                #original image intact

    for pixel in src.pixels: #using the iterator provided in our class implementation
        if red or not (green or blue): # if no channel is indicated then suppress the red
            pixel = (0, pixel[1], pixel[2]) #suppressing the red channel
        if green:
            pixel = (pixel[0], 0, pixel[2]) #suppressing the green channel
        if blue:
            pixel = (pixel[0], pixel[1], 0) #suppressing the blue channel
        localImage.pixels.set(i, pixel)
        i += 1 #iterator for our local image
    return localImage


def rotations(src: MyImage) -> MyImage:
    """Returns an image containing the 4 rotations of src.
    The new image has twice the dimensions of src. src is not modified.
    Args:
    - src: the image whose rotations have to be stored and returned.
    Returns:
    an image twice the size of src and containing the 4 rotations of src.
    """
    result = MyImage((src.size[0]*2, src.size[1]*2), src.pointer)   #creating an image twice the original size
    rotated: MyImage = degrees90(src) # rotating 90 degrees for the first time
    for count in range(4):
        for i in range(src.size[0]):
            for j in range(src.size[1]):
                x = rotated.get(i, j)                           #get the pixel from the rotated image
                if count == 0:
                    result.set(i, j, x)                         #set the pixels on top left
                elif count == 1:
                    result.set(i+src.size[1], j, x)             #set the pixels on bottom left
                elif count == 2:
                    result.set(i+src.size[1], j+src.size[1], x) #set the pixels on bottom right
                elif count == 3:
                    result.set(i, j+src.size[1], x)             #set the pixels on top right
        if count < 3: 
            rotated = degrees90(rotated)
    return result


def degrees90(locimage: MyImage) -> MyImage:
    n = locimage.size[0]
    for x in range(0, int(n/2)):
        for y in range(x, n-x-1):
            temp = locimage.get(x, y)                           # store current pixel in temp variable
            locimage.set(x, y, locimage.get(y, n-1-x))          # move values from right to top
            locimage.set(y, n-1-x, locimage.get(n-1-x, n-1-y))  # move values from bottom to right
            locimage.set(n-1-x, n-1-y, locimage.get(n-1-y, x))  # move values from left to bottom 
            locimage.set(n-1-y, x, temp)                        # assign temp to left 
    return locimage


def apply_mask(src: MyImage, maskfile: str, average: bool = True) -> MyImage:
    """Returns an copy of src with the mask from maskfile applied to it.
    maskfile specifies a text file which contains an n by n mask. It has the
    following format:
    - the first line contains n
    - the next n^2 lines contain 1 element each of the flattened mask
    Args:
    - src: the image on which the mask is to be applied
    - maskfile: path to a file specifying the mask to be applied
    - average: if True, averaging should to be done when applying the mask
    Returns:
    an image which the result of applying the specified mask to src.
    """
    mask, dimension = openfile(maskfile) #the function returns mask as 2D list and dimension of the mask as a tuple
    avg = 0
    # makes a local copy of the given MyImage object
    LocalImage = MyImage(src.size, src.pointer) # creating our object of MyImage
    width, height = src.size 
    for i in range(height): 
        for j in range(width):
            # traverse over each pixel on our src image
            pixel = src.get(i, j)
            pixel = mask[dimension//2][dimension//2] * (sum(pixel)//3) #multiply the middle element of our mask with our current pixel
            avg += mask[dimension//2][dimension//2] #summing the weights for average
            for k in range(1, dimension//2 + 1):
                #loop to traverse over the middle row and column of the mask and the corresponding pixel
                if j+k < width:
                    temp = src.get(i, j+k) #variable to store the neighbouring pixels
                    temp = mask[dimension//2][dimension //
                                              2 + k] * (sum(temp)//3) #taking the average and then multiplying with the corresponding weight
                    avg += mask[dimension//2][dimension//2+k]
                    pixel += temp
                if j-k > -1:
                    temp = src.get(i, j-k)
                    temp = mask[dimension//2][dimension //
                                              2 - k] * (sum(temp)//3)
                    avg += mask[dimension//2][dimension//2-k]
                    pixel += temp
                if i+k < height:
                    temp = src.get(i+k, j)
                    temp = mask[dimension//2+k][dimension//2] * (sum(temp)//3)
                    avg += mask[dimension//2+k][dimension//2]
                    pixel += temp
                if i-k > -1:
                    temp = src.get(i-k, j)
                    temp = mask[dimension//2-k][dimension//2] * (sum(temp)//3)
                    avg += mask[dimension//2-k][dimension//2]
                    pixel += temp
                for l in range(1, dimension//2 + 1):
                    #loop to traverse over the rest of the mask and the corresponding pixels
                    if i+k < height and j+l < width:
                        temp = src.get(i+k, j+l)
                        temp = mask[dimension//2 +
                                    k][dimension//2 + l] * (sum(temp)//3)
                        avg += mask[dimension//2 + k][dimension//2 + l]
                        pixel += temp
                    if i-k > -1 and j+l < width:
                        temp = src.get(i-k, j+l)
                        temp = mask[dimension//2 -
                                    k][dimension//2 + l] * (sum(temp)//3)
                        avg += mask[dimension//2 - k][dimension//2 + l]
                        pixel += temp
                    if i+k < height and j-l > -1:
                        temp = src.get(i+k, j-l)
                        temp = mask[dimension//2 +
                                    k][dimension // 2 - l] * (sum(temp)//3)
                        avg += mask[dimension//2 + k][dimension//2 - l]
                        pixel += temp
                    if i-k > -1 and j-l > -1:
                        temp = src.get(i-k, j-l)
                        temp = mask[dimension//2 -
                                    k][dimension // 2 - l] * (sum(temp)//3)
                        avg += mask[dimension//2 - k][dimension//2 - l]
                        pixel += temp
            if average: #condition to check whether average is required or not
                pixel = pixel // avg 
                avg = 0
            pixel = min(max(0, pixel), 255) # to make sure that our pixel value does not exceed 255
            LocalImage.set(i, j, (pixel, pixel, pixel)) #writing the pixel onto our image
    return LocalImage


def openfile(maskfile):
    maskfile = open(maskfile, 'r')  # open the given file for reading
    dimension = int(maskfile.readline())  # reads the dimension of the mask
    mask = [[int(maskfile.readline()) for _ in range(dimension)] #read the mask as a 2D list
            for _ in range(dimension)]
    return (mask, dimension)


# newimage: MyImage = MyImage.open("images/campus.jpeg")
# newimage = apply_mask(newimage, "masks/mask-blur-more.txt")
# newimage.show()
