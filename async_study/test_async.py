import asyncio

async def do_work(x):
    print('铺地板')
    await asyncio.sleep(10)
    print('盖房顶')

async def build_house():
    loop = asyncio.get_event_loop()
    do_many_tasks = [ asyncio.ensure_future(do_work(i)) for i in range(3)]
    await asyncio.wait(do_many_tasks)

try:
    loop = asyncio.get_event_loop()
    many_bouse_task = [ asyncio.ensure_future(build_house()) for i in range(3)]
    loop.run_until_complete(asyncio.wait(many_bouse_task))
except KeyboardInterrupt as e:
    print(asyncio.all_tasks(loop))
    for task in asyncio.all_tasks(loop):
        print('终止协程'+ str(task.cancel()))
    loop.stop()
    loop.run_forever()

