
""" sending OSC messages from Raspberry
    Author: Kike Ramirez
    15.09.2016

    Static IP Raspberry: 2.0.0.100
    Static IP Laptop: 2.0.0.1
    Sends a /ping every 2 seconds
    Sends a /keydown when botton is pushed
"""


from OSC import OSCServer,OSCClient, OSCMessage
import time, random
import RPi.GPIO as GPIO


server_IP = '2.0.0.100', 8081
client_IP = '2.0.0.1', 8080

timerPulse = 1
timePulse = time.time()

timerPing = 2
timePing = time.time()

def my_callback(channel):
    global timePulse;

    if (time.time() - timePulse) > timerPulse:

        try:
            msg = OSCMessage() #  we reuse the same variable msg used above overwriting it
            msg.setAddress("/keydown")
            client.send(msg) # now we dont need to tell the client the address anymore
            timePulse = time.time()
        except:
            print("Sin conexion OSC")

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)
GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback)

verbose = True

try:

    server = OSCServer( server_IP )
    server.timeout = 0
except:
    if verbose: print("No se encuentra el servidor OSC")

connected = False

while (connected == False):

    try:

        # Creamos el objeto "Cliente"
        client = OSCClient()

        # Realizamos la conexion
        client.connect( client_IP )

        connected = True
    except:
        print("Esperando cliente OS ")

print("Sending OSC messages to: " + str(client_IP))
try :    
    while 1: # endless loop

        if (time.time() - timePing) > timerPing:
            
            try: 
                msg = OSCMessage() #  we reuse the same variable msg used above overwriting it
                msg.setAddress("/ping")
                client.send(msg) # now we dont need to tell the client the address anymore
                timePing = time.time() 
            except:
                print("Sin conexion OSC")

except KeyboardInterrupt:
    print "Closing OSCClient"
    client.close()
    print "Done"
        


