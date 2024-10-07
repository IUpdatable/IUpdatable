import asyncio
from iupdatable import Timer
from iupdatable.services.SelfCleaningBackgroundService import SelfCleaningBackgroundService


class Demo(SelfCleaningBackgroundService):

    def __init__(self, name, is_debug=False, auto_start=True):
        super().__init__(is_debug=is_debug, auto_start=auto_start)
        self._name = name
        self._counter = 0

    async def _background_task(self):
        while True:
            self._counter += 1
            print(f"{Timer.get_now_time_str()}: {self._name} counter: {self._counter}")
            await asyncio.sleep(1)


async def main():
    # 创建一个自动启动的 Demo 实例
    demo1 = Demo(name="demo1", is_debug=True)
    print(f"{Timer.get_now_time_str()}: Demo1 created (auto-start)")
    await asyncio.sleep(3)

    # 停止 demo1
    print(f"{Timer.get_now_time_str()}: Stopping demo1")
    demo1.stop()
    await asyncio.sleep(3)

    # 重新启动 demo1
    print(f"{Timer.get_now_time_str()}: Restarting demo1")
    demo1.start()
    await asyncio.sleep(2)

    # 创建一个不自动启动的 Demo 实例
    demo2 = Demo(name="demo2", is_debug=True, auto_start=False)
    print(f"{Timer.get_now_time_str()}: Demo2 created (not auto-start)")
    await asyncio.sleep(2)

    # 手动启动 demo2
    print(f"{Timer.get_now_time_str()}: Starting demo2")
    demo2.start()
    await asyncio.sleep(3)

    print(f"{Timer.get_now_time_str()}: Main function ending")

if __name__ == "__main__":
    asyncio.run(main())
