# -*- coding: utf-8-*-
import re
import feedparser


WORDS = ["NEWS"]

PRIORITY = 3



class Article:

    def __init__(self, title):
        self.title = title
        """self.URL = URL"""


def getTopArticles(maxResults=None):
    d = feedparser.parse("https://news.google.com/?output=rss")
    count = 0
    articles = []
    for item in d['items']:
        articles.append(Article(item['title'])) 
        count += 1
        if maxResults and count > maxResults:
            break

    return articles


def handle(mic):
	
    """
        Responds to user-input, typically speech text, with a summary of
        the day's top news headlines, sending them to the user over email
        if desired.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    
    mic.say("Pulling up the news")
    articles = getTopArticles(maxResults=3)
    titles = [" ".join(x.title.split(" - ")[:-1]) for x in articles]
    all_titles = "... ".join(str(idx + 1) + "  " + title for idx, title in enumerate(titles))
    print all_titles
   
    mic.say("Here are the current top headlines. " )
    mic.say(all_titles)


def isValid(text):
    """
        Returns True if the input is related to the news.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(news|headline)\b', text, re.IGNORECASE))
