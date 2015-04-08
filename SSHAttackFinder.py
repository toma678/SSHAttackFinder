import re

auth = open("/var/log/auth.log","r").read() #Opens the logfile for reading
IPsf = open("/var/www/site/IPs", "w+") #Opens the file that holds the IPs for reading and writing
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
