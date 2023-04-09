from app.outers.repositories.item_combination_map_repository import ItemCombinationMapRepository
from app.outers.repositories.item_repository import ItemRepository


class SyncItemCombination:

    def __init__(self):
        self.item_repository: ItemRepository = ItemRepository()
        self.item_combination_repository: ItemCombinationMapRepository = ItemCombinationMapRepository()
