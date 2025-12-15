from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def scrape_runway_status():
    # ... scraping logic here ...
    url = 'https://en.lvnl.nl/runway-use'
    options = Options()
    # Uncomment the next line to run headless (no browser window)
    options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service('C:/Users/vishu/Downloads/dev-tools/chromedriver-win64/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')
    g_elements = soup.find_all('g')
    runways = []
    for g in g_elements:
        class_attr = g.get('class')
        if class_attr:
            runway_name = class_attr[0].capitalize()
            if 'take-off' in class_attr:
                activity = 'Take-off'
            elif 'landing' in class_attr:
                activity = 'Landing'
            else:
                activity = 'Silent'
            runways.append({'name': runway_name, 'activity': activity})
    return runways