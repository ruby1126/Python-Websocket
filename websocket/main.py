import websockets
import asyncio
import datetime


async def timerun(websocket, path):
    now = datetime.datetime.utcnow().isoformat() + "Z"
    print("有人進來囉 " + str(now))
    await asyncio.sleep(1)


start_server = websockets.serve(timerun, "localhost", 8765)
# asyncio.get_event_loop().run_until_complete(start_server)
asyncio.ensure_future(start_server)
asyncio.get_event_loop().run_forever()