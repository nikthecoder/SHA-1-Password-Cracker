import hashlib
import os

print(os.getcwd())

salts_list = open("known-salts.txt", "r").readlines()
password_db = open("top-10000-passwords.txt", "r").readlines()


def sha1_hash(password, salt=None):
  password = password.strip()
  if salt:
    salt = salt.strip()
    password += salt
  return hashlib.sha1(str(password).encode('utf-8')).hexdigest()


hashed_passwords = {
    sha1_hash(password): password.strip()
    for password in password_db
}
salted_hashes = {}
for salt in salts_list:
  for password in password_db:
    hashed_password = sha1_hash(password, salt)
    salted_hashes[hashed_password] = password.strip()
    hashed_salt = sha1_hash(salt, password)
    salted_hashes[hashed_salt] = password.strip()


def crack_sha1_hash(hashed_password, use_salts=False):
  hashed_passwords_dict = salted_hashes if use_salts else hashed_passwords
  password = hashed_passwords_dict.get(hashed_password)
  if not password:
    return "PASSWORD NOT IN DATABASE"

  return password


print(salted_hashes.get(""))
