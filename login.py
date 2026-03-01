from playwright.sync_api import sync_playwright
import os

# GitHub Actions me headless mode
HEADLESS = os.getenv("GITHUB_ACTIONS") == "true"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=HEADLESS)
    page = browser.new_page()

    # Correct relative path
    page.goto("login/login.html")  

    page.fill("#username", "Username")
    page.fill("#password", "1234")
    page.click("#loginBtn")

    if not HEADLESS:
        input("Press Enter to close browser...")

    browser.close()