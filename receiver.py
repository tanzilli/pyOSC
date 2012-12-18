#https://trac.v2.nl/wiki/pyOSC
#https://github.com/ptone/pyosc

from OSC import OSCServer,OSCClient, OSCMessage
import sys
from time import sleep
import types

server = OSCServer( ("0.0.0.0", 8000) )
client = OSCClient()
client.connect( ("192.168.1.3", 9000) )

def handle_timeout(self):
	print ("Timeout")

server.handle_timeout = types.MethodType(handle_timeout, server)

def user_callback(path, tags, args, source):
#	global client
	print ("path", path) 
	print ("args", args) 
	print ("source", source) 
	msg=OSCMessage("/2/fader2")
	msg.append(args);
	client.send(msg)
	msg=OSCMessage("/2/fader3")
	msg.append(args);
	client.send(msg)
	msg=OSCMessage("/2/rotary1")
	msg.append(args);
	client.send(msg)

def toggle33_callback(path, tags, args, source):
	print ("path", path) 
	print ("args", args) 
	print ("source", source) 


server.addMsgHandler( "/2/fader1",user_callback)
server.addMsgHandler( "/6/toggle33",toggle33_callback)

while True:
	server.handle_request()

server.close()


