from uow import UnitOfWork


class Repo:
    @staticmethod
    def save(model, bypass_uow: bool = False):
        if bypass_uow or not UnitOfWork.exists():
            print("Model SAVED in DB:", model)
        else:
            print("Just register in UoW:", model)
            UnitOfWork().register_new(model=model)
