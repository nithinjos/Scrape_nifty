from bs4 import BeautifulSoup
import redis
from selenium import webdriver

redis_inst = redis.StrictRedis(host='localhost', port=6379, db=0)
PHANTOMJS_PATH = './phantomjs'
url = "http://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G"
browser = webdriver.PhantomJS(PHANTOMJS_PATH)



keys = [
    'LTP',
    '%change',
    'TradedQty',
    'Value(inLakhs)',
    'Open',
    'High',
    'Low',
    'Prev.close',
    'LatestExDate']


def nScrape():

    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    table_gainers = soup.find_all('table')
    rows_g = table_gainers[0].find_all('tr')[1:]
    print("thread running")
    
    for row in rows_g:
        cols = row.find_all('td')
        entry = 'entry ' + str(rows_g.index(row))
        redis_inst.hset(entry, 'Symbol', cols[0].get_text())
        redis_inst.hset(entry, 'LTP', cols[1].get_text())
        redis_inst.hset(entry, '%change', cols[2].get_text())
        redis_inst.hset(entry, 'TradedQty', cols[3].get_text())
        redis_inst.hset(entry, 'Value(inLakhs)', cols[4].get_text())
        redis_inst.hset(entry, 'Open', cols[5].get_text())
        redis_inst.hset(entry, 'High', cols[6].get_text())
        redis_inst.hset(entry, 'Low', cols[7].get_text())
        redis_inst.hset(entry, 'Prev.close', cols[8].get_text())
        redis_inst.hset(entry, 'LatestExDate', cols[9].get_text())
        redis_inst.hset(entry, 'CA', cols[10].get_text())
    
    

