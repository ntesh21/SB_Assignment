import spacy
NER = spacy.load("en_core_web_sm")



def extract_ner(text):
  extracted_ner = {}
  ner_text= NER(text)
  name = {word.text for word in ner_text.ents if word.label_ == 'PERSON'}
  extracted_ner['name'] = name
  org = {word.text for word in ner_text.ents if word.label_ == 'ORG'}
  extracted_ner['organization'] = org
  dates = {word.text for word in ner_text.ents if word.label_ == 'DATE'}
  extracted_ner['dates'] = dates
  products = {word.text for word in ner_text.ents if word.label_ == 'PRODUCT'}
  extracted_ner['products'] = products
  countries = {word.text for word in ner_text.ents if word.label_ == 'GPE'}
  extracted_ner['countries'] = countries
  locations = {word.text for word in ner_text.ents if word.label_ == 'LOC'}
  extracted_ner['locations'] = locations
  monetary_values = {word.text for word in ner_text.ents if word.label_ == 'MONEY'}
  extracted_ner['money'] = monetary_values
  percentile = {word.text for word in ner_text.ents if word.label_ == 'PERCENT'}
  extracted_ner['percentile'] = percentile
  all_ners = {word.text for word in ner_text.ents}
  sent_list = text.split('.')
  summary_list = [[sent for sent in sent_list if ner in sent] for ner in all_ners]
  summary_list = [sent for sent in summary_list if sent]
  summary_list = [sent[0] for sent in summary_list]
  summary_list = set(summary_list)
  summary_list = list(summary_list)[:5]
  summary_text = '.'.join(summary_list)
  extracted_ner['summary'] = summary_text
  return extracted_ner