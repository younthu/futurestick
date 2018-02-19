import click
import requests

@click.group()
def cli():
    pass

@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

@cli.command()
@click.option('--quote', default='AG0', help='index of futures quote, could be a comma splitted array')
def get_quote(quote):
    """Getting data from sina api"""
    response = requests.get("http://hq.sinajs.cn/list="+quote)
#    print(response.text)
    #print(response.json())
    arr = response.text.split('=')[1].strip('"').split(',')
    print(arr[0]+","+arr[16]+"," + arr[15] + "," + arr[17] + "," + arr[5] + "    " + arr[8]) # please check ticket #74 for detailed fields explain


if __name__ == '__main__':
   # hello()
   cli()
   pass
