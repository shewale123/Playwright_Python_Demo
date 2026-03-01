from playwright.sync_api import sync_playwright
import os

# Decide headless mode automatically for GitHub Actions
HEADLESS = os.getenv("GITHUB_ACTIONS") == "true"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=HEADLESS)
    page = browser.new_page()

    # Absolute file path for login.html
    file_path = os.path.abspath("login.html")  # login.html should be in the same folder
    page.goto(f"file://{file_path}")

    # Fill login form
    page.fill("#username", "Username")
    page.fill("#password", "1234")
    page.click("#loginBtn")

    # Wait manually only on local machine
    if not HEADLESS:
        input("Press Enter to close browser...")

    browser.close()