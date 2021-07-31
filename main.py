"""
The user types the username and password in the frontend, and hits Enter.
The frontend sends that username and password to tokenUrl="token" ie., https://example.com/token
The API checks that username and password, and responds with a "token"
Normally, a token is set to expire after some time.
The frontend stores that token temporarily somewhere.
The user clicks in the frontend to go to another section of the frontend web app.
So, to authenticate with our API, it sends a header Authorization with a value of Bearer plus the token.
If the token contains foobar, the content of the Authorization header would be: Bearer foobar.


"""

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

class User(BaseModel):
    username: str
    hashed_password: str
    disabled:bool

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") #https://example.com/ >  https://example.com/token

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm=Depends()):
    usn=form_data.username
    if usn not in db:
        raise HTTPException(status_code=400, detail="Invalid authentication credentials")
    user=User(**db[usn])
    if user.disabled:
        raise HTTPException(status_code=400, detail="Invalid user")
    if "hashed"+form_data.password!= db[usn]["hashed_password"]:
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {"access_token": usn, "token_type": "bearer"}

@app.get("/resource1")
async def endpoint1(current_user: User = Depends(oauth2_scheme)): return "reached resource1"

if __name__ == "__main__":uvicorn.run(app, host="0.0.0.0", port=9000)