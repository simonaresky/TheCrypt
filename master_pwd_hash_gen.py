from hashlib import sha256
import hashlib
import master_pwd_check

def master_pwd_hash_gen():

    master_password = input("Enter your password: ")
    password = master_pwd_check.strong_check(master_password)
    valid_master_password = password.encode()
    
    compile_factor_together = hashlib.sha256(valid_master_password).hexdigest()

    print("Master Password: " + str(compile_factor_together))

master_pwd_hash_gen()
