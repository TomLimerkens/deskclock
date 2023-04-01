import board
import time
import math
import busio
import terminalio
import displayio
from adafruit_display_text import label
import gc9a01

displayio.release_displays()

import os
board_type = os.uname().machine

print(board_type)

print("** Assign pins")
#link pinouts to lcd driver
tft_clk = board.LCD_CLK
tft_mosi = board.LCD_DIN
tft_rst = board.LCD_RST
tft_dc = board.LCD_DC
tft_cs = board.LCD_CS
tft_bl = board.LCD_BL
spi = busio.SPI(clock=tft_clk,MOSI=tft_mosi)

print("** Link bus to display")
#setup the bus + link lcd driver
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = gc9a01.GC9A01(display_bus, width=240, height=240, backlight_pin=tft_bl)

#loadfrom disk
bitmap = displayio.OnDiskBitmap("/star.bmp")
bitmapred = displayio.OnDiskBitmap("/starred.bmp")
bitmapgreen = displayio.OnDiskBitmap("/stargreen.bmp")

#create tilegrid
tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

tile_red = displayio.TileGrid(bitmapred, pixel_shader=bitmapred.pixel_shader)
tile_green = displayio.TileGrid(bitmapgreen, pixel_shader=bitmapgreen.pixel_shader)

print("** set Display context")
#Set context
group = displayio.Group()
group.append(tile_grid)

groupred = displayio.Group()
groupred.append(tile_red)

groupgreen = displayio.Group()
groupgreen.append(tile_green)


display.show(group)

print("** draw label")
#Draw label
#text = "We have \nLiftoff!"
#text_area = label.Label(terminalio.FONT, text=text, color=0xFF0000,
#                        anchor_point=(0.5,0.5), anchored_position=(0,0))
#text_group = displayio.Group(scale=2)
#text_group.append(text_area)
#main.append(text_group)

print("** start animation")

theta = math.pi
r = 75
count = 0
while True:
    count +=1
    if count%3 == 0:
        print("A")
        display.show(group)
    if count%3 == 1:
        print("B")
        display.show(groupred)
    if count%3 == 2:
        print("C")
        display.show(groupgreen)


    #ditisfout
    print(time.monotonic(),"hello")
    time.sleep(3)

#    print(time.monotonic(),"hello")
#    text_group.x = 120 + int (r * math.sin(theta))
#    text_group.y = 120 + int (r * math.cos(theta))
#    theta -= 0.05
#    time.sleep(0.01)


