#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd4in26
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Trophy")
    epd = epd4in26.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    #font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    #font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    #font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)


    font24 = ImageFont.truetype(os.path.join(picdir, 'TIFont.otf'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'TIFont.otf'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'TIFont.otf'), 35)

    # Drawing on the Vertical image
    #logging.info("Drawing on the Vertical image...")
    #Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    #draw = ImageDraw.Draw(Limage)
    #draw.text((2, 0), 'hello world', font = font18, fill = 0)
    #draw.text((2, 20), '4.26inch e-Paper', font = font18, fill = 0)
    #draw.text((20, 50), u'微雪电子', font = font18, fill = 0)
    #draw.line((10, 90, 60, 140), fill = 0)
    #draw.line((60, 90, 10, 140), fill = 0)
    #draw.rectangle((10, 90, 60, 140), outline = 0)
    #draw.line((95, 90, 95, 140), fill = 0)
    #draw.line((70, 115, 120, 115), fill = 0)
    #draw.arc((70, 90, 120, 140), 0, 360, fill = 0)
    #draw.rectangle((10, 150, 60, 200), fill = 0)
    #draw.chord((70, 150, 120, 200), 0, 360, fill = 0)
    #epd.display(epd.getbuffer(Limage))
    #time.sleep(2)

    #logging.info("read bmp file")
    #epd.init_Fast()
    #Himage = Image.open(os.path.join(picdir, 'HACAN.bmp'))
    #epd.display_Fast(epd.getbuffer(Himage))
    #epd.display_Fast(epd.getbuffer(Himage))
    #time.sleep(2)

    #logging.info("read bmp file on window")
    #Himage2 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    #bmp = Image.open(os.path.join(picdir, 'Ghosts.bmp'))
    #Himage2.paste(bmp, (50,10))
    #epd.display_Fast(epd.getbuffer(Himage2))
    #time.sleep(2)

    # Drawing on the Horizontal image
    logging.info("Drawing on the Horizontal image...")
    epd.init()
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    turtles = Image.open(os.path.join(picdir, 'Turtles.jpg'))
    Himage.paste(turtles, (0,0))

    time.sleep(2)
    Himage.text((100, 0), 'Twilight Imperium', font = font35, fill = 0)
    Himage.text((0, 400), 'PAX MAGNIFICA BELLUM GLORIOSUM', font = font35, fill = 0)

    time.sleep(2)
    logging.info("Clear...")
    epd.init()
    epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in26.epdconfig.module_exit(cleanup=True)
    exit()
