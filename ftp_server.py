from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 实例化DummyAuthorizer来创建ftp用户
authorizer = DummyAuthorizer()

# 参数：用户名，密码，目录，权限
#authorizer.add_user('user', '0123456789', './', perm='elradfmwMT')

# 匿名登录
authorizer.add_anonymous('./', perm='elradfmwMT')
handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "Good Luck!"

# 参数：IP，端口，handler
server = FTPServer(('127.0.0.1', 21), handler)
server.serve_forever()


