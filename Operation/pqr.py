from fastapi import FastAPI
app = FastAPI()
 
list_of_username = list()
 
@app.get("/home/{age}")
def home(age: int, query):
    return {
        "name": "subhankar",
        "age": age,
        "query": query
    }
 
 
@app.put("/username/{username}")
def put_data(username: str):
    list_of_username.append(username)
    return {
        "user_name": username
    }
 
@app.post("/postdata")
def post_data(username: str):
    list_of_username.append(username)
    return {
        "username": list_of_username
    }
 
@app.delete("/delete")
def delete_data(username: str):
    list_of_username.remove(username)
    return {
        "username": list_of_username
    }