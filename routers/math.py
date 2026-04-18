from fastapi import APIRouter

import helpers.math

router = APIRouter(prefix="/math", tags=["math"])


@router.get("/square/{x}")
async def getSquare(x: int | float):
    return {"message": helpers.math.square(x)}


@router.get("/cube/{x}")
async def getCube(x: int | float):
    return {"message": helpers.math.cube(x)}


@router.get("/sqrt/{x}")
async def getSqrt(x: int | float):
    return {"message": helpers.math.sqrt(x)}
