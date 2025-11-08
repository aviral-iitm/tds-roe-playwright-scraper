from playwright.sync_api import sync_playwright
import re

seeds = list(range(36, 46))
total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        page.goto(url)
        page.wait_for_selector('table')
        
        # Get all table text
        tables = page.query_selector_all('table')
        for table in tables:
            text = table.inner_text()
            # Extract all numbers (including negative)
            numbers = re.findall(r'-?\d+\.?\d*', text)
            for num in numbers:
                try:
                    total_sum += float(num)
                except ValueError:
                    pass
    
    browser.close()

print(f"Total sum across all seeds (36-45): {total_sum}")
