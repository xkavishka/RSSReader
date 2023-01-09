import feedparser

# Replace `url` with the URL of the RSS feed you want to read
url = 'http://feeds.example.com/rss'

# Parse the RSS feed
feed = feedparser.parse(url)

# Print out the titles of the articles in the feed
for entry in feed.entries:
    print(entry.title)
