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
