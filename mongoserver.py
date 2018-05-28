#!/usr/bin/python
# -- coding: utf-8 --
#5.7 password change to authentication_string
from pymongo import MongoClient
from SimpleXMLRPCServer import SimpleXMLRPCServer
import os   

def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("sed -i 's/auth\ =\ true/auth\ =\ false/g' /etc/mongodb.conf")
    os.system("service mongo restart")
    os.system("echo \"db.changeUserPassword('root','1234')\" > /opt/chsql/mongo.sh")
    os.system("mongo --shell /opt/chsql/mongo.sh &")
    os.system("ps -aux|grep mongo\ --shell\ mongo.sh|grep -v grep|awk '{printf $2}'|xargs kill -9")
    os.system("rm /opt/chsql/mongo.sh")
    os.system("sed -i 's/auth\ =\ false/auth\ =\ true/g' /etc/mongodb.conf")
    os.system("service mongo restart")
    return x
def restart():
    os.system("service mongo restart")
    return 0
def chport(x):
    os.system("service mongo stop")
    os.system("source /opt/chsql/iniset.sh && iniset -sudo /etc/my.cnf mysqld port %s" % (x))
    os.system("service mongo start")
    return x
def start():
    os.system("service mongo start")
    return 0
def stop():
    os.system("service mongo stop")
    return 0
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('0.0.0.0', 8686))
    sqlRpc.register_function(chpassword)
    sqlRpc.register_function(restart)
    sqlRpc.register_function(chport)
    sqlRpc.register_function(start)
    sqlRpc.register_function(stop)
    sqlRpc.serve_forever()

