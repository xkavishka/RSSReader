import feedparser

while True:
    # Prompt the user to enter the URL of the RSS feed
    url = input('Enter the URL of the RSS feed/press Q to quit): ')

    # Check if the user pressed q to exit
    if url.lower() == 'q':
        break

    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Print out a banner
    print('\033[92m' + '''
    RSS FEED READER BY @XKAVISHKA
    ''' + '\033[0m')

    # Print out the titles of the articles in the feed
    for entry in feed.entries:
        print('\033[95m' + '-' * 20)
        print('\033[94m' + entry.title + '\033[0m')
        print('\033[95m' + '-' * 20)

    # Replace `url` with the URL of the RSS feed you want to read
    url = 'http://feeds.example.com/rss'

    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Print out the titles of the articles in the feed
    for entry in feed.entries:
        print(entry.title)
