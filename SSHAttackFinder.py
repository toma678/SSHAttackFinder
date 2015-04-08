"""
SSHAttackFinder lists IPs of possible brute force attacks via SSH.
    Copyright (C) 2015  Toma678

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import re
import os

auth = open("/var/log/auth.log","r").read() #Opens the logfile for reading
IPsf = open(os.getcwd()+"/IPs", "w+") #Opens the file that holds the IPs for reading and writing
IPs = IPsf.read()
a = re.findall(r'sshd.+Failed.+', auth)
IPset = set() #Initializes the set
for item in IPs: #Adds the IPs already listed in the file to the set
	IPset.add(item)
for item in a: #Pulls the IP from the string using regex
	findIP = re.findall( r'[0-9]+(?:\.[0-9]+){3}', item)
	if findIP: #Runs boolean check that the IP exists, then adds to set
		IPset.add(findIP[0])
for item in IPset: #Once the set is populated, it writes to the file (which is wiped by the w+ open option)
	IPsf.write(item+"\n")
