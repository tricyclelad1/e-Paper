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
    font35 = ImageFont.truetype(os.path.join(picdir, 'FTIFont.ot'), 35)

    # Drawing on the Vertical image
    logging.info("Drawing on the Vertical image...")
    Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Limage)
    draw.text((2, 0), 'hello world', font = font18, fill = 0)
    draw.text((2, 20), '4.26inch e-Paper', font = font18, fill = 0)
    draw.text((20, 50), u'微雪电子', font = font18, fill = 0)
    draw.line((10, 90, 60, 140), fill = 0)
    draw.line((60, 90, 10, 140), fill = 0)
    draw.rectangle((10, 90, 60, 140), outline = 0)
    draw.line((95, 90, 95, 140), fill = 0)
    draw.line((70, 115, 120, 115), fill = 0)
    draw.arc((70, 90, 120, 140), 0, 360, fill = 0)
    draw.rectangle((10, 150, 60, 200), fill = 0)
    draw.chord((70, 150, 120, 200), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Limage))
    time.sleep(2)

    logging.info("read bmp file")
    epd.init_Fast()
    Himage = Image.open(os.path.join(picdir, 'in5_V2.bmp'))
    epd.display_Fast(epd.getbuffer(Himage))
    time.sleep(2)

    logging.info("read bmp file on window")
    Himage2 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
    Himage2.paste(bmp, (50,10))
    epd.display_Fast(epd.getbuffer(Himage2))
    time.sleep(2)

    # Drawing on the Horizontal image
    logging.info("Drawing on the Horizontal image...")
    epd.init()
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'hello world', font = font24, fill = 0)
    draw.text((10, 20), '4.26inch e-Paper', font = font24, fill = 0)
    draw.text((150, 0), u'微雪电子', font = font24, fill = 0)
    draw.line((20, 50, 70, 100), fill = 0)
    draw.line((70, 50, 20, 100), fill = 0)
    draw.rectangle((20, 50, 70, 100), outline = 0)
    draw.line((165, 50, 165, 100), fill = 0)
    draw.line((140, 75, 190, 75), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw.rectangle((80, 50, 130, 100), fill = 0)
    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display_Base(epd.getbuffer(Himage))
    time.sleep(2)

    # partial update
    logging.info("5.show time")
    # epd.init()
    # epd.Clear()
    # Himage = Image.new('1', (epd.width, epd.height), 255)
    # draw = ImageDraw.Draw(Himage)
    num = 0
    while (True):
        draw.rectangle((10, 120, 130, 170), fill = 255)
        draw.text((10, 120), time.strftime('%H:%M:%S'), font = font24, fill = 0)
        epd.display_Partial(epd.getbuffer(Himage))
        num = num + 1
        if(num == 10):
            break

    '''4Gray display'''
    logging.info("4Gray display--------------------------------")
    epd.init_4GRAY()
    
    Limage = Image.new('L', (epd.width, epd.height), 0)  # 255: clear the frame
    draw = ImageDraw.Draw(Limage)
    draw.text((20, 0), u'微雪电子', font = font35, fill = epd.GRAY1)
    draw.text((20, 35), u'微雪电子', font = font35, fill = epd.GRAY2)
    draw.text((20, 70), u'微雪电子', font = font35, fill = epd.GRAY3)
    draw.text((40, 110), 'hello world', font = font18, fill = epd.GRAY1)
    draw.line((10, 140, 60, 190), fill = epd.GRAY1)
    draw.line((60, 140, 10, 190), fill = epd.GRAY1)
    draw.rectangle((10, 140, 60, 190), outline = epd.GRAY1)
    draw.line((95, 140, 95, 190), fill = epd.GRAY1)
    draw.line((70, 165, 120, 165), fill = epd.GRAY1)
    draw.arc((70, 140, 120, 190), 0, 360, fill = epd.GRAY1)
    draw.rectangle((10, 200, 60, 250), fill = epd.GRAY1)
    draw.chord((70, 200, 120, 250), 0, 360, fill = epd.GRAY1)
    epd.display_4Gray(epd.getbuffer_4Gray(Limage))
    time.sleep(2)
    
    #display 4Gra bmp
    Himage = Image.open(os.path.join(picdir, 'HACAN.bmp'))
    epd.display_4Gray(epd.getbuffer_4Gray(Himage))
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
