
import asyncio
import aiohttp 
from aiohttp import web
import aiofiles


async def Index_View(request):
    print(dir(request))
    if request.method == "POST":
        print("method post")

    async with aiofiles.open("templates/index.html", "r") as f:
        await f.seek(0)
        text = await f.read()

    return web.Response(text=text, content_type="text/html")

app = web.Application()
app.router.add_get("/", Index_View)

web.run_app(app)
