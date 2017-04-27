# coding=utf-8
from bs4 import BeautifulSoup
import requests
from time import sleep
import re
from collections import Counter
import matplotlib.pyplot as plt
import requests, json


#print len([td for td in tds if not is_video(td)])
# 21 for me, might be different for you

fig_price = []

def prd_info(td):
    """given a BeautifulSoup <td> Tag representing a book,
    extract the book's details and return a dict"""
    #print td
    PrdName = td.find("div", "mytext_name").text
    Price = td.find("div", re.compile("^(mytext_cash_number)")).text

    fig_price.append(Price)
    #print "PrdName-----------",PrdName
    #print "Price---------",Price
    #print "fig_name-------------",fig_price

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

#print prd
#print(len(prd))
print "----fig_price: ----" ,fig_price

test = int(fig_price[1]) + int(fig_price[2])
print "----test: ----",test











tran_int = []
one_th = 0
two_th = 0
three_th = 0
four_th = 0
mo_than_five_th = 0
for i in range(0, len(prd), 1):
    if int(fig_price[i]) < 1000 :
        one_th +=1
    elif (int(fig_price[i]) > 1000 and int(fig_price[i]) < 2000):
        two_th += 1
    elif (int(fig_price[i]) > 2000 and int(fig_price[i]) < 3000):
        three_th += 1
    elif (int(fig_price[i]) > 3000 and int(fig_price[i]) < 4000):
        four_th += 1
    else:
        mo_than_five_th += 1
    #print one_th


print "----one_th: ----",one_th
print "----two_th: ----",two_th
print "----three_th: ----",three_th
print "----four_th: ----",four_th
print "----mo_than_five_th: ----",mo_than_five_th


#print one_th
#print two_th

#print "----one_th: ----",one_th




price_q = [one_th,two_th,three_th,four_th,mo_than_five_th]
my_xticks = ['< 1000','1000 - 2000','2000 - 3000','3000 - 4000','> 4000']
num_num = [1,2,3,4,5]
plt.xticks(num_num, my_xticks)
plt.plot(num_num, price_q, color='green', marker='o', linestyle='solid')

# add a title
plt.title("Product data")
# add a label to the y-axis
plt.ylabel("Quantity")
# add a label to the x-axis
plt.xlabel("Price")
plt.show()



























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
