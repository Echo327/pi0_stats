#Stats(Bars AND Percentage)

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Alternatively you can specify a software SPI implementation by providing
# digital GPIO pin numbers for all the required display pins.  For example
# on a Raspberry Pi with the 128x32 display you might use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, sclk=18, din=25, cs=22)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# font = ImageFont.truetype('Minecraftia.ttf', 8)

cmd = "grep MemTotal /proc/meminfo | awk '{printf \"%s\",$2/1024/1024}'"
MemTotal = subprocess.check_output(cmd, shell = True )

# Set display contrast to a minimum
disp.set_contrast(0)

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring:
    # TEMP
    cmd = "cat /sys/class/thermal/thermal_zone0/temp"
    TEMP = subprocess.check_output(cmd, shell = True )
    TEMP = str(format(float(TEMP)/1000, '.0f')) + "'C"
    # CPU
    cmdt = "grep cpu /proc/stat | awk 'NR==1{printf \"%s\",$2+$3+$4+$5+$6+$7+$8+$9+$10+$11}'"
    cmdi = "grep cpu /proc/stat | awk 'NR==1{printf \"%s\",$5}'"
    CPUt = subprocess.check_output(cmdt, shell = True )
    CPUi = subprocess.check_output(cmdi, shell = True )
    CPU = ((float(CPUt)-float(CPUi))/float(CPUt))*100
    CPU = format(CPU, '.0f')
    CPUheight = float(CPU) * 0.1
    CPUheight = format(CPUheight, '.0f')
    # Memory
    cmd = "grep MemFree /proc/meminfo | awk '{printf \"%s\",$2/1024/1024}'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    MemPerc = (float(MemUsage)/float(MemTotal)) * 10
    MemPerc2 = MemPerc*10
    MemPerc2 = format(MemPerc2, '.0f')
    MemPerc = format(MemPerc, '.0f')
    # Disk Usage
    cmd =  "df -h | grep root | awk '{printf \"%.0f\",$5}'"
    Disk = subprocess.check_output(cmd, shell = True )
    DiskHeight = int(Disk) * 0.1
    
    # Write lines of text.
    draw.text((x, top),     "CPU: ", font=font, fill=255)
    draw.text((x+(width*0.25), top),  "MEM: ", font=font, fill=255)
    draw.text((x+(width*0.49), top),  "DISK: ", font=font, fill=255)
    #draw.text((x+(width*0.75), top),  "GPU: ", font=font, fill=255)
    draw.rectangle(( x+2,  top+10, x+17, bottom-15), outline=255, fill=0)
    draw.rectangle(( x+2+(width*0.25), top+10, x+17+(width*0.25), bottom-15), outline=255, fill=0)
    draw.rectangle(( x+2+(width*0.50), top+10, x+17+(width*0.50), bottom-15), outline=255, fill=0)
    #draw.rectangle(( x+2+(width*0.75), top+10, x+17+(width*0.75), bottom-15), outline=255, fill=0)
    # CPU Usage
    draw.rectangle(( x+3, bottom-15-int(CPUheight), x+16, bottom-16), outline=255, fill=1)
    draw.text((x, bottom-15),  str(CPU) + "%", font=font, fill=255)
    draw.text((x+(width*0.75), bottom-15),  TEMP, font=font, fill=255)
    # Memory Usage
    MemHeight = float(MemPerc)*((top+11)-(bottom-16))
    draw.rectangle(( x+3+(width*0.25), bottom-15-int(MemPerc), x+16+(width*0.25), bottom-16), outline=255, fill=1)
    draw.text((x+(width*0.25), bottom-15),  str(MemPerc2)+"%", font=font, fill=255)
    # Disk Usage
    draw.rectangle(( x+3+(width*0.50), bottom-15-int(DiskHeight), x+16+(width*0.50), bottom-16), outline=255, fill=1)
    draw.text((x+(width*0.50), bottom-15), Disk+"%", font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(0.1)
