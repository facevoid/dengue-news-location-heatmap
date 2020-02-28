import requests
import csv
import pandas as pd

def get_count_from_solr_data(query):
    url = 'http://pipilika.com:33133/solr/main_search/select?defType=edismax&fl=domain&fq=other_category: news AND update_date:[2005-01-01T00:00:00.000Z TO 2020-12-31T23:59:00.000Z]&mm=100&q=' + query + '&qf=content^1.0&rows=6429210'
    print(url)
    response = requests.get(url).json()
            # print(response)
    response = response['response']
    print('count ', response['numFound'])
    return response['numFound']

df = pd.read_csv('data_for_heatmap/district_wise_dengue_news_count_all_with_location.csv')
news_count = []

location_news_count_dict = {}
for location_name in list(df['location_name']):
    count = get_count_from_solr_data('ইয়াবা {}'.format(location_name.strip()))
    news_count.append(count)

df['count'] = news_count

with open('data_for_heatmap/yaba_news_bd_district_wise.csv', 'w') as fp:
    df.to_csv(fp, encoding='utf-8', index=False)

location_news_count_dict_sorted = {k: v for k, v in sorted(location_news_count_dict.items(), key=lambda item: item[1], reverse = True)}



with open('data_for_heatmap/yaba_news_location_wise_district_wise.csv', 'w') as fp:
    writer = csv.writer(fp)
    writer.writerow(['location_name', 'lat', 'long', 'count'])
    for key, val in location_news_count_dict_sorted.items():
        writer.writerow([key, '', '', val])