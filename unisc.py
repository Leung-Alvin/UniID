from eth_keys import keys
from eth_utils import keccak
import json
import os

class UniSC:
        
    def __init__(self):
        private_key_bytes = os.urandom(32)
        self.private_key = keys.PrivateKey(private_key_bytes)
        self.public_key = self.private_key.public_key
        self.eth_address = self.public_key.to_checksum_address()
        self.name = "Spongebob Squarepants"
        self.age = 20
        self.organization = "Bikini Bottom"
        self.sex = "Male"
        self.jwt = None
        self.regulator_address = None

    
    def __str__(self):
        return "Private Key: "+ str(self.private_key) + "\nPublic Key: " + str(self.public_key) + "\nEthereum Address: " + str(self.eth_address) + "\nJWT: "+ str(self.jwt) + "\nRegulator Address: " + str(self.regulator_address)
    
    def jsonify(self):
        selected_attributes = {
            "public_key": self.public_key.to_hex(),
            "eth_address": self.eth_address,
            "name": self.name,
            "age": self.age,
            "organization": self.organization,
            "sex": self.sex
        }
        # Convert the selected attributes to JSON
        json_data = json.dumps(selected_attributes, indent=4)
        return json_data
    
    def store_jwt(self, jwt):
        self.jwt = jwt

    def set_regulator_address(self, address):
        self.regulator_address = address