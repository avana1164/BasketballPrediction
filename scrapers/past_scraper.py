from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

url = "https://www.nba.com/stats/teams/advanced?Season=2023-24"

chrome_options = Options()
chrome_options.add_argument("--enable-unsafe-swiftshader")
chrome_options.add_argument("--headless")  # Run browser in headless mode
# chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (useful for headless)
# chrome_options.add_argument("--no-sandbox")  # Avoid sandbox issues (optional)
# chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome resource limitations (optional)

# setup driver and connect it to url
service = Service("../../chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url)
driver.implicitly_wait(10)

stats = driver.find_element(By.CSS_SELECTOR, "tbody.Crom_body__UYOcU")
print(stats.text)

driver.quit()