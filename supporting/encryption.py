#  MIT License
#
#  Copyright (c) 2019 Jac. Beekers
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

#
# pip install pycryptodome
import base64
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto import Random
import os
import uuid
from cryptography.fernet import Fernet

def decrypt(key, source, decode=True):
    if decode:
        source = base64.b64decode(source.encode("utf-8"))
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    iv = source[:AES.block_size]  # extract the iv from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    data = decryptor.decrypt(source[AES.block_size:])  # decrypt
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding


class Encryption():
    private_filename = "tmp_private"
    public_filename = "tmp_public"
    encrypted_session_key = ''
    nonce = ''
    tag = ''

    def encrypt_with_certificates(self, data, key_instance, encrypted_file):
        key = RSA.generate(2048)
        private_key = key.export_key()
        current_private_filename = Encryption.private_filename + str(key_instance) + ".tmp"
        file_out = open(current_private_filename, "wb")
        file_out.write(private_key)
        file_out.close()

        public_key = key.publickey().export_key()
        
        current_public_filename = Encryption.public_filename + str(key_instance) + ".tmp"
        file_out = open(current_public_filename, "wb")
        file_out.write(public_key)
        file_out.close()

        recipient_key = RSA.import_key(open(current_public_filename).read())
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        self.encrypted_session_key = cipher_rsa.encrypt(session_key)

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        self.nonce = cipher_aes.nonce
        encrypted_data, self.tag = cipher_aes.encrypt_and_digest(data.encode('utf-8'))

        file_out = open(encrypted_file, "wb")
        [ file_out.write(x) for x in (self.encrypted_session_key, self.nonce, self.tag, encrypted_data) ]

        file_out.close()
        return encrypted_data

    def decrypt_with_certificates(self, key_instance, encrypted_file):
        
        current_private_filename = Encryption.private_filename + str(key_instance) + ".tmp"
        private_key = RSA.import_key(open(current_private_filename).read())
        file_in = open(encrypted_file, "rb")
        encrypted_session_key, nonce, tag, encrypted_data = \
           [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(encrypted_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(encrypted_data, tag)
        file_in.close()
        return data.decode('utf-8')

    def cleanup(self, key_instance):
        os.remove(Encryption.private_filename + str(key_instance) + ".tmp")
        os.remove(Encryption.public_filename + str(key_instance) + ".tmp")

    def get_key(self) -> bytes:
        key = Fernet.generate_key()  # store in a secure location
        return key.decode()

    def encrypt(self, message, key: bytes) -> bytes:
        return Fernet(key).encrypt(message.encode('utf-8'))

    def decrypt(self, token, key: bytes) -> bytes:
        return Fernet(key).decrypt(token).decode('utf-8')


def verify():
    encryption = Encryption()
    data = 'Hello encrypted world!'
    encrypted_data_filename = "verify.enc.tmp"
    key_instance = 1
    encrypted = encryption.encrypt_with_certificates(data, key_instance, encrypted_data_filename)
    decrypted = encryption.decrypt_with_certificates(key_instance, encrypted_data_filename)
    print(decrypted)
    os.remove(encrypted_data_filename)
    encryption.cleanup(key_instance)


#main()
