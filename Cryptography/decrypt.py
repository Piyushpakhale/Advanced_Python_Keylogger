from cryptography.fernet import Fernet

key = '_YGuvGMyXy44cTykgbdJ4zcRgSA0f7n1VtjyKkpxEQo=='

key_info_e = "keylogs.txt"
com_info_e = 'computer.txt'
clip_info_e = 'clipboard.txt'

encrypted_file = [key_info_e,clip_info_e,com_info_e]
count =0

for decrypting_file in encrypted_file:
    with open(encrypted_file[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_file[count], 'wb') as f:
        f.write(decrypted)
    count += 1


