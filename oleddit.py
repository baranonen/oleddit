# Copyright © Baran Önen 2020

import time
import RPi.GPIO as GPIO

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import urllib.request
import json

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

currentpage = 1

# Enter subreddit name
subreddit = "python"

# Raspberry Pi pin configuration:
RST = 24

# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Initializing the display and showing a loading message

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)


font = ImageFont.truetype("Coders' Crux.ttf", 15)

disp.begin()
disp.clear()

draw.text((25, 0),    "OLEDDIT",  font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf', 20), fill=255)
draw.text((0, 20),    "Please wait, loading",  font=font, fill=255)
draw.text((0, 30),    "data",  font=font, fill=255)
draw.text((0, 45),    "This may take a while",  font=font, fill=255)
disp.image(image)
disp.display()

# Fetching data

subjson = urllib.request.urlopen('https://www.reddit.com/r/' + subreddit + '/top/.json?count=5').read()
obj = json.loads(subjson)

currentpost = str(obj['data']['children'][currentpage - 1]['data']['title'])
currentpostauthor = str(obj['data']['children'][currentpage - 1]['data']['author'])
postquantity = int(obj['data']['dist'])

disp.clear()

draw.rectangle((0,0,width,height), outline=0, fill=0)
draw.text((25, 0),    "OLEDDIT",  font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf', 20), fill=255)
draw.text((0, 20),    "Press the button to",  font=font, fill=255)
draw.text((0, 30),    "navigate between",  font=font, fill=255)
draw.text((0, 40),    "posts",  font=font, fill=255)

disp.image(image)
disp.display()

time.sleep(3)

def render():

    disp.image(image)
    disp.display()

    disp.clear()

    draw.rectangle((0,0,width,height), outline=0, fill=0)

    draw.text((0, 0),    "r/" + subreddit,  font=font, fill=255)

    #draw.text((width - 41, 0),    "Oleddit",  font=font, fill=255)
    
    if currentpage > 9:
        draw.text((width - 29, 0),    str(currentpage) + "/" + str(postquantity),  font=font, fill=255)
    else:
        if postquantity > 9:
            draw.text((width - 23, 0),    str(currentpage) + "/" + str(postquantity),  font=font, fill=255)
        else:
            draw.text((width - 17, 0),    str(currentpage) + "/" + str(postquantity),  font=font, fill=255)
            
    draw.rectangle((-1,11,width,height), outline=255, fill=0)
    
    draw.text((0, 14),    "u/" + currentpostauthor[0:19],  font=font, fill=255)
    
    draw.text((0, 25, width , height),    (currentpost[0:21]),  font=font, fill=255)
    draw.text((0, 35, width , height),    (currentpost[21:42]),  font=font, fill=255)
    draw.text((0, 45, width , height),    (currentpost[42:63]),  font=font, fill=255)
    draw.text((0, 55, width , height),    (currentpost[63:84]),  font=font, fill=255)

    disp.image(image)
    disp.display()


render()

while True:
    if GPIO.input(15) == GPIO.HIGH:
        if currentpage == postquantity:
            time.sleep(0.2)
            currentpage = 1
            currentpost = str(obj['data']['children'][currentpage - 1]['data']['title'])
            currentpostauthor = str(obj['data']['children'][currentpage - 1]['data']['author'])
            render()
        else:
            time.sleep(0.2)
            currentpage = currentpage + 1
            currentpost = str(obj['data']['children'][currentpage - 1]['data']['title'])
            currentpostauthor = str(obj['data']['children'][currentpage - 1]['data']['author'])
            render()
