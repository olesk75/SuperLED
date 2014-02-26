""" This file contains global variables used in the SuperLED project
	The objective is to shrink this file as much as possible and use
	function arguments in stead wherever possible.
"""

# Global variables
transmit_flag = False
abort_flag = None

DISPLAY_MODE = 'LED'  # One of 'curses', 'LED' or 'tkinter' - defaults to 'LED'
OFFLINE = None
DEBUG = False
NUM_LEDS = None

Arduino = ''    # The socket object that holds the connection to the Arduino

settings = {
	'OFFLINE': False,
	'DISPLAY_MODE': 'LED',
	'DEBUG': False
}

led_buffer = [''] * 256  # The list of bytes to be sent to curses or Arduino
for i in range(256):
	led_buffer[i] = [0, 0, 0]  # 256 x 3 list

transmit_buffer = [None] * 256  # We need this copy of the led_buffer to avoid overwriting while we do effects and prepare to transmit the data
for i in range(256):
	transmit_buffer[i] = [None] * 3
