import requests
import logging

class N:
	
	def __init__(self, td):
		self.z = td
		logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s %(message)s', encoding='utf-8', level=logging.DEBUG)
		
	def gr_nma(self):
		r = requests.get('https://api.hackertarget.com/nmap/?q=%s' % (self.z))
		if r.status_code == 200:
			logging.info('[+] nmap data server request successfully\n%s' % (r.text))
			return '[+] nmap data server request successfully'
		else:
			logging.warning('[-] nmap data server request successfully')
			return '[-] nmap data server request successfully'
