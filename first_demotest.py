
print("Script started")

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # headless=True for instant output
    page = browser.new_page()
    page.goto("https://www.google.com")
    print("Page title is:", page.title())
    browser.close()

print("Script finished")
# Trigger workflow run