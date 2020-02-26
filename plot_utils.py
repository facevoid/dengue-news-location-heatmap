import matplotlib.pyplot as plt 
import datetime as dt
import dateutil
import matplotlib.dates as mdates 
from datetime import datetime 


def plot_date_vs_news_count_on_dengue(date_wise_news):
    dates = list(date_wise_news.keys())
    dates.sort(key = lambda date: datetime.strptime(date, '%Y-%m-%d'))
    matlab_dates = [mdates.datestr2num(dateutil.parser.parse(date).strftime('%Y-%m-%d')) for date in dates]
    y = [date_wise_news[date] for date in dates]

    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
    ax.plot(matlab_dates, y, marker='o')
    plt.ylabel('News Count')
    plt.xlabel('Days')
    plt.xticks(rotation=70)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()

def plot_bar_chart(X, y, xlabel, ylabel):


    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111)
    ax.bar(X, y)

    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=70)
    plt.tight_layout()
    plt.show()
