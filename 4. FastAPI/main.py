from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)


@app.get('/')
def greet():
    # print("Hello this is visha")
    st = {"greet":"hello this is vishal"}
    return st

# products = [
#     Product(1,"phone", "budget phone", 99, 10),
#     Product(2,"laptop", "budget laptop", 500, 40),
# ]

products = [
    Product(id= 1, name= "phone", description= "budget phone", price= 99, quantity= 10),
    Product(id= 2, name= "laptop", description= "budget laptop", price= 999, quantity= 20),
    Product(id= 3, name= "cpu", description= "intel cpu", price= 15, quantity= 24),
    Product(id= 4, name= "gpu", description= "nvidia gpu", price= 50, quantity= 45),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    for p in products:
        db.add(database_models.Product(**p.model_dump()))
    db.commit()

# print(products[0].__dict__)
# print(products[1])  # as it is object of class Product which 
# is inherited from Pydantic basemodel, so it automatically
# print(str()) show in below example, overridding repr()

print(str(products[1]))
print(repr(products[1]))

print()

# print(products)  # this just print the list as it is

print(products[0].model_dump())
print(products[1])
print(repr(products[1]))
print(type(products[1]))

@app.get("/products")
def get_all_products():
    return products

@app.get("/products_from_db")
def get_all_products_db(db:Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            return products[i]
    return "product is not available for this id"
# print(get_product(3))

@app.get("/product_db/{id}")
def get_product_db(id:int, db:Session = Depends(get_db)):
    result = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if result:
        return result
    return f"Product does not exist with this id:{id}"

@app.post("/product")
def add_product(product:Product):
    products.append(product)
    return product

# @app.post("/product_db")
# def add_product_db()

@app.put("/product")
def update_product(id:int, product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated Successfully"
    return "Product id not found"

@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Producted Deleted"
    return "Product not found"