# These are the libraries you will need, get them if you don't have them :)
from realtime_trains_py import RealtimeTrainsPy
from playsound import playsound
import sys
import os
from pyfiglet import Figlet

title = Figlet(font = 'basic')
print("Welcome to")
print(" ")
print(title.renderText('TWAIN'))
print(title.renderText('STATION!'))

script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) # This gets the place the script and mp3 file is in
thomas_path = os.path.join(script_dir, 'thomas.mp3') # This sets the MP3 file!
playsound(thomas_path)

# Logging into API
print("Logging onto API (っº - ºς)")

# Login Info owo
# Pleae put your api login deets in username and password down there VVV
# Need an API login? Get it at https://api.rtt.io/
rtt = RealtimeTrainsPy(
	username="none",
	password="none",
	complexity="s.n"
)

# If you have got the info, then this will run!
print("Done! ٩(^ᗜ^ )و")
print("""What's the Station Code? owo
The default is set to Edinburgh (EDB)""")
stationcode = input("> ") # Can work with Tiploc, but also three letter station codes :3
if not stationcode:
	stationcode = "edb"

print("""
How many services you want to see? (▰╹◡╹▰)
The default is 4""")
serv = input("> ") # Lets you choose how many services you wanna see

if not serv:
	serv = 5
else:
	pass

# Get the departures
departures = rtt.get_departures(tiploc = stationcode, rows = int(serv))

 # All of this arranges the info in a readable way!
for departure in departures:
	# Print the details
	print(f"""
Platform {departure.platform}
{departure.gbtt_departure} service to {departure.terminus}
____________""")

 # A Choo Choo? In my departure Board?
print("""
⠀⠀⣀⡠⠤⠀⠐⠒⠒⡲⠶⠄⠠⣄⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠾⢿⠤⠀⠉⢉⣩⠏⣉⠓⠒⣳⠊⠀⠀⠀⠰⡏⠋⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢹⣿⠉⠀⠉⢹⢀⡄⠀⣀⣿⡔⢢⡸⠉⣢⡏⠉⣇⣀⣀⣀⠀⠀⠀⠀
⠀⠀⢸⠙⠟⠉⠉⠉⢲⠠⠊⡩⠋⠳⠞⠳⠶⠞⠲⠤⠷⠁⡌⡔⣱⡀⠀⠀
⠀⢀⡸⢜⣛⡛⠶⡰⣻⠆⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⡄⡇⠇⡸⠀⠀
⢠⢫⠊⠀⠀⠀⠁⢎⢺⠬⠄⣑⣄⣀⣀⣀⣀⣀⣀⣀⣈⣆⣱⣐⢾⣅⠀⠀
⠆⡅⠀⠸⠁⡱⠀⢈⢸⣠⡧⠶⢦⡀⣠⠴⠶⣄⢀⡤⠶⢤⣇⣿⣶⣿⣧⡀
⠘⣜⢄⡀⠀⠀⡀⢎⠌⢿⡁⠦⠄⣿⣇⠰⠄⢸⣿⠐⠶⢈⡿⢻⣿⣿⣻⡟
⠀⠈⠑⠨⠭⠥⠒⠁⠀⠈⠛⠶⠞⠁⠙⠳⠶⠋⠈⠳⠶⠟⠁⠀⠉⠑⠚⠃
""")
script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) # This gets the place the script and mp3 file is in
edward_path = os.path.join(script_dir, 'edward-the-blue-engine-whistle.mp3') # This sets the MP3 file!

playsound(edward_path) # This plays the file!
