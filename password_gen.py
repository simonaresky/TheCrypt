import secrets
import string

def password_gen(password_length):

    characters = string.ascii_letters + string.digits + string.punctuation

    secure_password = ''.join(secrets.choice(characters) for i in range(password_length))

    print(secure_password)

    #return secure_password

password_gen(20)