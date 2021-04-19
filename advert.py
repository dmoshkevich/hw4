import json
import keyword


class ColorizeMixin:
    """
    change the text color when output to the console
    """
    repr_color_code = 33

    def __repr__(self):
        """
        display the name and price of the ad
        """
        return f'\033[1;{self.repr_color_code};1m ' \
               f'{self.title} | {self.price} ₽' \
               f'\033[0;1;1m'


class Advert(ColorizeMixin):
    """
    Advert info
    """
    _price = 0

    def __setattr__(self, key, value):
        if keyword.iskeyword(key):
            key = key + "_"
        super.__setattr__(self, key, value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, var: int):
        if var < 0:
            raise ValueError("value should be >= 0")
        self._price = var


def dict_to_obj(data: dict, cls: object) -> object:
    """
    Convert dict into object
    """
    obj = cls()
    for a, b in data.items():
        if isinstance(b, (list, tuple)):
            obj.__setattr__(a, [dict_to_obj(x, cls)
                                if isinstance(x, dict)
                                else x for x in b])
        else:
            obj.__setattr__(a, dict_to_obj(b, cls)
                            if isinstance(b, dict) else b)
    return obj


if __name__ == '__main__':
    info_str = """{
      "title": "Вельш-корги",
      "price": 1000,
      "class": "dogs",
      "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
      }
    }"""
    inf_str = json.loads(info_str)
    corgi = dict_to_obj(inf_str, Advert)
    print(corgi.class_)
    print(corgi)
    print(corgi.location.address)
