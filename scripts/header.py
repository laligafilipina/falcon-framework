import requests
#import logging

class H:

	def __init__(self, td):
		self.z = td
		#logging.basicConfig(filename='./app.log', filemode='a', format='%(asctime)s - %(levelname)s %(message)s', encoding='utf-8', level=logging.DEBUG)
		
	def gr(self):
		r = requests.get('https://api.hackertarget.com/httpheaders/?q=%s' % (self.z))
		if r.status_code == 200:
			#logging.info('[+] header data requested successfully\n %s' % (r.text))
			return '\n\033[1;32m[+] header data requested successfully\033[0m\n\n%s' % (r.text)
		else:
			#logging.warning('[-] header data requested unsuccessfully')
			return '\n[-] header data requested unsuccessfully'

