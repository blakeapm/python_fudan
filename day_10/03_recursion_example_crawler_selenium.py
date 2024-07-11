import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin, urlparse

def is_html_page(url):
    """Check if the URL points to an HTML page."""
    skip = ('.pdf', '.jpg', '.jpeg', '.png', '.gif', '.zip', '.rar')
    return not url.lower().endswith(skip)

def crawl(driver, url, visited=set(), min_per_page=10):
    if url in visited:
        return visited
    if not is_html_page(url):
        return visited
    
    visited.add(url)
    try:
        driver.get(url)
        time.sleep(2)  # Allow time for the page to load
    except Exception as e:
        print(f"Error scraping: {url}\nError:\n\n{e}")
        return visited
    
    print(url)
    links = driver.find_elements(By.XPATH, '//a[@href]')
    if len(links) > min_per_page:
        links = links[:min_per_page]
    
    for link in links:
        try:
            href = link.get_attribute('href')
            if href and is_html_page(href):
                crawl(driver, urljoin(url, href), visited)
        except Exception as e:
            print(f"Error getting href from: {url}\nError:\n\n{e}")
    return visited

if __name__ == "__main__":
    driver = webdriver.Chrome()
    visited = crawl(driver, 'http://example.com')
    driver.quit()
    print("Visited URLs:", visited)
