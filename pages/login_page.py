class LoginPage:
    def __init__(self,page):
        self.page = page
        self.admin_user_tab=page.locator("//button[text()='Admin User']")
        self.managment_admin_tab=page.locator("//button[text()='Management Admin']")
        self.mobile_num=page.locator("input#mobile")
        self.password=page.locator("input#password")
        self.sign_in_btn=page.locator("button[type=submit]")
    def click_on_management_admin(self):
        self.managment_admin_tab.click()
    def login(self,userName,password,base_url):
      
        self.page.goto(base_url)
        self.mobile_num.fill(userName)
        self.password.fill(password)
        self.sign_in_btn.click()