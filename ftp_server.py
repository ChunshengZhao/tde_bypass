from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# ʵ����DummyAuthorizer������ftp�û�
authorizer = DummyAuthorizer()

# �������û��������룬Ŀ¼��Ȩ��
#authorizer.add_user('user', '0123456789', './', perm='elradfmwMT')

# ������¼
authorizer.add_anonymous('./', perm='elradfmwMT')
handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "Good Luck!"

# ������IP���˿ڣ�handler
server = FTPServer(('127.0.0.1', 21), handler)
server.serve_forever()


