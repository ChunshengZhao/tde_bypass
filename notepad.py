import argparse
import binascii
import sys
import os
from ftplib import FTP


def ftpconnect(host, username, password):
    ftp = FTP()
    #ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    print ftp.getwelcome()
    return ftp

def uploadfile(ftp, localpath, remotepath):
    bufsize = 1024*10
    #ftp.set_debuglevel(2)
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    fp.close()

def getArgs():
    parse=argparse.ArgumentParser()
    parse.add_argument('-e',type=str)
    parse.add_argument('-d',type=str)
    parse.add_argument('-a',type=str)
    parse.add_argument('-u',type=str)
    parse.add_argument('-p',type=str)
    args=parse.parse_args()
    return vars(args)

def ReadTemplFile(filename):
    with open(filename, 'rb') as ft:
        print 'The Decrypt File has bytes :'
        for i in range(1,6):
            print 'Hex: ', binascii.b2a_hex(ft.read(16))


args=getArgs()
#print args

if args['e'] is not None and args['d'] is None:
    ReadTemplFile(args['e'])
elif args['e'] is not None and args['p'] is not None:
    ftp = ftpconnect(args['a'], args['u'], args['p'])
    uploadfile(ftp, args['e'], args['d'])
else:
    print 'Argument Error.'



os.system("pause") 

