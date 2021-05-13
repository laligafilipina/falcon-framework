import requests
import logging

class V:

	def __init__(self, td):
		self.z = td
		logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s %(message)s', encoding='utf-8', level=logging.DEBUG)
		
	def gr_rev(self):
		r = requests.get('https://api.hackertarget.com/reversedns/?q=%s' % (self.z))
		if r.status_code == 200:
			logging.info('[+] reversedns data server request successfully\n%s' % (r.text))
			return '[+] reversedns data server request successfully'
		else:
			logging.warning('[-] reversedns data server request successfully')
			return '[-] reversedns data server request successfully'