# pi0_stats
Displays CPU, Memory, RAM, and GPU usages (text and barchart) and temperature (text) on an SPI 128x32 display

Display used is an OLED SSD 1306 on a Raspberry Pi Zero (Non WiFi version).

As it stands, there are two working versions:

(1) stats_bar_v1 : A crude attempt by just reading from the command line (very heavy on the cpu, but fully functional)

(2) stats_bar_v2 : Starting from v1 and modified to read directly from files under / (light on the cpu, currently checking for bugs and missing gpu activity)

(3) stats_bar_v3 : Not yet coded. Possibly one that tries to read these stats from an external system.

(4) stats_line_v1 : Not yet coded. I'm thinking line charts instead of bar charts.

EDIT(11/11/2017): I will add the files soon, hopefully this weekend. This is an old project I started when I had just gotten my pi0 and didn't have any other peripherals. Now I have all kind of sensors and just need to think of a good project that I can make.

EDIT(13/11/2017): I have copied the files from my pi0 (finally managed to do it without a screen and ssh), they should be up soon. Photos coming soon.

The library that I used is this one:
https://github.com/adafruit/Adafruit_SSD1306
I will upload a zip of the library as it was when I downloaded it to use (in case it has or gets modified).

EDIT:
Temporary - and lacking- instructions (knowledge of what you are doing is required) for Raspberry Pi (assuming OS is bare?):
sudo apt-get update


sudo apt-get install build-essential python-dev python-pip


sudo pip install RPi.GPIO


sudo apt-get install python-imaging python-smbus


cd Adafruit_Pytho n_SSD1306


sudo python setup.py install


sudo python ./stats_v2.py

