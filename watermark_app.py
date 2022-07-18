from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


window = Tk()
window.withdraw()

## Open the directory
filename = filedialog.askopenfilename(initialdir='/Users/gladys', title = 'Select an Image')
#print(filename)

def add_watermark(image, wm_text):
    opened_image = Image.open(image)

    image_width, image_height = opened_image.size
    draw  = ImageDraw.Draw(opened_image)

    #set the size of watermark text font
    font_size = int(image_width / 8)

    font = ImageFont.truetype('arial.ttf', font_size)

    #Coordinates for the Image
    x,y = int(image_width/2),int(image_height/2)   #this places the image at the center

    #Add watermark
    draw.text((x,y), wm_text, font=font,fill='white', stroke_fill="#222", anchor='ms')

    #show the selected image
    opened_image.show()

add_watermark(filename, 'Beauty Defined')


