import board
import max7219
import time

display = max7219.SevenSegment(digits=8, scan_digits=8, pin_clk=board.SCK, pin_cs=board.D3, pin_din=board.MOSI, reverse=True)
display.brightness(0)
display.letter(2, 'A', flush=True)
time.sleep(1)
display.text("ABCDEFG")
time.sleep(1)
display.number(3.14159)
time.sleep(1)
display.message("Hello World... A B C D E F G H I J K L M N O P Q R S T U V X Y Z")
display.clear()