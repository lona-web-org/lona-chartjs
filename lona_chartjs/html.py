from lona.static_files import Script, SORT_ORDER
from lona.html import Node


class Chart(Node):
    TAG_NAME = 'canvas'
    WIDGET = 'ChartjsChart'

    STATIC_FILES = [
        Script(
            name='chart.min.js',
            path='static/lona-chartjs/dist/chart.min.js',
            url='chart.min.js',
            sort_order=SORT_ORDER.FRAMEWORK,
        ),
        Script(
            name='chart.js',
            path='static/lona-chartjs/dist/chart.js',
            url='chart.js',
            sort_order=SORT_ORDER.FRAMEWORK,
            link=False,
        ),
        Script(
            name='chart-js-widgets.js',
            path='static/lona-chartjs/chartjs-widgets.js',
            url='chart-js-widgets.js',
            sort_order=SORT_ORDER.LIBRARY,
        ),
    ]

    def __init__(self, data=None, width=None, height=None):
        super().__init__()

        if data:
            self.data = data

        if width:
            self.width = width

        if height:
            self.height = height

    # data
    @property
    def data(self):
        return self.widget_data

    @data.setter
    def data(self, new_data):
        self.widget_data = new_data

    # width
    @property
    def width(self):
        return self.attributes.get('width', '')

    @width.setter
    def width(self, new_value):
        self.attributes['width'] = new_value

    # height
    @property
    def height(self):
        return self.attributes.get('height', '')

    @height.setter
    def height(self, new_value):
        self.attributes['height'] = new_value
