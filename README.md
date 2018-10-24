# MinecraftAutoFisher

## Description
The goal of fishing in Minecraft is to cast your line and wait until the fishing bobber bobs in the water.
If you click quickly enough when that happens, you'll reel in a fish (or some treasure!).

This program ~~cheats~~ automates this process for you by watching the subtitles on the screen; When the bobber bobs,
it makes a splashing sound and if you have subtitles enabled the text 'Fishing Bobber splashes' appears. This program watches
the screen and right clicks whenever it sees that text, allowing it to keep reeling in fish as long as you leave it running.

## Installation
Requires [tesseract](https://github.com/tesseract-ocr/tesseract)

More details to come

## Usage
First, run `screengrabber.py`. This will open up a slightly transparent window, and you should click and drag a rectangle over
the area the subtitles usually appear on your screen. This will tell the program where to look for the subtitles, and only
needs to be done once.

Second, run `fisher.py`, which will begin watching the part of the screen you selected for the text "Fishing Bobber splashes"
(make sure you have your subtitles turned on in the Minecraft settings!). Then just cast your fishing rod and leave it running!
The program will right click whenever it sees the text to reel in the fish, then right click again to recast the line, giving
you an infinite supply of fish.
> Note: If the program doesn't see the text for 45 seconds, it will think something is wrong and right click twice to recast
the line, make sure Minecraft is actually on screen or your computer will just right click every 45 seconds!
