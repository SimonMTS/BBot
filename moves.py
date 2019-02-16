from pynput.keyboard import Key, Controller
import keyboard

class moves:

    def make( me, enemy, dist ):
        if keyboard.is_pressed('m'):
            #print("-")
            #print( str(me[0]) + " - " + str(me[1]) )
            #print( str(enemy[0]) + " - " + str(enemy[1]) )
            #print( str(dist) )

            #return
            if me[1] > 300:
                Controller().press('w')
                Controller().release('w')

            if dist > 71 and (me[0] < 375 or me[0] > 550 ):
                #print( me[0] )

                if me[0] < 375:
                    Controller().press('d')
                else:
                    Controller().press('a')
            else:
                Controller().release('a')
                Controller().release('d')

            #return
            if dist < 70:
                Controller().press('c')
                Controller().release('c')