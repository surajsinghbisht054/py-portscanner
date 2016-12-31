#!/usr/bin/python
# python Script For Scanning Open Tcp Port version 0.0.2
#
# =========================================================================|
#   This Script is Created Only for Practise And Educational Purpose Only
# =========================================================================|

__author__='''
######################################################
			By S.S.B Group							
######################################################

	Suraj Singh
	Admin
	S.S.B Group
	surajsinghbisht054@gmail.com
	https://hackworldwithssb.blogspot.in

	Note: We Feel Proud To Be Indian
######################################################

	High-Speed Tcp Port Scanner written in python
'''
# =================Other Configuration================ 
# Usages :
usage = "usage: %prog [options] "
# Version
Version="%prog 0.0.2"
# ====================================================

# Importing Modules
import socket,time,threading,optparse,sys

# Port Scanner Engine
class PortScanner:
	def __init__(self, target, port, thread, timeout, output):
		self.target=target
		self.starttime=time.time()
		self.port=port
		self.thread=thread
		self.timeout=timeout
		self.output=output
		self.store_open_ports=[]
		self.port.reverse()
		self.startthreading()

	def checkopenport(self):
		s=socket.socket()
		s.settimeout(float(self.timeout))
		socket.setdefaulttimeout(float(self.timeout))
		port=self.port.pop()
		storeobj=str(s.connect_ex((self.target, int(port))))
		if storeobj=="0":
			self.store_open_ports.append(port)
		s.close()
		return 
		
	def startthreading(self):
		listthread=[]
		for i in range(len(self.port)):
			storethread=threading.Thread(target=self.checkopenport)
			storethread.start()
			if int(threading.activeCount())==int(self.thread):
				printingline="\r<  Number of Threads : {} | Port Scanning : {} | Open Ports Founded {} >".format(str(threading.activeCount()),str(i),str(len(self.store_open_ports)))
				sys.stdout.write(printingline)
				sys.stdout.flush()
				time.sleep(float(self.timeout))
			listthread.append(storethread)
		for i in listthread:
			i.join()
		self.closetime=time.time()
		self.showoutput()
		return

	# Showing Output of Scanner
	def showoutput(self):
		print "\n\n",'*'*120,'\n'
		for i in self.store_open_ports:
			print "[+] Open Port Found : %s, \tUsed For\t" % (i),
			try:
				print socket.getservbyport(int(i))
			except:
				print "unknown"
				pass
		print "\n",'*'*120,'\n'
		print "[+] Total Open Ports Found ", len(self.store_open_ports)
		print "[+] Scan Started On ", time.ctime(self.starttime)
		print "[+] Scan Finished On", time.ctime(self.closetime)			
		print '[+] Total Time Taken ',
		print self.closetime-self.starttime, ' Seconds '
		print "\n",'*'*120,'\n'
		print "\n\n Thanks For Using My Program by SSB"
		if self.output:
			self.saveresult()
		return	

	def saveresult(self):
		data=open(self.output,'a')
		for i in self.store_open_ports:
			line="{}\t\t\t{}\n".format(self.target, i)
			data.write(line)
		data.close()
		return


# Port Numbers Extractor
def port_extraction(port):
	storeport=[]
	# Verifiying Port Value
	if port:
		# Verifying Port is in Range
		if "-" in port and "," not in port:
			x1,x2=port.split('-')
			storeport=range(int(x1),int(x2))
		# Verifying Port is in Commas
		elif "," in port and "-" not in port:
			storeport=port.split(',')
		elif "," in port and "-" in port:
			x2=[]
			for i in port.split(','):
				if '-' in i:
					y1,y2=i.split('-')
					x2=x2+range(int(y1),int(y2))
				else:
					x2.append(i)
			storeport=x2
		else:
			storeport.append(port)
	else:
		print "[*] Please Provide Ports For Scanning."
		exit(0)
	return storeport

# Checking About User Input Data is IP Or Host
def valid_ip(ip):
	" Verifying IP Address "
	try:
		socket.inet_aton(ip)
	except socket.error:
		ip=socket.gethostbyname(ip)
	return ip

def main():
	print __author__
	parser=optparse.OptionParser(usage=usage,version=Version)
	parser.add_option('-t','--target',type='string',dest='target',help="Specify Target For Scan", default=None)
	parser.add_option("-p","--port",type='string', dest="port", help="Specify Target Ports Seperated by commas or Provide Range of Ports. eg. 80-1200", default=None)
	parser.add_option('-n',"--thread",type='string', dest="thread", help="Specify Number of Thread For Scanning ", default='500')
	parser.add_option('-o',"--output",type='string', dest="output", help="Specify Path For Saving Output in Txt.", default=None)
	parser.add_option('-T','--timeout',type='string', dest="timeout", help="Specify Port Time Out Seconds ",default='2')
	(options, args)= parser.parse_args()

	# Conditions
	if not options.target:
		print "[*] Please Specify Target. e.g: 192.168.10.1 or www.site.org"
		exit(0)
	if options.target:
		target=valid_ip(options.target)
	port=port_extraction(options.port)
	thread=options.thread
	output=options.output
	timeout=options.timeout
	print "[+] Scanning IP Address ", target
	PortScanner(target, port, thread, timeout, output)











# Trigger 
if __name__ == '__main__':
	main()