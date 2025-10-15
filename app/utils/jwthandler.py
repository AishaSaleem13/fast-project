from datetime import timedelta,datetime
from jose import jwt
from ..core.config import settingstructure

def tokengenreate(data:dict):
    to_encode_in_jwt=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=settingstructure.Expiry_token)
    to_encode_in_jwt.update({"exp":expire})
    enocdejwt=jwt.encode(to_encode_in_jwt,settingstructure.Secret_key,settingstructure.Alogorithm)
    return enocdejwt