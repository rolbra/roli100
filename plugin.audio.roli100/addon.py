"""
Audio Addon that lists items of a given directory
"""

# Step 1 - load in xbmc core support and setup the environment
import xbmcplugin
import xbmcgui
import sys
import os

# magic; id of this plugin - cast to integer
thisPlugin = int(sys.argv[1])

# Step 2 - create the support functions (or classes)
def createListing():
	#static items (no fies)
	listing = []
	listing.append('The first item')
	listing.append('The second item')
	listing.append('The third item')
	listing.append('The fourth item')
	return listing
	
def getListing():
	#items in a directory (audio files)
	directory = "D:\incoming\MUSIK\Alicia Keys - Here (MP3)"
	listing = os.listdir(directory)
	return listing

def sendToXbmc(listing):
	#access global plugin id
	global thisPlugin
	# send each item to xbmc
	for item in listing:
		listItem = xbmcgui.ListItem(item)
		xbmcplugin.addDirectoryItem(thisPlugin,'',listItem)
	# tell xbmc we have finished creating the directory listing
	xbmcplugin.endOfDirectory(thisPlugin)

# Step 3 - run the program
sendToXbmc(getListing())