#!/usr/bin/env python
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
    """Getting data from sina api.
 RB0 螺纹钢
 AG0 白银
 AU0 黄金
 CU0 沪铜
 AL0 沪铝
 ZN0 沪锌
 PB0 沪铅
 RU0 橡胶
 FU0 燃油
 WR0 线材
 A0 大豆
 M0 豆粕
 Y0 豆油
 J0 焦炭
 C0 玉米
 L0 乙烯
 P0 棕油
 V0 PVC
 RS0 菜籽
 RM0 菜粕
 FG0 玻璃
 CF0 棉花
 WS0 强麦
 ER0 籼稻
 ME0 甲醇
 RO0 菜油
 TA0 甲酸
    """
    response = requests.get("http://hq.sinajs.cn/list="+quote)
#    print(response.text)
    #print(response.json())
    for arrraw in response.text.splitlines():
        arr = arrraw.split('=')[1].strip(';').strip('"').split(',')
        print(arr[0]+","+arr[16]+"," + arr[15] + "," + arr[17] + "," + arr[5] + "    " + arr[8]) # please check ticket #74 for detailed fields explain


if __name__ == '__main__':
   # hello()
   cli()
   pass
