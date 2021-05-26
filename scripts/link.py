import requests
import logging

class L:

	def __init__(self, td):
		self.z = td
		#logging.basicConfig(filename='app.log', format='%(asctime)s - %(levelname)s %(message)s', encoding='utf-8', level=logging.DEBUG)
		
	def gr(self):
		r = requests.get('https://api.hackertarget.com/pagelinks/?q=%s' % (self.z))
		if r.status_code == 200:
			#logging.info('[+] link data scraped successfully\n%s' % (r.text))
			return '\n\033[1;32m[+] link data scraped successfully\033[0m\n\n%s' % (r.text)
		else:
			#logging.warning('[-] link data scraped unsuccessfully')
			return '\n[-] link data scraped unsuccessfully'
