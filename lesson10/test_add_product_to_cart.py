import pytest

@pytest.mark.test12
def test_add_product(create_page):

    app = create_page

    app.add_to_cart(items=3)

    app.delete_from_cart()

    assert app.cart_page.is_empty_cart()
