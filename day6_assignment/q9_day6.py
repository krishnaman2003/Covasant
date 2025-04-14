import asyncio
import os
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys

async def download_url(session, url, download_folder):
    try:
        async with session.get(url, timeout=20) as response:
            response.raise_for_status()
            content = await response.read()
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename or filename.endswith('/'):
                 filename = f"download_{hash(url)}.file"
            filepath = os.path.join(download_folder, filename)
            with open(filepath, 'wb') as f:
                f.write(content)
            print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed {url}: {e}")

async def main(start_url, download_folder="downloads"):
    os.makedirs(download_folder, exist_ok=True)
    print(f"Processing URL: {start_url}")
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(start_url, timeout=20) as response:
                response.raise_for_status()
                html_content = await response.text()
            soup = BeautifulSoup(html_content, 'html.parser')
            links = set()
            for link in soup.find_all('a', href=True):
                absolute_url = urljoin(start_url, link['href'])
                if absolute_url.startswith(('http://', 'https://')):
                    links.add(absolute_url)
            if not links:
                 print("No links found to download.")
                 return
            print(f"Found {len(links)} links. Starting download...")
            tasks = [asyncio.create_task(download_url(session, link_url, download_folder)) for link_url in links]
            await asyncio.gather(*tasks)
            print("Finished downloading.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
if __name__ == "__main__":
    target_url = "https://docs.python.org/3/"
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(target_url))