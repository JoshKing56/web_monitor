import click
import urllib3
from datetime import datetime
import time
from bs4 import BeautifulSoup
import update_handler

check_interval = 10

@click.command()
@click.argument('url')
def get_webpage(url):
    """Open URL and find the element we're looking for"""
    current_page = None
    while(True):
        req = urllib3.PoolManager()
        res = req.request('GET', url)
        soup = BeautifulSoup(res.data, 'html.parser')
        if current_page == None:
            print("Fetched page for the first time")
            current_page = soup.prettify()
        else:
            if current_page != soup.prettify():
                print("Update detected")
                update_handler.handle_update(url, current_page, soup.prettify())
                current_page = soup.prettify()
            else:
                print(f"Last update at: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
                time.sleep(check_interval)

 
if __name__ == '__main__':
    get_webpage()