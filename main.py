import numpy as np
from PIL import ImageGrab
import cv2
import time
import math
from math import sqrt
from moves import moves


class BBot:
    me = [ 0, 0 ]

    enemy = [ 0, 0 ]


    def main():
        last_time = time.time()

        while True:
            #screen = np.array(ImageGrab.grab(bbox=(0,0,1920,1080)))
            screen = np.array(ImageGrab.grab(bbox=(500,300,1420,680)))
            # edit screen

            screen = BBot.match_me( screen )

            screen = BBot.match_enemy( screen )
            
            dist = round( sqrt( (BBot.me[0] - BBot.enemy[0])**2 + (BBot.me[1] - BBot.enemy[1])**2 ) )
            #dist = round( math.hypot(BBot.me[0] - BBot.me[1], BBot.enemy[0] - BBot.enemy[1]) )
            
            moves.make( BBot.me, BBot.enemy, dist )

            #show screen
            #print('Loop took {} MiliSeconds'.format( round((time.time()-last_time)*1000) ))
            last_time = time.time()

            #draw circles
            cv2.circle( screen, (BBot.me[0], BBot.me[1]), 25, (237,28,36), -1 )
            
            smallScreen = cv2.resize(screen, (0,0), fx=0.7, fy=0.7) 

            cv2.imshow('BBot',cv2.cvtColor(smallScreen, cv2.COLOR_BGR2RGB))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


    def match_me( screen ):
        template = cv2.imread("assets/me4.png", 0)
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        threshold = 0.6
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen, top_left, bottom_right, (237,28,36), -2)
            #cv2.circle( screen, (top_left[0]+10, top_left[1]+61), 25, (237,28,36), -1 )
            BBot.me = [ top_left[0]+10, top_left[1]+61 ]
            print( str(BBot.me[0]) + " - " + str(BBot.me[1]) )
            break

        return screen


    def match_enemy( screen ):
        template = cv2.imread("assets/enemy.png", 0)
        w, h = template.shape[::-1]

        hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([0,204,255])
        upper_blue = np.array([200,255,255])
        screen_gray = cv2.inRange(hsv, lower_blue, upper_blue)

        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(screen, top_left, bottom_right, (255,127,39), -2)
        cv2.circle( screen, (top_left[0]+10, top_left[1]+43), 25, (255,127,39), -1 )

        BBot.enemy = [ top_left[0]+10, top_left[1]+43 ]

        return screen


BBot.main()