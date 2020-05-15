import urllib.request
#code代码
#scale表示的是时间长度 以分钟为基本单位，输入240就表示下载日K线数据;60就是小时K线数据
#datalen 则是获取数据的条数，在日K线的时间长度了，datalen就是获取60天日K数据

# links = 'http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/var=/CN_MarketData.getKLineData?symbol=' + code + '&scale=' + str(scale) + '&ma=no&datalen='+str(datalen)
# links = 'http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/var=/CN_MarketData.getKLineData?symbol=' + code + '&scale=' + str(scale) + '&ma=no&datalen='+str(datalen)


#http://market.finance.sina.com.cn/pricehis.php?symbol=sz000001&startdate=20200101&enddate=20200131
def get_stock_price(stock):
    str_links="""
        http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/var=/CN_MarketData.getKLineData?symbol={0}&scale={1}&ma=no&datalen={2}
    """

    str_links=str_links.format(stock['symbol'],stock['scale'],stock['datalen'])


    histData = urllib.request.urlopen(str_links).read()
    histData = str(histData).split('[')[1]
    histData = histData[1:len(histData) - 4].split('},{')
    datas = []
    for i in range(0, len(histData)):
        column = {}
        dayData = histData[i].split(',')
        for j in range(0, len(dayData)):
           field = dayData[j].split(':"')
           if field[0] == 'day':
              column['date'] = field[1].replace('"', '')
           else:
              column[field[0]] = field[1].replace('"', '')
        datas.append(column)
    return datas


stock={
    'symbol':'sz000001',
    'scale':5,
    'datalen':10,

}

dt=get_stock_price(stock)
print(dt)