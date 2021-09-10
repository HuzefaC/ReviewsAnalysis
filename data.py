import pandas as pd
from datetime import datetime
from pytz import utc


def load_data():
    return pd.read_csv("reviews.csv", parse_dates=['Timestamp'])


def avg_week():
    reviews_data = load_data()
    reviews_data['Week'] = reviews_data['Timestamp'].dt.strftime('%Y-%U')
    avg_ratings_week = reviews_data.groupby(['Week']).mean()
    return avg_ratings_week


def avg_month():
    reviews_data = load_data()
    reviews_data['Month'] = reviews_data['Timestamp'].dt.strftime('%Y-%m')
    avg_ratings_month = reviews_data.groupby(['Month']).mean()
    return avg_ratings_month


def avg_course_month():
    reviews_data = load_data()
    reviews_data['Month'] = reviews_data['Timestamp'].dt.strftime('%Y-%m')
    month_average_crs = reviews_data.groupby(['Month', 'Course Name'])[
        'Rating'].mean().unstack()
    return month_average_crs


def avg_day():
    reviews_data = load_data()
    reviews_data['Week_Day'] = reviews_data['Timestamp'].dt.strftime('%A')
    reviews_data['Day_Num'] = reviews_data['Timestamp'].dt.strftime('%w')
    day_wise_avg_rating = reviews_data.groupby(
        ['Week_Day', 'Day_Num']).mean().sort_values('Day_Num')
    return day_wise_avg_rating


def rating_count():
    reviews_data = load_data()
    rating_share = reviews_data.groupby(['Course Name'])['Rating'].count()
    return rating_share
