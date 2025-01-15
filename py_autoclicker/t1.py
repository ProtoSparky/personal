from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

trig = "æ"
rel = "ø"

def on_press(key):
    try:
        print(f'Key {key.char} pressed.')
        if key.char == trig:  # Trigger function when 'q' is pressed
            print('Function triggered by "q"!')
            routine()
    except AttributeError:
        print("Shit is fucked")
def routine():
    release_g = 0.15
    press_e = 0.15
    release_e = 0.15
    loop_time  = 0.1
    key_g = "g"
    key_e="e"
    keyboard = Controller() 
    while True:
        #Press a key
        keyboard.press(key_g)
        print("throw")
        time.sleep(release_g)
        keyboard.release(key_g)
        time.sleep(press_e)
        keyboard.press(key_e)
        print("catch")
        time.sleep(release_e)
        keyboard.release(key_e)
        time.sleep(loop_time)

def on_release(key):
    if key == keyboard.Key.caps_lock:  # Stop listener with escape
        return False
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

