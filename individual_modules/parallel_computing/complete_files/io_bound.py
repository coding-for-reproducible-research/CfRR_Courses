import time
import requests


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_single_site(url, session)


def download_single_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} bytes from {url}")


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
