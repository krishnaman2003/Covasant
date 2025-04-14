"""
Question-8:
Given a URL, download that and parse and download all links inside that page in thread 
- use concurrent, Concurrent Programming, decorators, Iterators, ThreadPoolExecutor, BeautifulSoup for parsing html, requests for downloading.
"""

import requests
import os
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
import time

def profile(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time} seconds")
        return result
    return wrapper

def download_link(url, download_folder):
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or filename == '/': 
             filename = f"download_{int(time.time()*1000)}.html" 
        filepath = os.path.join(download_folder, filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed {url}: {e}")

@profile
def download_all_links(start_url, download_folder="downloads", max_workers=5):
    os.makedirs(download_folder, exist_ok=True)
    try:
        response = requests.get(start_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links_to_download = set()
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(start_url, link['href'])
            if absolute_url.startswith(('http://', 'https://')):
                links_to_download.add(absolute_url)
        print(f"Found {len(links_to_download)} links. Starting download...")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(download_link, url, download_folder) for url in links_to_download]
        print("Finished downloading.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_url = "https://docs.python.org/3/"
    print(f"Processing URL: {target_url}")
    download_all_links(target_url)
