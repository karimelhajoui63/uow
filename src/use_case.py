import random

from another_use_case import AnotherUseCase
from model import Item
from repo import Repo
from uow import UnitOfWork


class UseCase:
    @staticmethod
    def method(item: Item):
        with UnitOfWork():
            print("--- START ---")
            Repo.save(model=item)

            AnotherUseCase.method()

            # if random.choice([True, False]):
            #     raise NotImplementedError()

            inner_item = Item(name="inner_item")
            Repo.save(model=inner_item)
            print("--- END ---")
