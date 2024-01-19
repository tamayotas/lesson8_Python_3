"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(99) == True
        assert product.check_quantity(100) == True
        assert product.check_quantity(101) == False


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(99) == 'Passed'
        assert product.buy(100) == 'Passed'

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(101)

@pytest.fixture
def cart():
    return Cart()

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product)
        assert 1 == cart.products.get(product)
        cart.add_product(product, 3)
        assert 4 == cart.products.get(product)

    def test_remove_product(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 2)
        assert 1 == cart.products.get(product)
        cart.remove_product(product, 1)
        assert 0 == cart.products.get(product)
        cart.add_product(product, 3)
        cart.remove_product(product, 4)
        assert None is cart.products.get(product)

    def test_clear(self, cart, product):
        cart.add_product(product, 3)
        cart.clear()
        assert {} == cart.products

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 3)
        cart.add_product(Product("hook", 200, "This is a hook", 2000), 3)
        assert 900 == cart.get_total_price()

    def test_buy(self, cart, product):
        cart.add_product(product, 3)
        cart.buy()
        assert 997 == product.quantity
        assert {} == cart.products
