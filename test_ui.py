from playwright.sync_api import sync_playwright
import time

from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False, slow_mo=500)
# page = browser.new_page()
# page.goto("https://www.saucedemo.com/")
#
#
# page.type(selector='[id="user-name"]', text='standard_user', delay=100)
# page.fill(selector='#password', value='secret_sauce')
# page.click(selector='.submit-button')
# page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout=10000)
# page.wait_for_selector('#inventory_container')
#
# button_and_cart = '[data-test="add-to-cart-sauce-labs-backpack"]'
# alt_locator_for_card = '.inventory_item a:has-text("Sauce Labs Backpack")'
# card_button_1 = '.inventory_item_description:has-text("Sauce Labs Backpack") button:has-text("Add to cart")'
# card_button_2 = '.inventory_item_description:has-text("Sauce Labs Bike Light") button:has-text("Add to cart")'
# cart = '[data-test="shopping-cart-link"]'
#
#
# page.is_visible(selector=button_and_cart)
# page.is_enabled(selector=button_and_cart)
# # page.click(selector=button_and_cart)
# # page.click(selector=alt_locator_for_card)
# page.click(selector=card_button_1)
# page.click(selector=card_button_2)
# page.is_visible(selector=cart)
# page.click(selector=cart)
#
# page.wait_for_url('https://www.saucedemo.com/cart.html', timeout=10000)
# page.wait_for_selector('.cart_list')
#
# button_checkout = '#checkout'
# page.wait_for_selector(button_checkout)
# page.is_visible(button_checkout)
# page.is_enabled(button_checkout)
# page.click(selector=button_checkout)
# page.wait_for_url('https://www.saucedemo.com/checkout-step-one.html', timeout=10000)
#
# page.fill(selector='#first-name', value='Ornella')
# page.fill(selector='#last-name', value='Chislyuk')
# page.fill(selector='#postal-code', value='242534543')
# page.click(selector='[type="submit"][id="continue"]')
#
# page.wait_for_url('https://www.saucedemo.com/checkout-step-two.html', timeout=10000)
# page.wait_for_selector('button:has-text("Finish")')
# page.click(selector='button:has-text("Finish")')
# page.wait_for_url('https://www.saucedemo.com/checkout-complete.html', timeout=10000)
# time.sleep(5)
#
# browser.close()
# playwright.stop()


def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.type_and_fill_checkout_form('Ornella', 'Chislyuk', '242534543')