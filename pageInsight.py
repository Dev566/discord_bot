from playwright.sync_api import sync_playwright
from flask import jsonify

def run(playwright):
    # Launch the browser (Chromium)
    browser = playwright.chromium.launch(headless=True)  # Set headless=True to run in headless mode
    page = browser.new_page()

    # Navigate to PageSpeed Insights
    page.goto("https://pagespeed.web.dev/")

    # Enter the URL you want to analyze
    url_to_analyze = "https://dev.waku-travel.com/"  # Replace with the URL you want to analyze
    page.fill('input[placeholder="Enter a web page URL"]', url_to_analyze)
    print("Button")
    # Click on the "Analyze" button
    page.click('button:has-text("Analyze")')
    print("Wait for load")
    # jsname="O2CIGd"
    # Wait for the results to load (can take some time depending on the URL)
    page.wait_for_selector('text=performance score is calculated', timeout=60000)
    print("Final URL:", page)
    # Take a screenshot of the results
    page.screenshot(path="pagespeed_results.png", full_page=True)
    

    # Close the browser
    browser.close()
    

def run_playwright_script():
    with sync_playwright() as playwright:
        # Launch the browser
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a website
        page.goto("https://pagespeed.web.dev/")

        # Enter the URL you want to analyze
        url_to_analyze = "https://dev.waku-travel.com/"  # Replace with the URL you want to analyze
        page.fill('input[placeholder="Enter a web page URL"]', url_to_analyze)
        print("Button")
        # Click on the "Analyze" button
        page.click('button:has-text("Analyze")')
        print("Wait for load")
        # Wait for the results to load (can take some time depending on the URL)
        page.wait_for_selector('text=performance score is calculated', timeout=60000)
        print("Final URL:", page)
        # Retrieve the final URL
        # final_url = jsonify(page)
        final_url = page.url()
        print("Final URL:", final_url)

        # Close the page and browser
        page.close()
        browser.close()

        return final_url

# print("Printing")
# # Execute the Playwright script
# with sync_playwright() as playwright:
#     run(playwright)