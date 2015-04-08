# SSHAttackFinder
A simple Python script that scans the logfile for attackers failing passwords on your system.

# Installation
Simply grab the file from here, place it in a  directory of your choosing, and execute in Python 3!

# Example Setups
The script automatically saves the "IPs" file to the current working directory (os.cwd()), however why not edit this line, and make the script output to your website's directory? Add the script to a cronjob, and you have a dynamically updating list of possible attackers!

Example line: IPsf = open("/var/www/site/IPs", "w+")                                                                    
Example Cron Line (crontab -e): 0 0 * * * python3 /home/foobar/SSHAttackFinder.py
However the person running this file must have access to the directory!

This script only runs on Linux. It may not work out-of-the-box on some distros, that don't use /var/log/auth.log, however change the "auth" line to the applicable logfile, and it should run.                                                  
<href="toma678.com/IPs"Here's> a realtime list (updated daily) of the attackers hitting my server.
