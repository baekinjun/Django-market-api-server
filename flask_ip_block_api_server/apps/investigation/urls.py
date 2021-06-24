from .view import *

url_patterns = [
    (WordCloudView, '/word_cloud'),
    (SearchChartView, '/search_chart_view'),
    (MaltegoInView, '/maltego_in'),
    (MaltegoOutView, '/maltego_out')
]
