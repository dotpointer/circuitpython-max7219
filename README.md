# circuitpython-max7219
**CircuitPython driver for MAX7219 with 7-segment modules**

This is a driver for 7 segment display modules using the MAX7219 driver chip on ESP32 microcontrollers running CircuitPython.

This driver is based on [JennaSys micropython-max7219 MicroPython driver for MAX7219 with 7-segment modules to CircuitPython](https://github.com/JennaSys/micropython-max7219/).

The reason for this driver is because the [Adafruit MAX7219 library](https://docs.circuitpython.org/projects/max7219/en/latest/api.html) only supports writing digits, the letters H, E, L, P and a few more characters to these type of displays.

At the time of writing this in september 2025, I found no other example or library to display more characters on these displays using CircuitPython on ESP32 and therefore I publish this to allow wider usage of these displays with more characters, they can be used for so much more than just to show numbers.

Features:
* Display letters, symbols, digits on the display
* Display standing or scrolling, type on single positions, clear, set brightness in 16 steps
* Utilizes software SPI bus and CS line defined in code, use the pins you want
* Supports cascading MAX7219 devices (only tested with 1)
* Number of digits per MAX7219 device can be specified
* Tested on Lolin WEMOS ESP32 S2 Mini clone with ESP32-S2FNR2 running CircuitPython 9.2.9

Some technical details from the original version:

_max7219.py_ uses an internal buffer (array) that is a direct representation of the display when flushed.  So buffer[0] is the leftmost digit in the display and buffer[digits] is the rightmost.  Also, digit0 is the leftmost and digit7 is rightmost for each MAX7219 device.  Cascaded devices add additional digits to the right.

If you have a pre-wired 7-segment display module that has the rightmost digit as digit0, then set the `reverse` parameter to `True` when you initialize the driver so that the digits will display in the correct order.

If less than 8 digits are connected to the MAX7219, set the `scan_digits` parameter when initializing so that the code propery handles text value inputs and cascading.  The digits initialization value represents the total number of digits across all cascaded devices.

_seven_segment_ascii.py_ maps ascii characters to their segment representations.  `get_char()` uses a DP-G-F-E-D-C-B-A bit order and `get_char2()` uses a DP-A-B-C-D-E-F-G bit order (which is what the MAX7219 specifies).

## ESP32 Example

```python
import board
import max7219
import time

# initialize the display - set the pins
display = max7219.SevenSegment(digits=8, scan_digits=8, pin_clk=board.SCK, pin_cs=board.D3, pin_din=board.MOSI, reverse=True)
# set the brightness, 0-15
display.brightness(0)
# one single letter
display.letter(2, 'A', flush=True)
time.sleep(1)
# a text
display.text("ABCDEF")
time.sleep(1)
# a number
display.number(3.14159)
time.sleep(1)
# a scrolling text
display.message("Hello World")
display.clear()

while True:
    time.sleep(100)
```

## Connections

| ESP32 pins  | MAX7219 LED Driver pins          |
|-------------|----------------------------------|
| 3.3V or 5V  | VCC                              |
| GND         | GND                              |
| GPIO35 MOSI | DIN, MOSI, SDI, DI, SI, SDA      |
| GPIO03 SDA  | CS, SS, CE, SSEL, NSS            |
| GPIO36 SCK  | CLK, SCK, SCLK, SCL              |

Note, DIN, CS and CLK pins on the microcontroller can be changed using pin_clk, pin_cs and pin_din arguments to SevenSegment. They are not locked to specific pins since this is software SPI, but you will have to use matching board.PIN names instead of board.MOSI and board.SCK.

## File list

| Name                   | Description                   | Required |
|------------------------|-------------------------------|----------|
| code.py                | Example                       | No       |
| LICENSE                | License                       | No       |
| max7219.py             | Library, required             | Yes      |
| README.md              | This read me file             | No       |
| seven_segment_ascii.py | ASCII to binary character map | Yes      |

## Credits
This library is based on:
* [JennaSys's MicroPython driver for MAX7219 with 7-segment modules](https://github.com/JennaSys/micropython-max7219/)

The MicroPython library is based on:
* [rm-hull's max7219.py (pre-2017 version)](https://github.com/rm-hull/max7219) for the Raspberry Pi ([PyPI Project](https://pypi.org/project/max7219/))
* [dmadison's Segmented LED Display - ASCII Library](https://github.com/dmadison/LED-Segment-ASCII)

## License

Licensed under the [MIT License](http://opensource.org/licenses/MIT).
