
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()
db = {
    "test": {
        "username": "test",
        "hashed_password": "hashedpassword",
        "disabled": False,
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    hashed_password: str
    disabled:bool

async def validate_user(token: str = Depends(oauth2_scheme)):
    if token not in db:
        raise HTTPException(status_code=400, detail="Invalid authentication credentials")
    user=User(**db[token])
    if user.disabled:
        raise HTTPException(status_code=400, detail="Invalid user")
    return user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    usn=form_data.username
    validate_user(usn)
    if "hashed"+form_data.password!= db[usn]["hashed_password"]:
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {"access_token": usn, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(validate_user)):
    return current_user

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)