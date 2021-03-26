# autoClicker.py
# https://pydirectinput.readthedocs.io/_/downloads/en/latest/pdf/
# automatic LMB click program with play controls for DirectX (Windows)
# applications.
import pyautogui
from pynput.keyboard import *
import pydirectinput

# keymap and settings
delay = 2  # seconds
resumeKey, pauseKey, stopKey = Key.f1, Key.f2, Key.esc

# running modifiers (start as True = run program as normal)
pause, running = True, True
delay = 1  # seconds
resumeKey, pauseKey, stopKey = Key.f1, Key.f2, Key.esc

# running modifiers (start as True = run program as normal)
pause, running = True

# program functions


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
    print('Moust position Saved! \n')
    print('Delay = ' + str(delay) + ' seconds \n')
    print('Controls: \n')
    print('\t F1 = Resume \n' +
          'F2 = Pause \n' +
          'F3 = Exit')
    print('Press F1 to begin . . .')


def main():
    display_controls()  # show keymap
    keyPress = Listener(on_press=on_press)  # check for keypress
    keyPress.start()

    cursorX, cursorY = pyautogui.position()
    while running:
        if not pause:
            pydirectinput.mouseDown(
                x=cursorX, y=cursorY, button='left')  # click at mouse pos
            # click at mouse pos
            pydirectinput.mouseUp(x=cursorX, y=cursorY, button='left')
            pydirectinput.PAUSE = delay  # wait duration (def = 1s)
    keyPress.stop()  # end input check (listening)


# main
if __name__ == '__main__':
    main()
