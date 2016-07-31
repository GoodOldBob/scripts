# for all my simple RSS needs on the CLI
import feedparser

MANGASTREAM_RSS_URL = "http://mangastream.com/rss"
MANGAFOX_LOOKISM_RSS_URL = "http://mangafox.me/rss/lookism.xml"

def get_mangastream():
    feed = feedparser.parse(MANGASTREAM_RSS_URL)
    entries = []

    for entry in feed.entries:
        title_and_date = [entry.title, entry.published]
        entries.append(title_and_date)

    # print out entries with the most recent output last
    entries.reverse()
    print("MANGASTREAM:\n-------------------------------")
    for entry in entries:
        print(entry[0] + "\n" + entry[1] + "\n")

def get_lookism():
    # gimme the last two chapters
    feed = feedparser.parse(MANGAFOX_LOOKISM_RSS_URL)
    print("LOOKISM:\n-------------------------------")
    counter = 0
    for entry in feed.entries:
        if counter > 1:
            break
        print(entry.title + "\n" + entry.published + "\n")
        counter = counter + 1

def main():
    get_mangastream()
    get_lookism()

if __name__ == "__main__":
    main()
