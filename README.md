# VolumeControl

 Discord| Maintained|
| :-: | :-: |
| [![Discord](https://img.shields.io/discord/641713710087405589.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/C3gfHBJ) | [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) |

This program controls the volume of individual applications under Windows and was developed with Python.

## Necessary packages
- import pythoncom
- from pynput.keyboard import Key
- from pynput.keyboard import Listener
- from pycaw.pycaw import AudioUtilities

## Usage
In the release version 1.0.0, which can be found in this repository, there is an .exe. In this version I control the volume of the Microsoft flight simulator with the F1 key. If you press the button for the first time while the program is active. The volume of the simulator is set to 80%. If you press the button again, it is set to 5%. In this rhythm it goes on alternately.

## Editing
In order to be able to change the volume of another application, it is sufficient to specify the maximum and minimum value of the application in the main.py file under Constants. Then you can either replace FlightSimulator.exe with another name under Definitions or add another key.

# Contribution
I am very happy about each of you who want to expand the code with me. Please follow the following guidelines:

- Add an issue to this repository and give it a name
- Fork this repository and add your changes
- Create a pull-request with your changes
