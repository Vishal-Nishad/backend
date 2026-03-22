from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def greet():
    print("Hello this is visha")
    return "he"
greet()
print(greet())