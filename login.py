from playwright.sync_api import sync_playwright
import os

# Decide headless mode based on environment
HEADLESS = os.getenv("GITHUB_ACTIONS") == "true"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=HEADLESS)
    page = browser.new_page()

    # Relative path for GitHub Actions
    page.goto("login.html")  

    page.fill("#username", "Username")
    page.fill("#password", "1234")
    page.click("#loginBtn")

    if not HEADLESS:
        input("Press Enter to close browser...")

    browser.close()