# twainstation (Please read this)!
Train Departure board checker with some cuteness added in!

# Introduction

Hewo ヾ(＾ ∇ ＾).

This is Twainstation, a Python departure board script which fetches departure board info from the RealTimeTrains API. This was made basically as a project for me to make a silly little departure board app and to try figure out how to do that in Python as a way to learn Python.

# How do use.

## Libraries needed/used

realtime-trains-py (https://pypi.org/project/realtime-trains-py/, pip install realtime-trains-py)
playsound (https://pypi.org/project/playsound/, pip install playsound)
pyfiglet (https://pypi.org/project/pyfiglet/, pip install pyfiglet)

os and sys should me included with your Python package.

If you are having trouble with playsound, install wheel with pip install wheel.

## API Login
***YOU WILL NEED AN API LOGIN***
You can get this from https://api.rtt.io/. Your API Username and password is the one on the page after logging in under ***API Auth Credentials***.
Your username should start with "rtt_" and the password will be a long string of numbers and letters.
I do not provide my own API key, hopefully I will find a way to hide it from the end user and this section will become redundant.
Simply replace the "none" in the ```username``` and ```password``` fields with your API username and password. 

## Actually using it
```cd``` into the folder containing the files and simply run ```python twainstation.py```

Once logged in it will ask for a three letter station code. To find one, go to https://www.realtimetrains.co.uk/, type in the station, and the three letter code for your station will be on the otherside of the name in gray.
It is, however, set by default to "EDB" (Edinburgh Waverley), if you wanna change that to your local station's code, you can. I'm not going to stop you. I just set it to EDB because it's my city's main station and I didn't wanna dox myself by having my location station in the Source Code. :3c

It will then act you how many services you wanna see. If you type "1" it'll just give you the next service. If you type "2", it will give you the next two services. It is by default set to "4" (showing the next four services). You can set it to more than four if you wanna.

It will then give you the services, show you a train, and leave.

# FAQ

## Will you be doing anything else with this.
Ye, gonna try see if I can't make it a live thing and not just quit after it's done. But right now my goal is to use some of the things I learnt to make a retro departures board.
## Was the Music and Kaomoji really necessary?
Yes. 🙃
## There's no licence, why?
It *does* use some copyrighted material, namely a soundclip from [This 1990 Thomas and Friends Game](https://youtu.be/cFEgNGEMA4c) and Edward's whistle from the OG TV Series. I don't think I'll get in shit for doing that. If the files disappear, that's why.
## Can I play around with the source code.
Yeah, go ahead.
