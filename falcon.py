class C:

    def gr0(x): h = header.H(x); return h.gr()
    def gr1(x): l = link.L(x); return l.gr()
    def gr2(x): i = ip.I(x); return i.gr_geo()
    def gr3(x): r = reverselookup.R(x); return r.gr_rev()
    def gr4(x): n = nmap.N(x); return n.gr_nma()
    def gr5(x): v = reversedns.V(x); return v.gr_rev()
    def gr6(x): s = hostsearch.S(x); return s.gr_hos()
    def gr7(x): w = whois.W(x); return w.gr_who()
    def gr8(x): z = zonetransfer.Z(x); return z.gr_zon()
    def gr9(x): m = malware.M(x); return m.gr_vir()



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
    import argparse

    try:
        parse = argparse.ArgumentParser()
        parse.add_argument('-hr','--header', help='collecting header request informations')
        parse.add_argument('-lk','--link', help='scraping links within the webpage')
        parse.add_argument('-i','--ip', help='getting geolocation informations')
        parse.add_argument('-rp','--reverselookup', help='getting reverse lookup informations')
        parse.add_argument('-np','--nmap', help='collecting nmap port scan result')
        parse.add_argument('-rs','--reversedns', help='getting reverse dns informations')
        parse.add_argument('-hs','--hostsearch', help='Checking for some host name search results')
        parse.add_argument('-w','--whois', help='whois informations lookup result')
        parse.add_argument('-z','--zonetransfer', help='getting zonetransfer information results')
        parse.add_argument('-m', '--malware', help='malware scanning the specified domain target')
        args = parse.parse_args()

        try:
            if args.header: C.gr0(args.header)
            if args.link: C.gr1(args.link)
            if args.ip: C.gr2(args.ip)
            if args.reverselookup: C.gr3(args.reverselookup)
            if args.nmap: C.gr4(args.nmap)
            if args.reversedns: C.gr5(args.reversedns)
            if args.hostsearch: C.gr6(args.hostsearch)
            if args.whois: C.gr7(args.whois)
            if args.zonetransfer: C.gr8(args.zonetransfer)
            if args.malware: C.gr9(args.malware)

        except ConnectionError: print("\n\033[1;31m[!] server block temporary (too much request!)\033[0m\n\n") 

    except KeyboardInterrupt:
        exit(0)
