from fastapi import FastAPI

app = FastAPI()


@app.get("/add")
def add_numbers(a: float, b: float):
    return {"result": a + b}


@app.get("/greet")
# @app.get("/greet/{name}")
def greet(name: str | None = None):
    if name:
        return {"message": f"Hello {name}"}
    else:
        return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
