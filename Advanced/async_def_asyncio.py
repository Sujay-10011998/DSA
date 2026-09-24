import asyncio

async def greet(name):
    print(f"Hello, {name}")
    await asyncio.sleep(1)  # Non-blocking delay
    print(f"How are you, {name}?")

async def main():
    await asyncio.gather(
        greet("Alice"),
        greet("Bob")
    )

asyncio.run(main())
