import requests
import termcolor

class I:

    def __init__(self, td):
        self.z = td

    def gr_geo(self):
        r = requests.get('https://api.hackertarget.com/geoip/?q=%s' % (self.z))
        if r.status_code == 200:
            m = "Geoip location  information are found..."
            f = "Geoip location  information request failed..."
            b = termcolor.colored(m, color='yellow', attrs=['bold'])
            c = termcolor.colored(r.text, color='blue', attrs=['bold'])
            d = termcolor.colored(f, color='red', attrs=['bold'])
            print('\u257E'*20,'\n',b,'\n',c,'\n')

        else:
             print('\u257E'*20,'\n','d','\n')
