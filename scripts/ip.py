import requests
#import logging

class I:

	def __init__(self, td):
		self.z = td
		#logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s %(message)s', encoding='utf-8', level=logging.DEBUG)

	def gr_geo(self):
		r = requests.get('https://api.hackertarget.com/geoip/?q=%s' % (self.z))
		if r.status_code == 200:
			#logging.info('[+] geographic data server request successfully\n%s' % (r.text))
			return '\n\033[1;32m[+] geographic data server request successfully\033[0m\n\n%s' % (r.text)
		else:
			#logging.warning('[-] geographic data server request successfully')
			return '\n[-] geographic data server request successfully'
