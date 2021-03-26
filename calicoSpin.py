# calicoSpin.py
# https://pydirectinput.readthedocs.io/_/downloads/en/latest/pdf/
# automatic calico slots player
import pyautogui
from pynput.keyboard import *
import pydirectinput
import time

# keymap and settings
delay = 1  # seconds
resumeKey = Key.f1
pauseKey = Key.f2
stopKey = Key.esc

# running modifiers (start as True = All ok!)
pause = True
running = True

# functions

def on_press(key):  # switch program status on keypress
    global running, pause  # running and pause are modifiable in on_press
    if key == resumeKey:
        pause = False
        print('Resume')
    elif key == pauseKey:
        pause = True
        print('Pause')
    elif key == stopKey:
        running = False
        print('Stop')
    else:
        pass

def display_controls():
    print('Cursor position stored! Ready to click.')
    print('Settings: ')
    print('\t delay = ' + str(delay) + ' sec' + '\n')
    print('Controls: \n')
    print('F1 = Resume \n' +
          'F2 = Pause \n' +
          'F3 = Exit')
    print('\n Press F1 to start . . .')


def main():
    cursorX, cursorY = pyautogui.position()
    keyPress = Listener(on_press=on_press)  # check for keypress
    keyPress.start()
    display_controls()  # show keymap
    while running:  # continue operating in running state
        if not pause:  # if program is not paused, click:
            for item in sequence:
                pydirectinput.mouseDown(
                    x=cursorX, y=cursorY, button='left')  # click at mouse pos
                # click at mouse pos
                pydirectinput.mouseUp(x=cursorX, y=cursorY, button='left')
                pydirectinput.PAUSE = delay  # wait duration (def = 1s)

    keyPress.stop()  # end input check (listening)

# main
if __name__ == '__main__':
    main()  # run main program (f*** __name__ == __main__)

"""
Working improvement for given sequence:
NOTE: offset(cursoryY value on Loss)must vary based on
screen resolution and window size.
Alternatively, use button PNG's.


def autoClickSequence():
    # save cursor position at program start, autoclick in sequence to exploit
    # currently cursor must be centred on BET 100 button

    cursorX, cursorY = pyautogui.position()
    sequence = 'L L L L L L L L L L L L L L W L W L W L W L W'.split(' ')
    keyPress = Listener(on_press=on_press)  # check for keypress
    keyPress.start()
    display_controls()  # show keymap
    while running:  # continue operating in running state
        if not pause:  # if program is not paused, click:
            for item in sequence:   # click at mouse pos
                if item == 'W':
                    print('Predicted win, betting the farm.\n')
                    pydirectinput.mouseDown(
                        x=cursorX, y=cursorY, button='left')
                    pydirectinput.mouseUp(
                        x=cursorX, y=(cursorY - 65
                                      ), button='left')

                    pydirectinput.PAUSE = delay  # wait duration (def = 1s)
                    492 - 427
                elif item == 'L':
                    print('Predicted loss, greasing the wheels.\n')
                    pydirectinput.mouseDown(
                        x=cursorX, y=cursorY, button='left')
                else:
                    time.sleep(1)
                    print('SKIP: Item in sequence is not'
                          + 'a W or L prediction...\n')
    keyPress.stop()  # end input check (listening)


"""
