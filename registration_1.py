from unisc import UniSC
from registrysc import RegistrySC
import os
from PIL import Image
import json


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    print("User Registration Process Simulation")
    print("=========================================")
    input("Press Enter to start the simulation...")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Step 0: Regulator has a smart contract deployed on the Ethereum network.")
    regulator = RegistrySC()
    print("Regulator Smart Contract: ")
    print(regulator)
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Step 1: User Deploys a smart contract.")
    user = UniSC()
    print("User Smart Contract: ")
    print(user)
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Step 2: User requests regulator to register them")
    print("To: ", regulator.eth_address, "(Regulator's Ethereum address)")
    print("From: ", user.eth_address, "(User's Ethereum address)")
    print("\nMessage: Certify me. Pretty please? :)")
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')


    print("Step 3: User has to verify their identity.")
    image = Image.open("SpongeBob27s_license.png")
    #Source:https://static.wikia.nocookie.net/spongebob/images/e/e4/SpongeBob%27s_driver%27s_license.png/revision/latest?cb=20220530065510 
    image.show()
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Step 4: Regulator is convinced and registers the user's UniID and public key to the registry smart contract.")
    regulator.register_attestation(user.eth_address, user.public_key)
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Step 5: User's UniID and attributes are collected to a JSON file.")
    user_json = user.jsonify()
    print(user_json)
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Step 6: Regulator provides user a JWT of their JSON file.")
    jwt = regulator.generate_jwt(json.loads(user_json))
    print(jwt)
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Step 7: User receives the JWT and stores it in their smart contract.")
    user.store_jwt(jwt)
    user.set_regulator_address(regulator.eth_address)
    print(user)
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')


    print("User Authentication Process Simulation")
    print("=========================================")
    input("Press Enter to start the simulation...")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Step 1: Verifier inspects the user's smart contract.")
    print("User Smart Contract: ")
    print(user)
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Step 2: Verifier checks JWT with Regulator's public address.")

    input("")

    os.system('cls' if os.name == 'nt' else 'clear')

    print("We're clear! :)")
    input("")

    

