import hashlib

print(""" 

-------------------------------------------------------------------------
                                          ______
                   |    |       /\       /          |    |
                   |____|      /__\      |_____     |____|
                   |____|     /____\           \    |____|
                   |    |    /      \          /    |    |
                   |    |   /        \   _____/     |    |

--------------------------------------------------------------------------

Develope by JERSON GABISAY
Description: This tool is for security that convert your text into hash 
and hash to text that understand how the data integrity works within the 
network or system.
--------------------------------------------------------------------------
""")





def sha_encryption(data: str, algorithm: str):
    data_bytes = data.encode('utf-8')
    
    if algorithm == 'SHA-1':
        return hashlib.sha1(data_bytes).hexdigest()
    elif algorithm == 'SHA-224':
        return hashlib.sha224(data_bytes).hexdigest()
    elif algorithm == 'SHA-256':
        return hashlib.sha256(data_bytes).hexdigest()
    elif algorithm == 'SHA-384':
        return hashlib.sha384(data_bytes).hexdigest()
    elif algorithm == 'SHA-512':
        return hashlib.sha512(data_bytes).hexdigest()
    else:
        return None

def main():
    print("Select the SHA encryption algorithm:")
    print("1. SHA-1")
    print("2. SHA-224")
    print("3. SHA-256")
    print("4. SHA-384")
    print("5. SHA-512")
    
    choice = input("Enter the number of the algorithm: ").strip()
    
    algorithms = {
        '1': 'SHA-1',
        '2': 'SHA-224',
        '3': 'SHA-256',
        '4': 'SHA-384',
        '5': 'SHA-512'
    }
    
    algorithm = algorithms.get(choice)
    if not algorithm:
        print("Invalid choice!")
        return
    
    action = input("Type 'plaintext' to encrypt or 'hash' to decrypt: ").strip().lower()
    if action == 'plaintext':
        data = input("Enter the plaintext to encrypt: ").strip()
        encrypted_data = sha_encryption(data, algorithm)
        print(f"Encrypted data ({algorithm}): {encrypted_data}")
    elif action == 'hash':
        print("SHA algorithms are one-way functions and cannot be decrypted.")
    else:
        print("Invalid action!")

if __name__ == "__main__":
    main()
