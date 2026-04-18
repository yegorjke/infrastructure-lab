from fastapi import FastAPI

import routers.math as math
import routers.notes as notes

app = FastAPI()

app.include_router(notes.router)
app.include_router(math.router)
