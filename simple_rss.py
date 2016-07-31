# for all my simple RSS needs on the CLI
import feedparser

mangastream_rss_url = "http://mangastream.com/rss"
mangafox_lookism_rss_url = "http://mangafox.me/rss/lookism.xml"

feed = feedparser.parse(mangastream_rss_url)
entries = []

for entry in feed.entries:
    title_and_date = [entry.title, entry.published]
    entries.append(title_and_date)

# print out entries with the most recent output last
entries.reverse()
print("MANGASTREAM:\n-------------------------------")
for entry in entries:
    print(entry[0] + "\n" + entry[1] + "\n")

# gimme the last two chapters
feed = feedparser.parse(mangafox_lookism_rss_url)
print("LOOKISM:\n-------------------------------")
counter = 0
for entry in feed.entries:
    if counter > 1:
        break
    print(entry.title + "\n" + entry.published + "\n")
    counter = counter + 1