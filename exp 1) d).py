from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Original data
plain_text = b"Rajalakshmi Engineering College."

# Encrypt data
cipher_text = cipher_suite.encrypt(plain_text)

# Decrypt data
decrypted_text = cipher_suite.decrypt(cipher_text)

# Display results
print("Original Data:", plain_text)
print("Encrypted Data:", cipher_text)
print("Decrypted Data:", decrypted_text)