import requests
from bs4 import BeautifulSoup

def crawl(url, visited=set(), min_per_page=10):
    if url in visited:
        return
    visited.add(url)
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Error scraping: {url}\nError:\n\n{e}")
        return visited
    soup = BeautifulSoup(response.text, 'html.parser')
    print(url)
    links = soup.find_all('a', href=True)
    if len(links) > min_per_page:
        links = links[:min_per_page]
    for link in links:
        crawl(requests.compat.urljoin(url, link['href']), visited)

visited = crawl('http://example.com')
