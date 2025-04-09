import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        safe_name = url.replace("http://", "").replace("https://", "").replace("/", "_").strip()
        if not safe_name:
            safe_name = "index"
        file_name = f"{safe_name}.html"
        with open(file_name, "wb") as outfile:
            outfile.write(response.content)
        print(f"Downloaded: {url} -> {file_name}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python link_downloader.py <URL>")
        sys.exit(1)
    start_time = time.time()
    url = sys.argv[1]
    try:
        main_response = requests.get(url)
        main_response.raise_for_status()
        html_content = main_response.text
    except Exception as e:
        print(f"Error downloading main page {url}: {e}")
        sys.exit(1)
    with open("main_page.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Main page downloaded as main_page.html")
    soup = BeautifulSoup(html_content, "html.parser")
    links = []
    for tag in soup.find_all("a", href=True):
        full_url = urljoin(url, tag["href"])
        links.append(full_url)
    links = list(set(links))
    print(f"Found {len(links)} links on the page.")
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_link = {executor.submit(download_url, link): link for link in links}
        for future in as_completed(future_to_link):
            link = future_to_link[future]
            try:
                future.result()
            except Exception as err:
                print(f"Error processing {link}: {err}")
    elapsed = time.time() - start_time
    print(f"Time taken: {elapsed:.2f} secs")

if __name__ == "__main__":
    main()
