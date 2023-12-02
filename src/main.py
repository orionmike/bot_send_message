import uvicorn

from fastapi import FastAPI, Request
from message.router import router as router_message

app = FastAPI()

app.include_router(router_message)


# @app.get('/')
# async def send_message():
#     print('ok')
#     return 'ok'

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
