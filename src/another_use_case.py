from time import sleep

from model import Item
from repo import Repo


class AnotherUseCase:
    @staticmethod
    def method():
        another_inner_item = Item(name="another_inner_item")
        AnotherUseCase.heavy_work()
        Repo.save(model=another_inner_item)

    @staticmethod
    def heavy_work():
        print("heavy work in progress...")
        sleep(5)
