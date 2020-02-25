import matplotlib.pyplot as plt 
import datetime as dt
import dateutil
import matplotlib.dates as mdates 

def plot_date_vs_news_count_on_dengue(date_wise_news):

    matlab_dates = [mdates.datestr2num(dateutil.parser.parse(date).strftime('%Y-%m-%d')) for date in date_wise_news.keys()]
    y = [val for val in date_wise_news.values()]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
    plt.scatter(matlab_dates,y)
    plt.ylabel('News Count')
    plt.xlabel('Days')
    plt.gcf().autofmt_xdate()
    plt.show()