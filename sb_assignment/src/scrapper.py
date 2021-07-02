import re
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from urllib.request import urlopen

def cleanUpTweet(txt):
  # Remove mentions
  # txt = txt.lower()
  txt = re.sub(r'@[A-Za-z0-9_]+', '', txt)
  # Remove hashtags
  txt = re.sub(r'\n', '', txt)
  # Remove urls
  txt = re.sub(r'https?:\/\/[A-Za-z0-9\.\/]+', '', txt)
  regrex_pattern = re.compile(pattern = "["
      u"\U0001F600-\U0001F64F"  # emoticons
      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
      u"\U0001F680-\U0001F6FF"  # transport & map symbols
      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
      u"\xa0"
                      "]+", flags = re.UNICODE)
  txt = regrex_pattern.sub(r'',txt)
  return txt

def get_date_posted(day):
    current_date = datetime.now()
    try:
        day_split = [d.split(' ') for d in day]
        day_num = day_split[0][0]
        day_unit = day_split[0][1]
        day_num = int(day_split[0][0])
        if day_unit == 'hours':
            posted_date = current_date.date()
        else:
            posted_date =  current_date - timedelta(days=day_num)
            posted_date = posted_date.date()
    except:
        posted_date = None
    return posted_date

def extract_data(url):
  extracted_data = {}
  page = urlopen(url)
  html = page.read().decode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  title = soup.title.string
  title =  title.replace("– TechCrunch", "")
  extracted_data['title'] = title
  all_para = soup.find_all("p")
  para_list = [p.text for p in all_para]
  text = " ".join(para_list)
  processed_text = cleanUpTweet(text)
  extracted_data['text'] = processed_text
  authors = soup.find('div', attrs={'class':'article__byline'}).find_all('a')
  author = [author.text for author in authors]
  author = [re.sub('\n+', '', s) for s in author] 
  author = [re.sub('\t+', '', s) for s in author] 
  author_list = [auth for auth in author if  not auth.startswith("@")]
  extracted_data['authors'] = author_list
  date_span = soup.find('div', attrs={'class':'article__byline'}).find_all('span')
  day = [i.text for i in date_span]
  day = [re.sub('\n+', '', s) for s in day] 
  day = [re.sub('\t+', '', s) for s in day] 
  day = [re.sub('[/]', '', s) for s in day]
  day = [re.sub(r"\@\w+", "", s) for s in day]
  day = [s.strip(' ') for s in day]
  day = [s for s in day if s]
  posted_date = get_date_posted(day)
  extracted_data['date_posted'] = posted_date
  return extracted_data