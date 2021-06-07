import smtplib
import logging
import termcolor
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class E:

    def __init__(self, te):
        self.z = te

    def se(self):
        logging.basicConfig(filename='./logs/app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.basicConfig(filename='./logs/app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.WARNING)

# user_input() username_api
# user_input() password_api
# user_input() msg_subject
# user_input() msg_from
# user_input() msg_to

        m_s = raw_input('> smtp server service  : ')
        m_p = raw_input('> smtp port service    : ')
        a_u = raw_input('> username smtp account: ')
        a_p = raw_input('> password smtp account: ')
        s_e = raw_input('> spoofed email sender : ')
        s_s = raw_input('> message subject      : ')
        s_m = raw_input('> message to be sent   : ')
        m = MIMEMultipart('mixed')

        m['Subject'] = s_s
        m['From'] = s_e
        m['To'] = self.z

        pm = MIMEText(s_m, 'plain')
        hm = MIMEText(s_m, 'html')
        m.attach(pm)
        m.attach(hm)

        ms = smtplib.SMTP(m_s, m_p)
        ms.ehlo()
        m.starttls()
        m.ehlo()
        m.login(a_u, a_p)
        m.sendmail(s_e, self.z, m.string())
        m.close()
