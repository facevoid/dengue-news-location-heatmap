import matplotlib.pyplot as plt 
import datetime as dt
import dateutil
import matplotlib.dates as mdates 
from datetime import datetime 


def plot_date_vs_news_count_on_dengue(date_wise_news, file_name_to_save=None):
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

    if file_name_to_save is not None:
        plt.savefig('plots/{}.png'.format(file_name_to_save))
    plt.show()

def plot_bar_chart(X, y, xlabel, ylabel, file_name_to_save=None):


    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111)
    ax.bar(X, y)

    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=70)
    plt.tight_layout()
    if file_name_to_save is not None:
        plt.savefig('plots/{}.png'.format(file_name_to_save))
    plt.show()


def plot_bar_chart_unicode_text(X, y, xlabel, ylabel):
    import matplotlib.font_manager as fm
    prop = fm.FontProperties(fname='kalpurush.ttf')
    ticks_font = fm.FontProperties(family='Helvetica', style='normal',
    size=12, weight='normal', stretch='normal')

    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111)
    ax.bar(X, y)
    ax.xaxis.get_label().set_fontproperties(ticks_font)
    # for label in (ax.get_xticklabels()):
    #     label.set_fontproperties(prop)

    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=70)
    plt.tight_layout()
    plt.show()