from playwright.sync_api import Page, expect


class LoginPage:
    """登录页面的 Page Object"""

    def __init__(self, page: Page):
        """
        构造函数：接收 page 对象，初始化页面上的所有元素定位器
        """
        self.page = page

        # ========== 元素定位器（作为类的属性） ==========
        # 用户名输入框
        self.username_input = page.locator("#user-name")
        # 密码输入框
        self.password_input = page.locator("#password")
        # 登录按钮
        self.login_button = page.locator("#login-button")
        # 错误信息提示
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        """打开登录页面"""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        """
        执行登录操作
        :param username: 用户名
        :param password: 密码
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        """
        获取错误提示文本
        :return: 错误信息的文本内容
        """
        return self.error_message.text_content()

    def wait_for_login_success(self):
        """等待登录成功后跳转到商品页"""
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def is_error_visible(self) -> bool:
        """判断错误信息是否可见"""
        return self.error_message.is_visible()