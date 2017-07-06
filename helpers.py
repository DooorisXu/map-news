import feedparser
import urllib.parse

def lookup(geo):
    """Looks up articles for geo."""

    # check cache for geo
    # getting geo from cache instead of the server--for the sake of speed and use--temporarily stored 
    if geo in lookup.cache:
        return lookup.cache[geo]

    # get feed from Google
    # parses the Google feed (which is in RSS)
    
    feed = feedparser.parse("http://news.google.com/news?geo={}&output=rss".format(urllib.parse.quote(geo, safe="")))
    print(type(feed))
    
    # if no items in feed, get feed from Onion
    # feed is a dict 
    if not feed["items"]:
        # get something from Onion if there is no serious news from Google
        # feedparser parse the RSS we get from Google 
        feed = feedparser.parse("http://www.theonion.com/feeds/rss")

    # cache results
    # lookup things in the dict, and return an array 
    # use a for loop here 
    lookup.cache[geo] = [{"link": item["link"], "title": item["title"]} for item in feed["items"]]

    # return results
    return lookup.cache[geo]

# initialize cache
lookup.cache = {}
