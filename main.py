from requests_html import HTMLSession

url = 'https://news.google.com/rss/search?q=lockdown'

# Create our session
s = HTMLSession()

# Get the specified url
r = s.get(url)

# Testing title acquisition.
for title in r.html.find('title'):
  print(title.text)