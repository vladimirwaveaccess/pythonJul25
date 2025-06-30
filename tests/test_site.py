import time

from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(browser):
    homepage = HomePage(browser)
    product_page = ProductPage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page.check_title_is("Samsung galaxy s6")


def test_monitor(browser):
    homepage = HomePage(browser)
    product_page = ProductPage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    product_page.check_products_count(2)
    time.sleep(2)
