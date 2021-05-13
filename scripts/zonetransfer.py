import requests
import logging

class Z:

	def __init__ (self, td):
		self.z = td
		logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s %(message)s', encoding='utf-8', level=logging.DEBUG)
		
	def gr_zon(self):
		r = requests.get('https://api.hackertarget.com/zonetransfer/?q=%s' % (self.z))
		if r.status_code == 200:
			logging.info('[+] zonetransfer data server request successfully\n%s' % (r.text))
			return '[+] zonestransfer data server request successfully'
		else:
			logging.warning('[-] zonetransfer data server request unsuccessfully')
			return '[+] zonetransfer data server request successfully'