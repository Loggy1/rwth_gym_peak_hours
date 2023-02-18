from PIL import Image, ImageDraw, ImageFilter
import pytesseract
from datetime import datetime, date
import pathlib
from globals import *


def read_image():
    # Transforming image to string
    insertIntoWhite()
    visitors = int(float(pytesseract.image_to_string(Image.open(path + "/scraper" + '/images/combined.jpg'), config='--psm 6 digits')))
    
    # Writing to db-file
    # File-Format: Weekday/Hour/Values.txt
    # Value-Format: Visitors
    time =  datetime.now()
    db_file = open(path + "/db/" + str(time.strftime('%A')) + "/" + str(time.strftime("%H")) + "/values.txt","a")
    db_file.write(str(visitors) + "\n")
    db_file.close()
    print("Visitors right now: " + str(visitors))
    changeBackgroundColor()


# Change background color of image to white
# Convertion to jpg
def changeBackgroundColor():
    im = Image.open(path + "/scraper" + '/images/my_file.png')
    fill_color = (255,255,255)  # white
    im = im.convert("RGBA")   # it had mode P after DL it from OP
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)
        background.paste(im, im.split()[-1]) # omit transparency
        im = background

    im.convert("RGB").save((path + "/scraper" + '/images/my_file.jpg'))

# Insert image into white background
# Pytesseract needs images which are bigger than these provided by rwth
def insertIntoWhite():
    changeBackgroundColor()
    im1 = Image.open(path + "/scraper" + '/images/White_paper.jpg')
    im2 = Image.open(path + "/scraper" + '/images/my_file.jpg')
    im1.paste(im2, (500, 500))
    im1.save(path + "/scraper" + '/images/combined.jpg', quality=100)

