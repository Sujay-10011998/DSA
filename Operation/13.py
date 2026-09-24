async def send_pong_message(interval_seconds: int, message: str):
    """
    Periodically broadcasts a message to all connected clients.

    :param interval_seconds: Interval between messages in seconds.
    :param message: Message to be broadcasted.
    """
    while True:
        await asyncio.sleep(interval_seconds)  # Wait for the specified interval
        await broadcast_message(message)  # Broadcast the message

async def refresh_cache(interval_seconds: int):
    while True:
        ic("Starting Caching")
        cache_action = CacheActionWorkflowHandler()
        await cache_action.process_request()
        ic("Caching Done")
        await asyncio.sleep(interval_seconds)

@app.on_event("startup")
async def startup_event():
    # Start the periodic broadcasting task
    asyncio.create_task(send_pong_message(10, "ping"))
    asyncio.create_task(refresh_cache(60))