import pytest
import advert
import json


def test_title():
    info_str = """{
          "title": "Вельш-корги",
          "price": 1000
        }"""
    actual = advert.dict_to_obj(json.loads(info_str), advert.Advert)
    expected_title = 'Вельш-корги'
    assert actual.title == expected_title


def test_nesting():
    info_str = """{
     "title": "iPhone X", 
     "price": 100,
     "location": {
      "address": "город Самара, улица Мориса Тореза, 50"
     }   
     }"""
    actual = advert.dict_to_obj(json.loads(info_str), advert.Advert)
    expected_address = "город Самара, улица Мориса Тореза, 50"
    assert actual.location.address == expected_address


def test_price_below_zero():
    info_str = """{
     "title": "iPhone X", 
     "price": -100 
     }"""
    with pytest.raises(ValueError):
        advert.dict_to_obj(json.loads(info_str), advert.Advert)


def test_no_price_in_json():
    info_str = """{
     "title": "iPhone X"
     }"""
    actual = advert.dict_to_obj(json.loads(info_str), advert.Advert)
    expected_price = 0
    assert actual.price == expected_price
