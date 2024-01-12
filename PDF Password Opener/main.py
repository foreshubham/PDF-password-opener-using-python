import pikepdf
from tqdm import tqdm
passwords = [line.strip() for line in open("Name you want after decrypting with the extension .txt")]
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open("Name of password protected pdf with extention", password=password) as pdf:
            print("\n[+] Password:",password)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue
