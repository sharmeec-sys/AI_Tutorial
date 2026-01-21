from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launch browser (set headless=False to see browser)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Step 1: Open Google
        page.goto("https://www.google.com")

        # Step 2: Search for SA vs Aus update
        page.fill("textarea[name='q']", "SA vs Aus update latest news")
        page.keyboard.press("Enter")

        # Step 3: Wait for search results
        page.wait_for_selector("h3")

        # Step 4: Click the first result
        page.locator("h3").first.click()

        # Step 5: Wait for page to load
        page.wait_for_load_state("networkidle")

        # Step 6: Get page title (latest news headline)
        print("\nLatest News Title:")
        print(page.title())

        # Optional: Extract f
