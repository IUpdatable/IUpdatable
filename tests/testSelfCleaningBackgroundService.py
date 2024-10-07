import time
from iupdatable.services.SelfCleaningBackgroundService import SelfCleaningBackgroundService


class Demo(SelfCleaningBackgroundService):
    _counter = 0

    def _background_task(self):
        while True:
            self._counter += 1
            time.sleep(1)
            print("counter:" + str(self._counter))


if __name__ == '__main__':
    demo = Demo()
    time.sleep(5.1)  # 稍等一会儿，以便演示后台任务
    print("结束")  # main函数结束，后台任务自动结束
