from cryptography.fernet import Fernet
key=Fernet.generate_key()
cipher=Fernet(key)
with open(r"C:\Users\Hays\Downloads\ENCRYPTED.mp4", "rb") as f: data=f.read()
encrypted=cipher.encrypt(data)
with open(r"C:\Users\Hays\Downloads\ENCRYPTED.mp4", "wb") as f: f.write(encrypted)
print("File encrypted successfully")