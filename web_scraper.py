import requests
from bs4 import BeautifulSoup
import pprint
x=1
y=int(input ("enter number of pages you want to scrape :"))
mega_links=[]
mega_subtext=[]
for x in range(1,y+1):
  if x==1:
    res = requests.get('https://news.ycombinator.com/news')
  else:
    res = requests.get('https://news.ycombinator.com/news?p='+str(x))
  soup = BeautifulSoup(res.text, 'html.parser')
  link = soup.select('.storylink')
  substext = soup.select('.subtext')
  mega_links=mega_links+link
  mega_subtext=mega_subtext+substext

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)
 
pprint.pprint(create_custom_hn(mega_links,mega_subtext))
