import playwright.sync_api

with playwright.sync_api.sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("file:///C:/Users/hp/Projects/Playwright_Python_Demo/login/login.html")

    page.fill("#username", "Username")
    page.fill("#password", "1234")
    page.click("#loginBtn")

    

    input("Press Enter to close browser...")
browser.close()