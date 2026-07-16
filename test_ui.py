from playwright.sync_api import Page, expect


def test_saucedemo_login(page: Page):
    # 打开登录页
    page.goto("https://www.saucedemo.com/")

    # 输入账号密码
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    # 点击登录
    page.locator("#login-button").click()

    # ✅ 断言1：URL 跳转成功（自动等待页面跳转完成）
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # ✅ 断言2：页面标题正确
    expect(page.locator(".title")).to_have_text("Products")

    # ✅ 断言3：商品列表可见（有 6 个商品）
    expect(page.locator(".inventory_item")).to_have_count(6)

    # ✅ 断言4：第一个商品的名称包含 "Sauce Labs"
    first_item_name = page.locator(".inventory_item_name").first
    expect(first_item_name).to_contain_text("Sauce Labs")