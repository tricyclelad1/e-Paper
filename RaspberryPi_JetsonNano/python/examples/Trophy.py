#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import json

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

scoreboard = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'scoreboard.json')
portraitdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'portraits')
symboldir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'symbols')


import logging
from waveshare_epd import epd4in26
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:

   

    logging.info("Trophy")
    epd = epd4in26.EPD() 

    logging.info("Read scoreboard file")
    #Open file and load the data
    with open(scoreboard, 'r') as file:
        data = json.load(file)

    #Access Scoreboard
    winner = data['winner']
    player2 = data['player2']
    player3 = data['player3']
    player4 = data['player4']
    player5 = data['player5']
    player6 = data['player6']
    player7 = data['player7']
    player8 = data['player8']

    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font18 = ImageFont.truetype(os.path.join(libdir, 'TIFont.otf'), 18)
    font40 = ImageFont.truetype(os.path.join(libdir, 'TIFont.otf'), 40)
    font44 = ImageFont.truetype(os.path.join(libdir, 'TIFont.otf'), 44)
 

    #Drawing on the Horizontal Image
    logging.info("Drawing on the Horizontal image...")


    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame

    #Load the winner and leverage that both portrait and symbol use the same filename 
    winnerName = winner['name']
    winnerTitle = winner['title']
    winnerFaction = winner['faction']
    winnerImage = winnerFaction + ".jpg" 
    
    #Load each image element
    backgroundImage = Image.open(os.path.join(libdir, 'background.jpg'))
    portraitImage = Image.open(os.path.join(portraitdir, winnerImage))
    symbolImage = Image.open(os.path.join(symboldir, winnerImage))

    #Add each element to buffer
    Himage.paste(backgroundImage, (0,0))
    Himage.paste(portraitImage, (15,168))
    Himage.paste(symbolImage, (575,212))

    #Display Buffer to screen
    epd.display_Fast(epd.getbuffer(Himage))
    time.sleep(2)

    draw = ImageDraw.Draw(Himage)
    draw.text((400, 112), winnerName + " - " + winnerTitle, font = font40, fill = 0, anchor="mm") #400x195 is center of winner box

    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
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
