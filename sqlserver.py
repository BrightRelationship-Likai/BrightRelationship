from SimpleXMLRPCServer import SimpleXMLRPCServer
import os   
def chpassword(x):
    os.system("echo \"changing password\"")
	os.system("service mysql stop")
	os.system("mysqld --skip-grant-tables")
	os.system("mysql -uroot -e \"use mysql;update user set password=password(x) where user="root";flush privileges;\"")
	os.system("service mysql start")
def restart():
	os.system("service mysql restart")
def chport(x):
	os.system("service mysql stop")
	os.system("source ./iniset.sh")
	os.system("iniset -sudo /etc/my.cnf mysqld port x")
	os.system("service mysql start")
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('127.0.0.1', 8686))
    sqlRpc.register_function(chpassword)
	sqlRpc.register_function(restart)
	sqlRpc.register_function(chport)
    sqlRpc.serve_forever()
