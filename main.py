from fastapi import FastAPI

import routers.notes as notes

app = FastAPI()

app.include_router(notes.router)
