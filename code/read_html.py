from bs4 import BeautifulSoup
import requests
from time import sleep
import re
from collections import Counter
import matplotlib.pyplot as plt
import requests, json


def is_video(td):
 """it's a video if it has exactly one pricelabel, and if
 the stripped text inside that pricelabel starts with 'Video'"""
 pricelabels = td('span', 'pricelabel')
 return (len(pricelabels) == 1 and
         pricelabels[0].text.strip().startswith("Video"))


#print len([td for td in tds if not is_video(td)])
# 21 for me, might be different for you


def book_info(td):
    """given a BeautifulSoup <td> Tag representing a book,
    extract the book's details and return a dict"""

    #print "td-----",td

    title = td.find("div", "thumbheader").a.text
    by_author = td.find('div', 'AuthorName').text
    authors = [x.strip() for x in re.sub("^By ", "", by_author).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0]
    date = td.find("span", "directorydate").text.strip()

    #print "title-----------",title

    return {
        "title" : title,
        "authors" : authors,
        "isbn" : isbn,
        "date" : date
    }

base_url = "http://shop.oreilly.com/category/browse-subjects/" + \
 "data.do?sortby=publicationDate&page="

books = []

NUM_PAGES = 2 # at the time of writing, probably more by now

for page_num in range(1, NUM_PAGES + 1):
    print "souping page", page_num, ",", len(books), " found so far"
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')

    for td in soup('td', 'thumbtext'):
        if not is_video(td):
            books.append(book_info(td))
            #print "td-----",td
# now be a good citizen and respect the robots.txt!
sleep(2)

print books
print(len(books))

def get_year(book):
    """book["date"] looks like 'November 2014' so we need to
    split on the space and then take the second piece"""
    return int(book["date"].split()[1])

# 2017 is the last complete year of data (when I ran this)
year_counts = Counter(get_year(book) for book in books
                if get_year(book) <= 2017)

years = sorted(year_counts)
book_counts = [year_counts[year] for year in years]
plt.plot(years, book_counts)
plt.ylabel("# of data books")
plt.title("Data is Big!")
plt.show()

endpoint = "https://api.github.com/users/Leechengche/repos"
repos = json.loads(requests.get(endpoint).text)

for rows in repos:
    data_print = rows["name"]

print data_print
