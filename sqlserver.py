from SimpleXMLRPCServer import SimpleXMLRPCServer
import os   
def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("service mysqld stop")
    os.system("mysqld --skip-grant-tables")
    os.system("mysql -uroot -e \"use mysql;update user set password=password(%s) where user=\"root\";flush privileges;\"" % (x))
    os.system("service mysqld start")
def restart():
    os.system("service mysqld restart")
def chport(x):
    os.system("service mysqld stop")
    os.system("source /root/iniset.sh && iniset -sudo /etc/my.cnf mysqld port %s" % (x))
    os.system("service mysqld start")
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('0.0.0.0', 8686))
    sqlRpc.register_function(chpassword)
    sqlRpc.register_function(restart)
    sqlRpc.register_function(chport)
    sqlRpc.serve_forever()
