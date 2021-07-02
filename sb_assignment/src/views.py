from django.shortcuts import render
from django.http import HttpResponse
import json
import re
from datetime import datetime, timedelta
from dateutil import parser
from src.scrapper import extract_data
from src.extract_keywords import extract_major_keywords
from src.extract_ner import extract_ner
from src.models import Content
   
# create a function

def format_list_string(txt):
  txt = re.sub(r'"', '', txt)
  # txt = re.sub(r'[', '', txt)
  txt = re.sub(r']', '', txt)
  txt = txt[1:]
  txt_list = txt.split(',')
  return txt_list


def index(request):
    cxt = {"data_filled":"no", "message":""}
    try:
        if request.method == 'POST':
            url = request.POST.get('url')
            extracted_data = extract_data(url)
            title  = extracted_data['title']
            text = extracted_data['text']
            cxt_author = extracted_data['authors']
            author = json.dumps(cxt_author)
            date_posted = extracted_data['date_posted']
            formatted_date_posted = date_posted.strftime("%d %B, %Y")
            cxt_keywords = list(extract_major_keywords(text))
            top_keywords = json.dumps(cxt_keywords)
            extracted_ner = extract_ner(text)
            cxt_names = list(extracted_ner['name'])
            names = json.dumps(cxt_names)
            cxt_org = list(extracted_ner['organization'])
            org =json.dumps(cxt_org)
            cxt_dates = list(extracted_ner['dates'])
            dates = json.dumps(cxt_dates)
            cxt_products = list(extracted_ner['products'])
            products = json.dumps(cxt_products)
            cxt_countries = list(extracted_ner['countries'])
            countries = json.dumps(cxt_countries)
            cxt_locations = list(extracted_ner['locations'])
            locations = json.dumps(cxt_locations)
            cxt_money = list(extracted_ner['money'])
            monatery_values = json.dumps(cxt_money)
            cxt_percentile = list(extracted_ner['percentile'])
            percentile = json.dumps(cxt_percentile)
            summary = extracted_ner['summary']
            cxt = {'url':url, 'title':title, 'text':text, 'author':cxt_author, 'date_posted':formatted_date_posted, 
                    'keywords':cxt_keywords, "names":cxt_names, "organizations":cxt_org, "dates":cxt_dates, 
                    "products":cxt_products, "countries":cxt_countries, "locations":cxt_locations, 
                    "money":cxt_money, "percentile":cxt_percentile, "summary":summary, "data_filled":"yes"}
            
            data_present = Content.objects.filter(url=url).exists()
            if data_present is True:
                cxt['data_saved'] = 'true'
    except (ValueError, AttributeError):
            cxt["err_msg"] = "wrong"


    return render(request, "index.html", cxt)

def list_data(request):
    data = Content.objects.all()
    return render(request, "data-list.html", {"data":data})

def data_detail(request, id):
    data = Content.objects.get(id=id)
    author = format_list_string(data.author)
    date_posted = data.posted_on.strftime("%d %B, %Y")
    keywords = format_list_string(data.keywords)
    names = format_list_string(data.names)
    organizations = format_list_string(data.organization)
    dates = format_list_string(data.dates)
    products = format_list_string(data.products)
    countries = format_list_string(data.countries)
    locations= format_list_string(data.locations)
    money = format_list_string(data.money)
    percentile = format_list_string(data.percentile)
    return render(request, "data-details.html", {"data":data, "author":author, 
                    "keywords":keywords, "date_posted":date_posted, "names":names,
                    "organizations":organizations, "dates":dates, "products":products,
                    "countries":countries, "locations":locations, "money":money,
                    "percentile":percentile})

def save_db(request):
    if request.method == 'POST':
        url = request.POST['url']
        title = request.POST['title']
        text = request.POST['text']
        author = format_list_string(request.POST['author'])
        author = [re.sub(r'&#x27;', '', item) for item in author]
        date_posted =  request.POST['posted_on']
        form_date = parser.parse(date_posted)
        posted_on = form_date.date()
        keywords = format_list_string(request.POST['keywords'])
        keywords = [re.sub(r'&#x27;', '', item) for item in keywords]
        names = format_list_string(request.POST['names'])
        names = [re.sub(r'&#x27;', '', item) for item in names]
        organization = format_list_string(request.POST['organization'])
        organization = [re.sub(r'&#x27;', '', item) for item in organization]
        dates = format_list_string(request.POST['dates'])
        dates = [re.sub(r'&#x27;', '', item) for item in dates]
        products = format_list_string(request.POST['products'])
        products = [re.sub(r'&#x27;', '', item) for item in products]
        countries = format_list_string(request.POST['countries'])
        countries = [re.sub(r'&#x27;', '', item) for item in countries]
        locations = format_list_string(request.POST['locations'])
        locations = [re.sub(r'&#x27;', '', item) for item in locations]
        money = format_list_string(request.POST['money'])
        money = [re.sub(r'&#x27;', '', item) for item in money]
        percentile = format_list_string(request.POST['percentile'])
        percentile = [re.sub(r'&#x27;', '', item) for item in percentile]
        summary = request.POST['summary']
        p = Content(url=url, title=title, text=text, author=author, posted_on=posted_on, keywords=keywords,
                        names=names, organization=organization, dates=dates, products=products, countries=countries,
                        locations=locations, money=money, percentile=percentile, summary=summary)
        try:
            p.save()
            message = "Success"
        except:
            message = "Failed"
    return HttpResponse(message)