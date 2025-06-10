import threading
import time
from concurrent.futures import ThreadPoolExecutor
import requests

thread_local = threading.local()


def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_single_site, sites)


def download_single_site(url):
    session = get_session_for_thread()
    with session.get(url) as response:
        print(f"Read {len(response.content)} bytes from {url}")


def get_session_for_thread():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


# Create list of site to download
sites = [
        "https://www.exeter.ac.uk/research/research-software-and-analytics/",
        "https://coding-for-reproducible-research.github.io/CfRR_Courses/home_page.html",
    ] * 100

# Report time for downloading all sites
start_time = time.perf_counter()
download_all_sites(sites)
run_time = time.perf_counter() - start_time
print(f"Downloaded {len(sites)} sites in {run_time} seconds")