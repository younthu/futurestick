#!/usr/bin/env python
import os
import click
import requests
from time import sleep
from models.trade import Trade
from models.stop import Stop
from pymongo import *

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
@click.option('--quote', '-q', default='AG0', help='index of futures quote, could be a comma splitted array')
@click.option('--repeat','-r',  default=True, help='refresh infinitely')
@click.option('--save', '-s', default=True, help='save ticks to mongo db')
def get_quote(quote, repeat, save):
    """ list of codes:
    郑商所：
    TA0	    PTA连续
    OI0	    菜油连续
    RS1809	菜籽1809
    RM0	    菜粕连续
    ZC0	    动力煤连续
    WH0	    强麦连续
    JR1805	粳稻1805
    SR0	    白糖连续
    CF0	    棉花连续
    RI0	    早籼稻连续
    MA0	    郑醇连续
    FG0	    玻璃连续
    LR0	    晚籼稻连续
    SF0	    硅铁连续
    SM0	    锰硅连续
    CY1809	棉纱1809

    大连商品交易所:
    V0	PVC连续
    P0	棕榈连续
    B0	豆二连续
    M0	豆粕连续
    I0	铁矿石连续
    JD0	鸡蛋连续
    L0	塑料连续
    PP0	PP连续
    BB0	胶合板连续
    Y0	豆油连续
    C0	玉米连续
    A0	豆一连续
    J0	焦炭连续
    JM0	焦煤连续
    CS0	玉米淀粉连续

    上海期货交易所:
    FU0	燃油连续
    AL0	沪铝连续
    RU0	橡胶连续
    ZN0	沪锌连续
    CU0	沪铜连续
    AU0	黄金连续
    RB0	螺纹钢连续
    WR0	线材连续
    PB0	沪铅连续
    AG0	白银连续
    BU0	沥青连续
    HC0	热轧卷板连续
    SN0	沪锡连续
    NI0	沪镍连续

    中国金融期货交易所
    IF0	期指0
    TF0	TF0

    更多请参考： http://vip.stock.finance.sina.com.cn/quotes_service/view/qihuohangqing.html
    """
    response = requests.get("http://hq.sinajs.cn/list="+quote)
    client = MongoClient()
    db = client.futuresticks
    collection = db.first_product

    while True:
        linenum = 0
        for arrraw in response.text.splitlines():
            arr = arrraw.split('=')[1].strip(';').strip('"').split(',')
            print(arr[0]+","+arr[16]+"," + arr[15] + "," + arr[17] + "," + arr[5] + "    " + arr[8])

            if save:
                collection.insert({'code':quote, 'tick': arr[8]})

            linenum = linenum + 1

        if not repeat:
            break

        sleep(1)

        # clear buffer#
        #  "\033[F" move one line up, '\r' move cursor back to beginning of line
        print("\033[F" * (linenum + 1) + '\r')


@cli.command()
@click.option('--code', '-c', help='code of tureus product')
@click.option('--limit', '-l', help='when to alert. a positive number means top limit, a minus number means bottom limit')
def watch(code, limit):
    response = requests.get("http://hq.sinajs.cn/list="+code)
    notified = False

    while True:
        linenum = 1

        for arrraw in response.text.splitlines():
            arr = arrraw.split('=')[1].strip(';').strip('"').split(',')
            print(arr[0]+","+arr[16]+"," + arr[15] + "," + arr[17] + "," + arr[5] + "    " + arr[8])

        #    if save:
        #        collection.insert({'code':quote, 'tick': arr[8]})

            if float(limit) < 0 and float(arr[8]) + float(limit) < 0:
                print("break bottom limit:" + limit * -1)

                if not notified:
                    notify(title = 'Bottom limit hit',
                       subtitle = 'it is going down',
                       message = 'please pay attention to ' + arr[0] + ', it has hit bottom limit' + limit * -1 + " with value:" + arr[8])
                    notified = True
            elif float(limit) > 0 and float(arr[8]) - float(limit) > 0 :
                print('hit up limit:' + limit)

                if not notified:
                    notify(title='Up limite hit',
                           subtitle = 'it is going up',
                           message = 'please pay attention to ' + arr[0] + ', it has hit up limit ' + limit + ' with value ' + arr[8])
                    notified = True

            else:
                print('watching...')
                if notified:
                    notified = False

            linenum = linenum + 1

        sleep(1)

        # clear buffer#
        #  "\033[F" move one line up, '\r' move cursor back to beginning of line
        print("\033[F" * (linenum + 1) + '\r')

@cli.command()
@click.option('--code', '-c', help='code of futures product')
@click.option('--num', '-n', help='num of futures')
@click.option('--price', '-p', help='price of futures product')
def trade_product(code, num, price):
    Trade.trade(code, num, price)


@cli.command()
@click.option('--code', '-c', help='code of futures product')
@click.option('--stop', '-s', help='stop loss limit')
@click.option('--num', '-n', help='num of product to sell, positive number for stop profit, negative for stop loss')
def stop_order(code, stop, num):
    Stop.stop_order(code, stop, num)
    pass

if __name__ == '__main__':
    cli()
    pass

# The notifier function, https://stackoverflow.com/questions/17651017/python-post-osx-notification/17651702#17651702
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))
