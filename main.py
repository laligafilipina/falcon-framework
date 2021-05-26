class C:

    def __init__(self, td): self.z = td;
    def gr0(self): h = header.H(self.z); return h.gr()
    def gr1(self): l = link.L(self.z); return l.gr()
    def gr2(self): i = ip.I(self.z); return i.gr_geo()
    def gr3(self): r = reverselookup.R(self.z); return r.gr_rev()
    def gr4(self): n = nmap.N(self.z); return n.gr_nma()
    def gr5(self): v = reversedns.V(self.z); return v.gr_rev()
    def gr6(self): s = hostsearch.S(self.z); return s.gr_hos()
    def gr7(self): w = whois.W(self.z); return w.gr_who()
    def gr8(self): z = zonetransfer.Z(self.z); return z.gr_zon()
    def gr9(self): m = malware.M(self.z); return z.gr_vir()



if __name__ == '__main__':

    #from scripts import email
    #from scripts import fuzz
    from scripts import header
    from scripts import ip
    from scripts import link
    from scripts import malware
    #from scripts import ssl
    #from scripts import waf
    from scripts import reverselookup
    from scripts import reversedns
    from scripts import hostsearch
    from scripts import nmap
    from scripts import whois
    from scripts import zonetransfer

    try:
        #color:#B2F47D
        x = str(input('target domain: '))
        i = C(x)

        try:
            print(i.gr0()) 
            print(i.gr1())
            print(i.gr2())
            print(i.gr3())
            print(i.gr4())
            print(i.gr5())
            print(i.gr6())
            print(i.gr7())
            print(i.gr8())
            print(i.gr9())
        except ConnectionError: print("\n\033[1;31m[!] server block temporary (too much request!)\033[0m\n\n") 

    except KeyboardInterrupt:
        exit(0)
