from playwright.sync_api import Page, expect

 # 1. 打开 saucedemo
    # 2. 填用户名
    # 3. 填密码
    # 4. 点登录
    # 5. 断言跳转到 inventory 页
def test_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name","standard_user")
    page.fill("#password","secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
     

     
