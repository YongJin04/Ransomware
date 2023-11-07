from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import subprocess
import sys

# function: create RSA key 
def create_rsa_keys():
    key = RSA.generate(2048)  # create RSA-2048 bit key
    private_key = key.export_key()  # extract private key
    public_key = key.publickey().export_key()  # extract public key 
    return private_key, public_key  # return

# function: encrypt data with public key
def encrypt_data_with_rsa(public_key, data):
    rsa_key = RSA.import_key(public_key)  # import public key
    rsa_cipher = PKCS1_OAEP.new(rsa_key)  # create PKCS1_OAEP object
    encrypted_data = rsa_cipher.encrypt(data)  # encrypt data
    return encrypted_data  # return

# main
if __name__ == '__main__':
    private_key, public_key = create_rsa_keys()  # function call

    hex_key = sys.argv[1]  # data type of argument: hex sring
    data_to_encrypt = bytes.fromhex(hex_key)  # type conversion: hex string to Byte type
    encrypted_data = encrypt_data_with_rsa(public_key, data_to_encrypt)  # function call

    encrypted_data_hex_string = encrypted_data.hex()  # type conversion: Byte type to hex string (use "subprocess")

    subprocess.run(['python3', 'chatBot.py', encrypted_data_hex_string])  # call script "chatBot.py"

    # print private key after decoding string
    print("Private Key:")
    print(private_key.decode())

    # print public key after decoding string
    print("\nPublic Key:")
    print(public_key.decode())
