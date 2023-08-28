from model import Item
from repo import Repo


class AnotherUseCase:
    @staticmethod
    def method():
        another_inner_item = Item(name="another_inner_item")
        Repo.save(model=another_inner_item)
