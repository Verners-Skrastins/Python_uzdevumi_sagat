"""
Iegūt ziņas, izmantojot rss no google.lv.

"""

import feedparser


# jānorāda RSS plūsmas URL
rss_URL="https://news.google.com/rss"


#lejupialadet un izanalizet RSS plūsmu
feed=feedparser.parse(rss_URL)

#paradit zinu virsrakstus un saites

for entry in feed.entries:
    print('virsraksts:', entry.title)
    print("Saite", entry.link)
    print("\n")