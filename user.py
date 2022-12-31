import os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64
import base58
import codecs
import hashlib


class User():

    def __init__(self, dir=None):
        if dir!= None:
            self.private_key = RSA.import_key(open(dir + '_priv.pem', 'r').read())
            self.public_key = RSA.import_key(open(dir + '_pub.pem', 'r').read())
        else:
            self.private_key = RSA.generate(1024)
            self.public_key = self.private_key.publickey()

        self.e_cipher = PKCS1_OAEP.new(key=self.public_key)
        self.d_cipher = PKCS1_OAEP.new(key=self.private_key)

    def writeKeysToFiles(self, privKeyFile, pubKeyFile):
        _private_pem = self.private_key.export_key().decode()
        _public_pem = self.public_key.export_key().decode()
        with open(privKeyFile, 'w') as _priv_key:
            _priv_key.write(_private_pem)
        with open(pubKeyFile, 'w') as _pub_key:
            _pub_key.write(_public_pem)

    def writeKeysToFiles(self, filePrefix):
        _private_pem = self.private_key.export_key().decode()
        _public_pem = self.public_key.export_key().decode()
        print(filePrefix)
        with open(filePrefix + "_priv.pem", 'w+') as _priv_key:
            _priv_key.write(_private_pem)
        with open(filePrefix + "_pub.pem", 'w+') as _pub_key:
            _pub_key.write(_public_pem)

    def readKeysFromFiles(self, privKeyFile, pubKeyFile):
        self.private_key = RSA.import_key(open(privKeyFile, 'r').read())
        self.public_key = RSA.import_key(open(pubKeyFile, 'r').read())

    def sign(self, message_bytes):
        sha = hashlib.sha256()
        sha.update(message_bytes)
        return self.encryptHex(str.encode(sha.hexdigest()))

    def verify(self, message_bytes, signature):
        sha = hashlib.sha256()
        sha.update(message_bytes)
        _msgDigest = sha.hexdigest()
        _signDigest = self.decryptHex(signature).decode()
        if _msgDigest == _signDigest:
            return True
        return False

    def encrypt(self, message):
        return self.e_cipher.encrypt(message)

    def decrypt(self, cipher_text):
        return self.d_cipher.decrypt(cipher_text)

    def encryptBase64(self, message):
        return base64.b64encode(self.encrypt(message))

    def decryptBase64(self, cipher_text_base64):
        return self.decrypt(base64.b64decode(cipher_text_base64))

    def encryptHex(self, message):
        return self.encrypt(message).hex()

    def decryptHex(self, cipher_text_hex):
        return self.decrypt(bytes.fromhex(cipher_text_hex))

    def encryptLatin1(self, message):
        return codecs.decode(self.encrypt(message), 'latin1')

    def decryptLatin1(self, cipher_text_latin1):
        return self.decrypt(cipher_text_latin1.encode('latin1'))

    def printKeysType(self):
        print(type(self.private_key), type(self.public_key))

    def printKeys(self):
        self.printKeysPEM()

    def pubKeyPEM(self):
        return self.public_key.export_key().decode()

    def privKeyPEM(self):
        return self.private_key.export_key().decode()

    def printKeysPEM(self):
        print(self.privKeyPEM())
        print(self.pubKeyPEM())

    def pubKeyAsAddress(self):
        sha = hashlib.sha256()
        sha.update(self.pubKeyPEM().encode())
        return base58.b58encode(sha.hexdigest())


def main():
    for i in range(50):
        user = User()
        address = user.pubKeyAsAddress()
        path = 'users/{}'.format(address.decode())
        if not os.path.exists(path):
            os.makedirs(path)
        user.writeKeysToFiles('users/{}/'.format(address.decode()))


if __name__ == "__main__":
    main()