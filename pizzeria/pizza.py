class Pizza:
    def __init__(self, name, ingredients, size, price):
        self.name = name
        self.ingredients = ingredients
        self.size = size
        self.price = price

    def __str__(self):
        return f'пицца: {self.name}, {self.ingredients} ({self.size} см) - {self.price} руб.'
        #     in self.dimension:
        #         return f'пицца: {self.name}. {self.ingredients} ({self.size}) {self.price}.'
        #     else:

    @classmethod
    def import_from_file(cls, file_name):
        items_source = open(file_name, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for item_dict in items_source_as_dict:
            _item = cls(**item_dict)
            #_item = Student(**item_dict)
            #_item = Teacher(**item_dict)
            items.append(_item)
        return items


class Snacks(Pizza):

    def __init__(self, name, ingredients, weight, price, *args, **kwargs):
        self.name = name
        self.ingredients = ingredients
        self.weight = weight
        self.price = price

    def __str__(self):
        if self.weight:
            return f'закуски: {self.name}, {self.ingredients} ({self.weight} гр) - {self.price} руб.'
        else:
            return f'закуски: {self.name}. {self.ingredients} {self.price}.'


class Drinks(Pizza):
    def __init__(self, name, volume, price):
        self.name = name
        self.volume = volume
        self.price = price

    def __str__(self):
        return f'напитки: {self.name}, ({self.volume} л) - {self.price} руб.'



