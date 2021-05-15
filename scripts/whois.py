import requests
import logging

class W:

	def __init__(self, td):
		self.z = td
		logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s %(message)s', encoding='utf-8', level=logging.DEBUG)

	def gr_who(self):
		r = requests.get('https://api.hackertarget.com/whois/?q=%s' % (self.z))
		if r.status_code == 200:
			logging.info('[+] whois data server request successfully\n%s' % (r.text))
			return '[+] whois data server request successfully'
		else:
			logging.warning('[-] whois data server request unsuccessfully')
			return '[+] whois data server request successfully'