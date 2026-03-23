from fastapi import FastAPI

app = FastAPI()



@app.get('/')
def greet():
    # print("Hello this is visha")
    st = {"greet":"hello this is vishal"}
    return st

@app.get("/products")
def get_all_products():
    return "All products"




print(greet())