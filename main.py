from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/list/")
async def read_items(items: list[str] | None = Query(default=None)):
    query_items = {"items": items}
    return query_items

@app.get("/filter/")
async def filter_keys(keys: list[str] | None = Query(default=None)):
    initial_dict = {
        "one": 1,
        "two": 2,
    }

    filtered_dict = { key: initial_dict[key] for key in keys }

    return filtered_dict
