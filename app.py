import justpy as jp
from data import avg_week, avg_month, avg_course_month, avg_day, rating_count
from charts import spline_chart, area_chart, pie_chart


def app():
    webpage = jp.QuasarPage()

    h1 = jp.QDiv(a=webpage, text='Analysis of Course Reviews',
                 classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=webpage, text='These graphs represent course review analysis',
                 classes='text-p text-center q-pa-md')

    # Chart for weekly average ratings
    hc1 = jp.HighCharts(a=webpage, options=spline_chart)
    hc1.options.title.text = "Average Ratings by Week"
    hc1.options.subtitle.text = "According to Course Review Dataset"
    hc1.options.xAxis.title.text = "Week"
    hc1.options.yAxis.title.text = "Average Rating"
    hc1.options.series[0].name = "Average Ratings by Week"
    avg_week_data = avg_week()
    hc1.options.series[0].data = list(avg_week_data['Rating'])
    hc1.options.xAxis.categories = list(avg_week_data.index)

    # Chart for monthly average ratings
    hc2 = jp.HighCharts(a=webpage, options=spline_chart)
    hc2.options.title.text = "Average Ratings by Month"
    hc2.options.subtitle.text = "According to Course Review Dataset"
    hc2.options.xAxis.title.text = "Month"
    hc2.options.yAxis.title.text = "Average Rating"
    hc2.options.series[0].name = "Average Ratings by Month"
    avg_month_data = avg_month()
    hc2.options.series[0].data = list(avg_month_data['Rating'])
    hc2.options.xAxis.categories = list(avg_month_data.index)

    # Chart for average ratings by course by month
    hc3 = jp.HighCharts(a=webpage, options=area_chart)
    hc3.options.title.text = "Average Ratings by Month"
    hc3.options.subtitle.text = "According to Course Review Dataset"
    hc3.options.xAxis.title.text = "Month"
    hc3.options.yAxis.title.text = "Average Rating"
    avg_course_month_data = avg_course_month()
    data = []

    for i in range(len(avg_course_month_data.columns)):
        cl_name = avg_course_month_data.columns[i]
        temp = {
            "name": cl_name,
            "data": [item for item in avg_course_month_data[cl_name]]
        }
        data.append(temp)

    hc3.options.series = data
    hc3.options.xAxis.categories = list(avg_course_month_data.index)

    # Chart for aggregated average ratings by day of the week
    hc4 = jp.HighCharts(a=webpage, options=spline_chart)
    hc4.options.title.text = "Aggregated Average Ratings by Day of the Week"
    hc4.options.subtitle.text = "According to Course Review Dataset"
    hc4.options.xAxis.title.text = "Day"
    hc4.options.yAxis.title.text = "Average Rating"
    hc4.options.series[0].name = "Average Ratings by Day"
    avg_day_data = avg_day()
    hc4.options.series[0].data = list(avg_day_data['Rating'])
    hc4.options.xAxis.categories = list(avg_day_data.index.get_level_values(0))

    # Pie chart showing the count of ratings of different courses
    hc5 = jp.HighCharts(a=webpage, options=pie_chart)
    hc5.options.title.text = "Percentage of rating by course"
    hc5.options.subtitle.text = "According to Course Review Dataset"
    share = rating_count()
    hc5.options.series[0].name = "Course"
    pie_data = []
    for i in range(len(share.index)):
        c_name = share.index[i]
        temp = {
            "name": c_name,
            "y": int(share[c_name])
        }
        pie_data.append(temp)
    hc5.options.series[0].data = pie_data
    return webpage


jp.justpy(app)
