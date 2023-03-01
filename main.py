from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


class Product:

    id: int
    name: str
    price: int


bd = [Product() for i in range(3)]


@app.get("/notfound", response_class = HTMLResponse, status_code=404)
def notfound():
    return  "<h1>Resource Not Found</h1>"


@app.get("/")
async def root():
    return "Hello"


@app.get("/info")
async def getInfoProducts():
    return bd


@app.get("/info/{id}")
async def getInfoONEproduct(id: int):
    if id == Product.id:
        return {f"{Product.id}": f"name: {Product.name}, price: {Product.price}"}
    else:
        notfound()


@app.post("/create?id={id}&name={name}&price={}")

