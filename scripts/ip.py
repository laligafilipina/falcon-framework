import requests
import termcolor
import logging

class I:

    def __init__(self, td):
        self.z = td

    def gr_geo(self):
        logging.basicConfig(filename='./logs/app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.basicConfig(filename='./logs/app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.WARNING)
        r = requests.get('https://api.hackertarget.com/geoip/?q=%s' % (self.z))
        if r.status_code == 200:
            bnr = "Incoming Results from API Server"
            m = "Geoip location  information are found..."
            f = "Geoip location  information request failed..."
            a = termcolor.colored(bnr, color='green', attrs=['bold'])
            b = termcolor.colored(m, color='yellow', attrs=['bold'])
            c = termcolor.colored(r.text, color='blue', attrs=['bold'])
            d = termcolor.colored(f, color='red', attrs=['bold'])
            print('\u257E'*20,a,'\u257E'*20,'\n',b,'\n',c,'\n')
            logging.info('[+] Hackertarget API GeoIP Request Service Success')

        else:
             print('\u257E'*20,'\n','d','\n')
             logging.warning('[!] Hackertarget API GeoIP Request Service Failed')
