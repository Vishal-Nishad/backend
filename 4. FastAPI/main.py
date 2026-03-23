from fastapi import FastAPI
from models import Product

app = FastAPI()



@app.get('/')
def greet():
    # print("Hello this is visha")
    st = {"greet":"hello this is vishal"}
    return st

products = [
    Product(1,"phone", "budget phone", 99, 10),
    Product(2,"laptop", "budget laptop", 500, 40),
]

print(products[0].__dict__)

print(products)

@app.get("/products")
def get_all_products():
    return products

print(get_all_products())

print(greet())