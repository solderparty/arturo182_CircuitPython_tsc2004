# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-FileCopyrightText: 2021 arturo182
# SPDX-License-Identifier: MIT

import board
from tsc2004 import TSC2004

i2c = board.I2C()
tsc = TSC2004(i2c)

print("Go Ahead - Touch the Screen - Make My Day!")
while True:
    if tsc.touched:
        print(tsc.read_data())

