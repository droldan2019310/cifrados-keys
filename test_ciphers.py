import unittest
import string
import os
import subprocess

import cipher_fixed_key
import cipher_dynamic_key
import key_generator

class TestCiphers(unittest.TestCase):

    def test_key_generator(self):
        length = 100
        key = key_generator.generate_key(length)
        self.assertEqual(len(key), length)
        for char in key:
            self.assertTrue(32 <= ord(char) <= 126)

    def test_fixed_key_logic(self):
        msg = "Hello World!"
        key = "Key"
        
        # Encrypt
        encrypted = cipher_fixed_key.encrypt(msg, key)
        self.assertNotEqual(msg, encrypted)
        
        # Decrypt
        decrypted = cipher_fixed_key.decrypt(encrypted, key)
        self.assertEqual(msg, decrypted)

    def test_fixed_key_logic_long_key(self):
        msg = "Short"
        key = "LongKeyIsHere"
        encrypted = cipher_fixed_key.encrypt(msg, key)
        decrypted = cipher_fixed_key.decrypt(encrypted, key)
        self.assertEqual(msg, decrypted)

    def test_dynamic_key_logic(self):
        msg = "Secret Message"
        
        encrypted, key = cipher_dynamic_key.encrypt(msg)
        self.assertEqual(len(key), len(msg))
        self.assertNotEqual(msg, encrypted)
        
        decrypted = cipher_dynamic_key.decrypt(encrypted, key)
        self.assertEqual(msg, decrypted)

    def test_dynamic_key_manual(self):
        msg = "Test"
        key = "1234"
        encrypted, used_key = cipher_dynamic_key.encrypt(msg, key)
        self.assertEqual(key, used_key)
        
        decrypted = cipher_dynamic_key.decrypt(encrypted, key)
        self.assertEqual(msg, decrypted)

if __name__ == '__main__':
    unittest.main()
