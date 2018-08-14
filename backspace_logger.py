#!/usr/bin/env python3

from pynput import keyboard
import time
import datetime
import pystray
from PIL import Image, ImageDraw
import threading
from pystray import MenuItem as item


backspaces = {}
keys_pressed = {}


def update_tray():
    threading.Timer(15.0, update_tray).start()
    now = time.time()
    counter = 1
    for k in backspaces.keys():
        if not k < now - datetime.timedelta(minutes=20).total_seconds():
            counter += 1
    total = 1
    for ky in keys_pressed.keys():
        if not ky < now - datetime.timedelta(minutes=20).total_seconds():
            total += 1
    ratio = counter / total
    if ratio > 0.1 and ratio <= 0.3:
        color = 'darkorange'
    elif ratio > 0.3 and ratio <= 0.5:
        color = 'orangered'
    elif ratio > 0.5:
        color = 'red'
    else:
        color = 'orange'
    image = icon_generator(ratio, color)
    icon._icon = image
    icon._update_icon()
    print('backspace used {}/{} in the last 20 minutes, ratio: {}'.format(counter//2, total//2, ratio*1.2))


def icon_generator(n, color):
    # Generate an image
    width = 16
    height = 16

    color2 = 'black'
    image = Image.new('RGB', (width, height), color)
    dc = ImageDraw.Draw(image)
    # dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
    dc.rectangle((0, 16-16*(n*1.2) , width, 0), fill=color2)
    return image


def setup(icon):
    icon.visible = True
    update_tray()

    def on_release(key):
        now = time.time()
        if str(key) == 'Key.backspace':
            backspaces[now] = 'Key.backspace'
        else:
            keys_pressed[now] = key
        if str(key) == 'Key.pause':
            print('Exiting...')
            return False

    with keyboard.Listener(on_press=on_release) as listener:
        listener.join()


image = icon_generator(0, 'orange')
icon = pystray.Icon('backspace listener')
icon._icon = image
icon.run(setup)
