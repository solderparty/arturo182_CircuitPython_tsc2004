# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-FileCopyrightText: 2021 arturo182 for Solder Party
# SPDX-License-Identifier: MIT

"""
Simple painting demo that draws on the Keyboard Featherwing
ILI9341 display using the TSC2004 resistive touch driver.
This code is based on the stmpe610_paint_demo by ladyada
"""

import board
import digitalio
from adafruit_rgb_display import ili9341, color565
import tsc2004

# Create a SPI bus object for the display
spi = board.SPI()

# Keyboard FeatherWing default pins
tft_cs = digitalio.DigitalInOut(board.D9)
tft_dc = digitalio.DigitalInOut(board.D10)

# Initialize display
display = ili9341.ILI9341(spi, cs=tft_cs, dc=tft_dc)

# Fill with black!
display.fill(color565(0, 0, 0))

# Create a I2C bus object for the touch driver
i2c = board.I2C()

# Create the touch driver object
tsc = tsc2004.TSC2004(i2c)

TS_MINX = 260
TS_MAXX = 4800
TS_MINY = 300
TS_MAXY = 2900

# This function help transforming the touch coordinate system to the display coordinates
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    if tsc.touched:
        for touch in tsc.touches:
            touch['x'] = _map(touch['x'], TS_MINX, TS_MAXX, 0, 320)
            touch['y'] = _map(touch['y'], TS_MINY, TS_MAXY, 0, 240)
            display.fill_rectangle(touch['x'] - 2, touch['y'] - 2, 4, 4, color565(255, 0, 0))
