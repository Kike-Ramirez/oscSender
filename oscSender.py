
""" sending OSC with pyOSC
https://trac.v2.nl/wiki/pyOSC
example by www.ixi-audio.net based on pyOSC documentation
"""


from OSC import OSCServer,OSCClient, OSCMessage
import time, random
import RPi.GPIO as GPIO

def my_callback(channel):
    value = random.randint(0,9)

    print('/Keydown detected, value %s'%value)
    msg = OSCMessage() #  we reuse the same variable msg used above overwriting it
    msg.setAddress("/keydown")
    msg.append(value)
    client.send(msg) # now we dont need to tell the client the address anymore

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)
GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback)

server_IP = '192.168.1.57', 8081
verbose = True

try:

    server = OSCServer( server_IP )
    server.timeout = 0
except:
    if verbose: print("No se encuentra el servidor OSC")

client_IP = '192.255.255.255', 8080

# Creamos el objeto "Cliente"
client = OSCClient()

# Realizamos la conexion
client.connect( client_IP )

try :    
    while 1: # endless loop

        msg = OSCMessage() #  we reuse the same variable msg used above overwriting it
        msg.setAddress("/ping")
        client.send(msg) # now we dont need to tell the client the address anymore
        time.sleep(1) # wait here some secs
        print("Ping...")

except KeyboardInterrupt:
    print "Closing OSCClient"
    client.close()
    print "Done"
        


