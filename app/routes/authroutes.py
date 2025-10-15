from ..utils import hash_password
from ..schemas.userSchema import Login,Register
from ..models.userSchema_model import collectionfieldname
from ..utils.jwthandler import tokengenreate
from ..utils.hash_password import hashingpassword,checking
from fastapi import HTTPException,APIRouter,status

router =APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register")
async def signup(user:Register):
 existing_user= await collectionfieldname.find_one({"email":user.email})
 if existing_user:
  return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="email already exist")
 
 hashpassword=hashingpassword(user.password)
 new_user={"name":user.name,"email":user.email,"password":hashpassword}
 result=await collectionfieldname.insert_one(new_user)
 return {"message": "User registered successfully","userid":str(result.inserted_id)}

@router.post("/Login")
async def login(user:Login):
 db_user=await collectionfieldname.find_one({"email":user.email})
 if not db_user or not checking(user.password,db_user["password"]):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
 token=tokengenreate({"userid":str(db_user["id"]),"email":db_user["email"]})
 return {"generatedtoken":token,"token-type":"bearer"}