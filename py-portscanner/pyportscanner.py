#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For http://bitforestinfo.blogspot.in
# This Script is Written By
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
# =================Other Configuration================ 
# Usages :
usage = "usage: %prog [options] "
# Version
Version="%prog 0.0.1"
# ====================================================
print __author__
# Importing Modules
import socket, optparse, threading


# Extracting User Inputs
parser=optparse.OptionParser(usage, version=Version)
parser.add_option("-p","--port", dest="port", help="Specify Target Ports\
	Seperated by commas or Provide Range of Ports. ")
parser.add_option("-H","--Host", dest="host", help=" Specify Target Host")
(options, args)= parser.parse_args()

# Check Host Target 
def check_host(ip):
        storeobj=[]
        for i in ip.split('.'):
                if i.isdigit():
                        pass
                else:
                        return None
	return True


# Checking Host Address Provided by User
if options.host.count('.')>=3 and check_host(options.host):
	host=options.host
elif '.' in options.host:
	try:
		host=socket.gethostbyname(options.host)
	except:
	        print "[*] Please Provide Target Host. Example: 192.168.1.1 \n or www.sitename.com"
        	exit(0)

else:
	print "[*] Please Provide Target Host"
	exit(0)

# Checking Port Address Provided By user
if options.port:
	if "-" in options.port and "," not in options.port:
		x1,x2=options.port.split('-')
		port=range(int(x1),int(x2))
	elif "," in options.port and "-" not in options.port:
		port=options.port.split(',')
	elif "," in options.port and "-" in options.port:
		x2=[]
		for i in options.port.split(','):
			if "-" in i:
				y1,y2=i.split('-')
				x2.append(range(int(y1),int(y2)))
			else:
				x2.append(i)
		port=x2
	else:
		port=[options.port]
else:
	print "[*] Please Provide Target Ports "
	exit(0)


def check(host, port):
	s=socket.socket()
	s.settimeout(1)
	socket.setdefaulttimeout(1)
	storeobj=str(s.connect_ex((host, int(port))))
	if storeobj=="0":
		return True
	else:
		return False

def portscan(i):
	if type(i)==type([]):
		for j in i:
			if check(host, j):
				print "[+]  -->> Open Port Found -->>  ", j
			else:
				print "[*] Close Port ",j
	else:
		if check(host, i):
			print "[+]  -->> Open Port Found -->>  ",i
		else:
			print '[*] Close Port ',i
threadlist=[]
for i in port:
	if type(i)==type([]):
		for ii in i:
			thread=threading.Thread(target=portscan(ii))
			thread.start()
			threadlist.append(thread)
	else:
		thread=threading.Thread(target=portscan(i))
		thread.start()
		threadlist.append(thread)

for i in threadlist:
	i.join()
