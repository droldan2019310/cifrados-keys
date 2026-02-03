import argparse
import sys

MIN_ASCII = 32
MAX_ASCII = 126
RANGE = MAX_ASCII - MIN_ASCII + 1

def encrypt(plaintext, key):
    ciphertext = []
    key_len = len(key)
    for i, char in enumerate(plaintext):
        if not (MIN_ASCII <= ord(char) <= MAX_ASCII):
            ciphertext.append(char)
            continue
            
        p_val = ord(char) - MIN_ASCII
        k_val = ord(key[i % key_len]) - MIN_ASCII
        
        c_val = (p_val + k_val) % RANGE
        ciphertext.append(chr(c_val + MIN_ASCII))
    return "".join(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    key_len = len(key)
    for i, char in enumerate(ciphertext):
        if not (MIN_ASCII <= ord(char) <= MAX_ASCII):
            plaintext.append(char)
            continue
            
        c_val = ord(char) - MIN_ASCII
        k_val = ord(key[i % key_len]) - MIN_ASCII
        
        p_val = (c_val - k_val) % RANGE
        plaintext.append(chr(p_val + MIN_ASCII))
    return "".join(plaintext)

def main():
    parser = argparse.ArgumentParser(description="Encrypt/Decrypt using a Fixed Key (Vigenère-style on ASCII).")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform.")
    parser.add_argument("--message", "-m", help="Message to process (string).")
    parser.add_argument("--file", "-f", help="File containing the message.")
    parser.add_argument("--key", "-k", required=True, help="Fixed key string.")
    
    args = parser.parse_args()
    
    content = ""
    if args.message:
        content = args.message
    elif args.file:
        try:
            with open(args.file, "r") as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: File {args.file} not found.")
            sys.exit(1)
    else:
        print("Error: Must provide --message or --file.")
        sys.exit(1)
        
    if args.action == "encrypt":
        result = encrypt(content, args.key)
        print("Ciphertext:")
        print(result)
    else:
        result = decrypt(content, args.key)
        print("Plaintext:")
        print(result)

if __name__ == "__main__":
    main()
