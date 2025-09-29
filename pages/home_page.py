class HomePage:
    def __init__(self, page):
        self.page = page
        # Example locators (update as per your actual UI)
        self.welcome_banner = page.locator(".welcome-banner")
        self.profile_icon = page.locator("#profileIcon")
        self.logout_button = page.locator("button#logout")  
        self.content = page.locator('//h2[text()="Select Complaint Type"]') 

    def get_welcome_text(self):
        return self.welcome_banner.text_content()
    
    def get_content_txt(self):
        return self.content.text_content()

    def click_profile(self):
        self.profile_icon.click()

    def logout(self):
        self.logout_button.click()
