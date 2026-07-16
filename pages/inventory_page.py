from playwright.sync_api import Page, expect


class InventoryPage:  # ✅ 类名必须是 InventoryPage（大写 I，大写 P）
    """商品列表页的 Page Object"""

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.shopping_cart = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_title_text(self) -> str:
        return self.title.text_content()

    def get_item_count(self) -> int:
        return self.inventory_items.count()

    def add_item_to_cart(self, item_name: str):
        add_button = self.page.locator(
            f".inventory_item:has-text('{item_name}') .btn_inventory"
        )
        add_button.click()

    def go_to_cart(self):
        self.shopping_cart.click()

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0