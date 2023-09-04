# # coroutine
import asyncio
#
#


def prvni_coroutine(name: str) -> str:
    # await asyncio.sleep(seconds)
    print(f"Yuchuuu vytvoril jsem {name} coroutine!")
#
#
# def normalni_funkce():
#     print("O joj, ja jsem normalni funkce. Uz me nebudes potrebovat?")
#
#
# asyncio.run(prvni_coroutine())
# normalni_funkce()


async def main():
    loop = asyncio.get_running_loop()
    print("Start")

    await asyncio.sleep(1)
    loop.call_soon(prvni_coroutine, "pepa")
    print("End")


async def main():
    result_first = await prvni_coroutine("franta", 1)
    result_second = await prvni_coroutine("pepa", 2)
    print(result_first)
    print(result_second)
    print("Co to je?")


asyncio.run(main())
