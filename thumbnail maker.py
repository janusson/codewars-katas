'''
create a centered thumbnail from image, exports to my desktop
Eric Janusson
'''
from PIL import Image

def createThumbnail(input_file, output_img, dimensions=(300,300)):
    '''
    create a centred thumbnail from an image.

    Args:
        input_file (pathlike): path of image to make a thumnail of
        output_img (pathlike): path of thumnail output
        dimensions (tuple, optional): thumbnail dimensions. 
        Defaults to (300,300).
    '''
    width, height = dimensions
    img = Image.open(input_file)
    dimensions = img.size

    if width > height:
        difference = width - height
        left = int(difference / 2)
        upper = 0
        right = height + left
        lower = height
    else:
        difference = height - width
        left = 0
        upper = int(difference / 2)
        right = width
        lower = width + upper
    print(left, upper, right, lower)
    img = img.crop()
    img.thumbnail(dimensions)
    img.save(output_img)

# test case
img1 =r''
out_name = r'C:\Users\ericj\Desktop\file_thumb.jpg'
out_size = (450, 450)
createThumbnail(img1, out_name, out_size)
