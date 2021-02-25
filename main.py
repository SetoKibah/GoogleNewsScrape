from requests_html import HTMLSession
from pygooglenews import GoogleNews

# Interesting tool that might be helpful to use https://github.com/kotartemiy/pygooglenews

# Testing template given on the github page
gn = GoogleNews()

search = gn.search('lockdown')

for item in search['entries']:
  print(item['title'])

# Template is clean and works well, will further improve


"""
url = 'https://news.google.com/rss/search?q=lockdown'

# Create our session
s = HTMLSession()

# Get the specified url
r = s.get(url)

# Testing title acquisition.
for title in r.html.find('title'):
  print(title.text)
  """