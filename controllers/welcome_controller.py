from starlette.responses import JSONResponse


async def homepage(request):
    return JSONResponse({'hello': 'world1'}, status_code=200)
