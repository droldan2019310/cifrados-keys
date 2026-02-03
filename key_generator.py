#!/usr/bin/env python3
import random
import string
import argparse

def generate_key(length):
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    chars = string.ascii_letters + string.digits + string.punctuation + " "
    return "".join(random.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Generate a generic ASCII key.")
    parser.add_argument("length", type=int, help="Length of the key to generate.")
    parser.add_argument("--output", "-o", help="File to write the key to.")
    
    args = parser.parse_args()
    
    try:
        key = generate_key(args.length)
        if args.output:
            with open(args.output, "w") as f:
                f.write(key)
            print(f"Key of length {args.length} written to {args.output}")
        else:
            print(f"Generated Key: {key}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
