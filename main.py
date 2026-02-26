import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = "https://www.yellowpages-uae.com/uae/hospitals?page={}"

# Open CSV file
csv_file = open("Hospitals_UAE.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(csv_file)
writer.writerow(["Name", "Location", "City", "Phone", "Website", "Products & Services"])

# Loop through 5 pages
for page in range(1, 6):
    url = base_url.format(page)
    print(f"🔎 Scraping page {page} ... {url}")
    driver.get(url)
    time.sleep(3)

    # Scrape all listings
    listings = driver.find_elements(By.CSS_SELECTOR, "div.flex.flex-grow.flex-col.w-full")

    for item in listings:
        # Name
        try:
            name = item.find_element(By.TAG_NAME, "h3").text.strip()
        except:
            name = ""

        # Location
        try:
            location = item.find_element(
                By.XPATH, ".//span[contains(text(),'Location')]/following-sibling::span"
            ).text.strip()
        except:
            location = ""

        # City
        try:
            city = item.find_element(
                By.XPATH, ".//span[contains(text(),'City')]/following-sibling::span"
            ).text.strip()
        except:
            city = ""

        # Phone
        try:
            phone_element = item.find_element(By.XPATH, ".//a[@aria-label='Phone']")
            phone = phone_element.get_attribute("href").replace("tel:", "").strip()
        except:
            phone = ""

        # Website
        try:
            website = item.find_element(
                By.XPATH, ".//button[contains(@class,'listing_button')]"
            ).get_attribute("data-url")
        except:
            website = ""

        # Products & Services (multiple links support)
        try:
            links = item.find_elements(
                By.CSS_SELECTOR, "div.flex.flex-wrap span.font-semibold + h4 div span a"
            )
            products = ", ".join([a.text.strip() for a in links])
        except:
            products = ""

        # Write row
        writer.writerow([name, location, city, phone, website, products])

    time.sleep(1)  # polite delay

# Close CSV and browser
csv_file.close()
driver.quit()
print("✅ Data scraping complete! Saved to Hospitals_UAE.csv")
