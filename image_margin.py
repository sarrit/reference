from PIL import Image, ImageOps

def setMargin(img, margin_top_mm=0, margin_right_mm=0):

    #mm to px
    margin_top = int(margin_top_mm*5.6)
    margin_right = int(margin_right_mm*5.6)

    if margin_top >= 0:
        top = abs(margin_top)
        bottom = 0
    else:
        top = 0
        bottom = abs(margin_top)

    if margin_right >= 0:
        right = abs(margin_right)
        left = 0
    else:
        right = 0
        left = abs(margin_right)

    img = ImageOps.expand(img, border=(left,top,right,bottom), fill=(255, 255, 255, 255))
    return ImageOps.crop(img, border=(right,bottom,left,top)) # left, top, right, bottom

#img = Image.open("env9.jpg")
img = setMargin(img, margin_top_mm=0, margin_right_mm=10)
#img.save("barcode_new.jpg")







from scipy.ndimage import shift
from PIL import Image, ImageOps

def imageResize(img, margin_top_mm=0, margin_right_mm=0):
    left,top,right,bottom = 0,0,0,0
    margin_top_pix = int(margin_top_mm)
    margin_right_pix = int(margin_right_mm)
    
    if(margin_top_pix < 0):
        right = margin_top_pix
    else:
        left = margin_top_pix
        
    if(margin_right_pix < 0):
        bottom = margin_right_pix
    else:
        top = margin_right_pix
        
    print(top)
    
    image_reshape = ImageOps.expand(img, border=(left,top,right,bottom), fill=(255, 255, 255, 255))
    img_shifted = shift(image_reshape, (-margin_right_pix, -margin_top_pix, 0), mode='constant', cval=255)
    img = Image.fromarray(img_shifted)
    return img
    
    
img = Image.open("env9.jpg")
img = imageResize(img, margin_top_mm=0, margin_right_mm=50)
img.save("barcode_new.jpg")
