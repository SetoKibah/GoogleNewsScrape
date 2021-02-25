#from requests_html import HTMLSession
from pygooglenews import GoogleNews
from time import sleep

gn = GoogleNews()

# Function to get our search terms and parse the data
def get_titles(search):
  # Empty list to store acquired headlines
  stories = []

  # Grab our search term and generate list based on our parameters
  search = gn.search(search)
  newsitem = search['entries']
  for item in newsitem:
    story = {
        'title': item.title,
        'link': item.link
    }
    # Add our criteria to the list
    stories.append(story)

  # Print the list of headlines and links to be perused
  for section in stories:
    print(f"{section['title']}:\n{section['link']}\n")
    sleep(5)
  return

# Function call and keyword request
search = input('Enter keyword to search for: ')
get_titles(search)