import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(page: Page):
    """测试：使用标准用户成功登录"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    login_page.wait_for_login_success()
    inventory_page = InventoryPage(page)
    assert inventory_page.get_title_text() == "Products"
    assert inventory_page.get_item_count() == 6


def test_locked_out_user(page: Page):
    """测试：使用锁定用户登录，验证错误信息"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    error_text = login_page.get_error_message()
    assert "locked out" in error_text


def test_invalid_password(page: Page):
    """测试：使用错误密码登录"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "wrong_password")

    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text