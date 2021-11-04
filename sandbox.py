import click

@click.command()
@click.argument('url')
def get_webpage(url):
    """Open URL and find the element we're looking for"""
    print(url)

if __name__ == '__main__':
    get_webpage()