#!/usr/bin/python

import ssl
import sys
from functions import base64checker

cert=ssl.get_server_certificate((sys.argv[1],443))
a=open("cert.pem","w")
a.write(cert)
a.close()
cert_dict=ssl._ssl._test_decode_cert("cert.pem")
print "There are "+str(len(cert_dict))+" fields in the cert"
#print cert_dict
for k in cert_dict.keys():
        #print type(cert_dict[k])
        if (type(cert_dict[k]) == tuple):
                print k
                print "\tThere are "+str(len(cert_dict[k]))+" subfields in this key"
                for i in range(0,len(cert_dict[k])):
                        print "\t\t"+str(cert_dict[k][i])
                        #print str(cert_dict[k][i][0])
                        #a=base64checker(str(cert_dict[k][i][1]))
                        #if (a==True):
                        #       print "\t\t\tBase64 detected!"
        else:
                print k+" "+str(cert_dict[k])
        print ""
