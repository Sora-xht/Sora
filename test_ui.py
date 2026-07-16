# test_ui.py
from playwright.sync_api import Page, expect

def test_example_page(page: Page):
    page.goto("https://example.com")  # 打开网页
    # 使用 page.locator() 定位元素，支持CSS选择器和文本等
    header = page.locator("h2")
    # 使用 expect 进行断言，这是Playwright推荐的断言方式
    expect(header).to_have_text("Example Domain")