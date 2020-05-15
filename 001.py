import tushare as ts

ts.set_token('e82c8fe9f87fb4dbd37d45a035151bdd61a1f1a592d56c2584c82d52')
# df=ts.get_hist_data('600848')
# df=ts.guba_sina()
# df=ts.lpr_data(2020)
# df=ts.top_list('2020-05-12')
# df=ts.get_hist_data('600104',start='2017-03-01',end='2017-03-31')
# df=ts.inst_detail()

# dflist=df.values.tolist()
# df=ts.cap_tops()
# df=ts.fund_holdings(2020, 1)
# df=ts.sh_margins(start='2020-01-01', end='2020-04-19')
df=ts.get_stock_basics()
df.to_excel("05.xlsx")


# print(dflist)

# pro=ts.pro_api()
# # df = pro.daily(daily_basic='20200325')
# df = pro.stock_basic()


print(df)
# df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')