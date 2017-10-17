# pi0_stats
Displays CPU, Memory, RAM, and GPU usages and temperature on an SPI 128*32 display

Display used is an OLED SSD 1306
Currently being developed on a Pi Zero (Non WiFi version).

Having put my micro-controllers away because I am full time on a job hunt and they are too distracting, I don't have time for this. If anyone specifically requests for the files, then I might take the Pi0 out of the box that is in a bigger box that is inside a suitcase full of my other things (because I might have to move once I get a job so I'm already mostly packed). Other than a pi0, I have a NodeMCU, Arduino Nano, and Arduino Uno(clone), but no ongoing project at this time.

As it stands, there are two versions:
stats_v1 : A crude attempt by just reading from the command line (very heavy on the cpu, but fully functional)
stats_v2 : A continuation of v1, reading directly from files under / (light on the cpu, currently in debugging phase)
