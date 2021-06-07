import requests
import termcolor
import logging

class N:
    
    def __init__(self, td):
        self.z = td
        
    def gr_nma(self):
        logging.basicConfig(filename='./logs/app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.basicConfig(filename='./logs/app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.WARNING)
        r = requests.get('https://api.hackertarget.com/nmap/?q=%s' % (self.z))
        if r.status_code == 200:
            bnr = "Incoming Results from API Server"
            m = "Scanned ports information are found..."
            f = "Scanned ports information request failed..."
            a = termcolor.colored(bnr, color='green', attrs=['bold'])
            b = termcolor.colored(m, color='yellow', attrs=['bold'])
            c = termcolor.colored(r.text, color='blue', attrs=['bold'])
            d = termcolor.colored(f, color='red', attrs=['bold'])
            print('\u257E'*20,a,'\u257E'*20,'\n',b,'\n',c,'\n')
            logging.info('[+] Hackertarget API Port Scan Request Service Success')

        else:
            print('\u257E'*20,'\n','d','\n')
            logging.warning('[!] Hackertarget API Port Scan Request Service Failed')
