import threading, time, requests, os, concurrent.futures
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def profile(func):
    def _inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(f"{func.__name__} ({threading.current_thread().name}): {round(time.time() - start_time, 2)} secs")
        return res
    return _inner

class LinkIterator:
    def __init__(self, links):
        self.links = links
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.links):
            link = self.links[self.index]
            self.index += 1
            return link
        raise StopIteration

class UrlDownloader:
    def __init__(self, url, output_dir="downloads"):
        self.url = url
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    @profile
    def download(self, url):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                file_name = os.path.basename(url) or "index.html"
                if '.' not in file_name:
                    file_name += ".html"
                path = os.path.join(self.output_dir, file_name)
                with open(path, "wb") as f:
                    f.write(response.content)
                print("Downloaded:", url)
                return response.text
        except Exception as e:
            print(f"Error {url}: {e}")
    def get_links(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return [urljoin(self.url, a["href"]) for a in soup.find_all("a", href=True) if a["href"].startswith("http")]
    @profile
    def process(self, max_threads=4, max_links=10):
        html = self.download(self.url)
        if not html:
            return
        links = self.get_links(html)[:max_links]
        print(f"Found {len(links)} links")
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as ex:
            ex.map(self.download, LinkIterator(links))

if __name__ == "__main__":
    url = "https://python.org"
    UrlDownloader(url).process(4, 10)
