import requests
import termcolor

class N:
    
    def __init__(self, td):
        self.z = td
        
    def gr_nma(self):
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

        else:
            print('\u257E'*20,'\n','d','\n')
