import requests
import logging

class S:

	def __init__(self, td):
		self.z = td
		logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s %(message)s', encoding='utf-8', level=logging.DEBUG)
		
	def gr_hos(self):
		r = requests.get('https://api.hackertarget.com/hostsearch/?q=%s' % (self.z))
		if r.status_code == 200:
			logging.info('[+] hostsearch data server request successfully\n%s' % (r.text))
			return '[+] hostsearch data server request successfully'
		else:
			logging.warning('[-] hostsearch data server request unsuccessfully')
			return '[+] hostsearch data server request successfully'
