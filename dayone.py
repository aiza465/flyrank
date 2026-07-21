from fastapi import FastAPI
app = FastAPI(title="FlyRank")

@app.get("/")
def welcome_msg():
    return {'message': 'Welcome to FlyRank'}

@app.post("/users/{user_id}")
def enter_user(user_id:int):
    return {'user': user_id}