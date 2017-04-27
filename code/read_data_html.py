from bs4 import BeautifulSoup
import requests
from time import sleep
import re
from collections import Counter
import matplotlib.pyplot as plt
import requests, json


#print len([td for td in tds if not is_video(td)])
# 21 for me, might be different for you


def prd_info(td):
    """given a BeautifulSoup <td> Tag representing a book,
    extract the book's details and return a dict"""
    #print td
    PrdName = td.find("div", "mytext_name").text
    Price = td.find("div", re.compile("^(mytext_cash_number)")).text
    #"^mytext_cash_number"
    #print td.find("div", re.compile("^(mytext_cash_number)")).text

    print "PrdName-----------",PrdName
    print "Price---------",Price

    return {
        "ProName" : PrdName,
        "Price" : Price
    }

base_url = "http://www.tkec.com.tw/product/201205benefits/index.aspx?page="

prd = []

NUM_PAGES = 3 # at the time of writing, probably more by now

for page_num in range(1, NUM_PAGES + 1):
    print "souping page", page_num, ",", len(prd), " found so far"
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')
    #print soup
    #soup.prettify()
    for my_name in soup('div', 'mypj_out_box'):
        prd.append(prd_info(my_name))
        #print my_name

# now be a good citizen and respect the robots.txt!
sleep(2)

print prd
print(len(prd))














#def get_year(book):
#    """book["date"] looks like 'November 2014' so we need to
#    split on the space and then take the second piece"""
#    return int(book["date"].split()[1])

# 2017 is the last complete year of data (when I ran this)
#year_counts = Counter(get_year(book) for book in books
#                if get_year(book) <= 2017)

#years = sorted(year_counts)
#book_counts = [year_counts[year] for year in years]

#plt.plot(years, book_counts)
#plt.ylabel("# of data books")
#plt.title("Data is Big!")
#plt.show()


