from eth_keys import keys
from eth_utils import keccak
import os
import jwt
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
import binascii
import base64
import json
class RegistrySC:
        
    def __init__(self):
        private_key_bytes = os.urandom(32)
        self.private_key = keys.PrivateKey(private_key_bytes)
        self.public_key = self.private_key.public_key
        self.eth_address = self.public_key.to_checksum_address()
        self.registry = {}

    
    def __str__(self):
        return "Private Key: "+ str(self.private_key) + "\nPublic Key: " + str(self.public_key) + "\nEthereum Address: " + str(self.eth_address)
    
    def register_attestation(self, user_eth_address, user_public_key):
        """
        Register the user's public key and Ethereum address in the registry.
        """
        self.registry[user_eth_address] = user_public_key
        print(f"User {user_eth_address} registered successfully.")

    def b64url_encode(self,data: bytes) -> str:
        return base64.urlsafe_b64encode(data).decode('utf-8').rstrip('=')

    def generate_jwt(self, payload):
        header = {
            "alg": "ES256",
            "typ": "JWT"
        }

        header_b64 = self.b64url_encode(json.dumps(header).encode('utf-8'))
        payload_b64 = self.b64url_encode(json.dumps(payload).encode('utf-8'))
        payload['iat'] = datetime.now()

        message = f"{header_b64}.{payload_b64}".encode()

        msg_hash = keccak(message)
        signature = self.private_key.sign_msg_hash(msg_hash)

        jwt_signature = signature.r.to_bytes(32, 'big') + signature.s.to_bytes(32, 'big')
        signature_b64 = self.b64url_encode(jwt_signature)

        jwt = f"{header_b64}.{payload_b64}.{signature_b64}"
        return jwt

