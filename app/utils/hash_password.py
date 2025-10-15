from passlib.context import CryptContext

password_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hashingpassword(password:str) ->str:
    return hash(password)

def checking(plain_password:str,hashingpassword:str)->bool:
    return password_context.verify(plain_password,hashingpassword)
