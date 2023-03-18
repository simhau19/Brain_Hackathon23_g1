import asyncio
import json
import websockets

async def fetch_data():
    domain = 'g1'
    service = 'mediccase'
    token = 'aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e'
    objectID = '1'
    format = 'json'
    url = f"wss://{domain}.cioty.com/{service}"

    headers = {
        "Content-Type":"application/x-www-form-urlencoded",
        "Synx-Cat":"4"
    }

    data = {
        'token': token,
        'objectID': objectID,
        'format': format
    }

    async with websockets.connect(url, extra_headers=headers) as websocket:
        await websocket.send(json.dumps(data))
        async for message in websocket:
            print(message)

asyncio.get_event_loop().run_until_complete(fetch_data())
