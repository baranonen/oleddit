# Oleddit
A very tiny Reddit client that runs on a 0.96 inch OLED screen with a Raspberry Pi </br>
## Usage
Download these fonts and copy the .ttf files to the same directory as the python file: </br>
[VCD OSD Mono](https://www.dafont.com/vcr-osd-mono.font "VCD OSD Mono")</br>
[Coder's Crux](https://www.dafont.com/coders-crux.font "Coder's Crux") </br>
Install the [Adafruit SSD 1306 library](https://github.com/adafruit/Adafruit_Python_SSD1306 "Adafruit SSD 1306 library")</br>
Prepare the circuit according to this schematic</br>
![Oleddit Schematic](https://raw.githubusercontent.com/baranonen/oleddit/master/Schematics/Oleddit.png "Oleddit Schematic")</br>
Run oleddit.py</br>
You can change the `subreddit` variable to load posts from another subreddit</br>