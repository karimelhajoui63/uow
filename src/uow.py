from model import Item


class UnitOfWork:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.new_models = []
        return cls._instance

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("--- EXIT ---")
        if exc_type is None:
            self.commit()
        self._instance = None
        self.new_models = []

    @classmethod
    def exists(cls) -> bool:
        return cls._instance is not None

    def register_new(self, model: Item):
        print(f"add '{model.name}' to {[i.name for i in self.new_models]}")
        self.new_models.append(model)

    def _insert(self, model):
        # Perform the insert operation
        print("FROM UoW:")
        from repo import Repo

        Repo.save(model=model, bypass_uow=True)

    def commit(self):
        for model in self.new_models:
            self._insert(model)
