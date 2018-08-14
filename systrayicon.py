import pystray
from PIL import Image, ImageDraw

# Generate an image
width = 16
height = width
color1 = 'red'
color2 = 'green'
image = Image.new('RGB', (width, height), color1)
dc = ImageDraw.Draw(image)
dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
dc.rectangle((0, height // 2, width // 2, height), fill=color2)

icon = pystray.Icon('test name')
icon._icon = image

def setup(icon):
    icon.visible = True

icon.run(setup)