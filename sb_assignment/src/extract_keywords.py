import re
from nltk import tokenize
from operator import itemgetter
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))

def check_sent(word, sentences): 
    final = [all([w in x for w in word]) for x in sentences] 
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    return result

def extract_major_keywords(text):
  total_words = text.split()
  total_word_length = len(total_words)
  total_sentences = tokenize.sent_tokenize(text)
  total_sent_len = len(total_sentences)

  tf_score = {}
  for each_word in total_words:
      each_word = each_word.replace(',','')
      each_word = each_word.replace("'","")
      if each_word not in stop_words:
          if each_word in tf_score:
              tf_score[each_word] += 1
          else:
              tf_score[each_word] = 1
  # Dividing by total_word_length for each dictionary element
  tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())

  idf_score = {}
  for each_word in total_words:
      each_word = re.sub(r'[^\w\s]', '', each_word)
      each_word = re.sub(r"'", '', each_word)
      each_word = re.sub(r'_', '', each_word)
      each_word = re.sub(r',', '', each_word)
      each_word = re.sub(" \d+", "", each_word)
      if each_word not in stop_words:
          if each_word in idf_score:
              idf_score[each_word] = check_sent(each_word, total_sentences)
          else:
              idf_score[each_word] = 1

  # Performing a log and divide
  idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())

  tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
  top_dict = get_top_n(tf_idf_score, 5)
  top_words = [k.lower()  for  k in  top_dict.keys() if len(k)>2] 
  top_words = set(top_words)
  red_words = {'the', 'techcrunch', 'for', 'since', 'from',
                'he', 'like', 'i', 'and', 'but', 'or', 'nor',
                'yet', 'so', 'he', 'she', 'it', 'they', 'them',
                'as', 'after', 'although', 'if', 'because', 'before',
                'than', 'till', 'when', 'with', 'without', 'of', 'on',
                'in', 'another'}
  top_keywords = top_words - red_words

  return top_keywords