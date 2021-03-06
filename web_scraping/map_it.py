#! python3
# map_it.py - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from the command line
    address = ''.join(sys.argv[1:])
    # TODO: Get address from clipboard
else:
    # Get address form clipboard
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)