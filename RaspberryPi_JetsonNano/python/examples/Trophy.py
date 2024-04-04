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

    font24 = ImageFont.truetype(os.path.join(picdir, 'TIFont.otf'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'TIFont.otf'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'TIFont.otf'), 35)

    #Drawing on the Horizontal Image
    logging.info("Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame

    background = Image.open(os.path.join(picdir, 'Background Test.jpg'))
    Himage.paste(background, (0,0))
    epd.display_Fast(epd.getbuffer(Himage))
    time.sleep(2)

    #draw = ImageDraw.Draw(Himage)
    #draw.rectangle((0,0,800,480), fill=0)
    #draw.rectangle((100,0,400,35), fill=255)
    #draw.rectangle((0,400,700,435), fill=255)
    #draw.text((100, 0), 'Twilight Imperium', font = font35, fill = 0)
    #draw.text((0, 400), 'PAX MAGNIFICA BELLUM GLORIOSUM', font = font35, fill = 0)
    #epd.display(epd.getbuffer(Himage))

    #time.sleep(2)
    #logging.info("Clear...")
    #epd.init()
    #epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in26.epdconfig.module_exit(cleanup=True)
    exit()
