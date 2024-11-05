from pages.base_page import BasePage

class CompleteOrderAndLogout(BasePage):
    BUTTON_FINISH_SELECTOR = 'button:has-text("Finish")'
    BURGER_MENU_SELECTOR = '#react-burger-menu-btn'
    LOGOUT_SELECTOR = 'a:has-text("Logout")'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    def complete_order(self):
        self.wait_for_selector_and_click(self.BUTTON_FINISH_SELECTOR)
        self.assert_text_present_on_page("Thank you for your order!")

    def logout(self):
        self.wait_for_selector_and_click(self.BURGER_MENU_SELECTOR)
        self.assert_element_is_visible('.bm-item-list')
        self.wait_for_selector_and_click(self.LOGOUT_SELECTOR)
        self.wait_for_url()
        self.assert_text_present_on_page('Swag Labs')




