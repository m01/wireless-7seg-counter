#!/usr/bin/env python2
import re, pexpect

conn = pexpect.spawn('telnet 192.168.1.254')
conn.expect('Username :')
conn.sendline("Administrator\r") # or SuperUser for O2 wireless boxes
conn.expect('Password :')
conn.sendline("UltraSecretPassword\r") # try your serial number
conn.expect("{Administrator}=>")
conn.sendline("wireless stations list\r")
conn.expect('{Administrator}=>')
output = conn.before
# extract nr of associated stations : X
m=re.search(r"Total number of associated stations : ([0-9]+)", output)

num_devices = int(m.groups()[0])

conn.sendline("exit\r") # log off
conn.close()

# now you just need to display it
print("There are " + str(num_devices) + " wireless devices connected")
from sevensegment import sevensegment
s=sevensegment.SevenSegmentDisplay()
s.set(num_devices)

