from collections import Counter
import math, random, csv, json


def get_domain(email_address):
 """split on '@' and return the last piece"""
 return email_address.lower().split("@")[-1]
with open('email.txt', 'r') as f:
 domain_counts = Counter(get_domain(line.strip())
 for line in f
 if "@" in line)

 print domain_counts


def process(date, symbol, price):
    print date, symbol, price



print ""
print "tab delimited stock prices:"

with open('tab_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)

print

print "colon delimited stock prices:"
with open('colon_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date, symbol, closing_price)

print


print "writing out comma_delimited_stock_prices.txt"

today_prices = { 'Chinese' : 90.5, 'English' : 41.68, 'Math' : 64.5 }

with open('comma_delimited_stock_prices.txt','wb') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])

print "writing out tab_delimited_stock_prices.txt"

today_prices = { 'Chinese' : 90.5, 'English' : 41.68, 'Math' : 64.5 }

with open('tab_delimited_stock_prices.txt','wb') as f:
    writer = csv.writer(f, delimiter='\t')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])




