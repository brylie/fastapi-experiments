from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/list/")
async def read_items(items: list[str] | None = Query(default=None)):
    query_items = {"items": items}
    return query_items
