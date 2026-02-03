import argparse
import sys
import random
import string
import os

MIN_ASCII = 32
MAX_ASCII = 126
RANGE = MAX_ASCII - MIN_ASCII + 1

def generate_key(length):
    chars = string.ascii_letters + string.digits + string.punctuation + " "
    return "".join(random.choice(chars) for _ in range(length))

def encrypt(plaintext, key=None):
    if key is None:
        key = generate_key(len(plaintext))
    
    if len(key) != len(plaintext):
        raise ValueError("Key length must equal plaintext length for dynamic cipher.")

    ciphertext = []
    for i, char in enumerate(plaintext):
        if not (MIN_ASCII <= ord(char) <= MAX_ASCII):
            ciphertext.append(char)
            continue
            
        p_val = ord(char) - MIN_ASCII
        k_val = ord(key[i]) - MIN_ASCII
        
        c_val = (p_val + k_val) % RANGE
        ciphertext.append(chr(c_val + MIN_ASCII))
    
    return "".join(ciphertext), key

def decrypt(ciphertext, key):
    if len(key) != len(ciphertext):
        raise ValueError("Key length must equal ciphertext length.")

    plaintext = []
    for i, char in enumerate(ciphertext):
        if not (MIN_ASCII <= ord(char) <= MAX_ASCII):
            plaintext.append(char)
            continue
            
        c_val = ord(char) - MIN_ASCII
        k_val = ord(key[i]) - MIN_ASCII
        
        p_val = (c_val - k_val) % RANGE
        plaintext.append(chr(p_val + MIN_ASCII))
    return "".join(plaintext)

def main():
    parser = argparse.ArgumentParser(description="Encrypt/Decrypt using a Dynamic Key (One-Time Pad style).")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform.")
    parser.add_argument("--message", "-m", help="Message to process.")
    parser.add_argument("--file", "-f", help="File containing the message.")
    parser.add_argument("--key", "-k", help="Key for decryption (or manual key for encryption).")
    parser.add_argument("--key-out", "-ko", help="File to save the generated key (for encryption).")
    
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
        try:
            provided_key = args.key
            if provided_key and len(provided_key) != len(content):
                 print(f"Warning: Provided key length ({len(provided_key)}) does not match message length ({len(content)}). Ignoring provided key and generating new one.")
                 provided_key = None
            
            result, key_used = encrypt(content, provided_key)
            print(f"Computed Ciphertext:\n{result}")
            print(f"Key used:\n{key_used}")
            
            if args.key_out:
                with open(args.key_out, "w") as f:
                    f.write(key_used)
                print(f"Key saved to {args.key_out}")
                
        except ValueError as e:
            print(f"Error: {e}")
            
    else: # decrypt
        if not args.key:
            print("Error: --key is required for decryption.")
            sys.exit(1)
            
        try:
            result = decrypt(content, args.key)
            print("Plaintext:")
            print(result)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
