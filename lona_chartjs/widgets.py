from lona.static_files import Script, SORT_ORDER
from lona.html import Node, Widget


class Canvas(Node):
    TAG_NAME = 'canvas'


class Chart(Widget):
    FRONTEND_WIDGET_CLASS = 'ChartjsChart'

    STATIC_FILES = [
        Script(
            name='chart.min.js',
            path='static/chart.min.js',
            url='chart.min.js',
            sort_order=SORT_ORDER.FRAMEWORK,
        ),
        Script(
            name='chart.js',
            path='static/chart.js',
            url='chart.js',
            sort_order=SORT_ORDER.FRAMEWORK,
            link=False,
        ),
        Script(
            name='chart-js-widgets.js',
            path='static/chartjs-widgets.js',
            url='chart-js-widgets.js',
            sort_order=SORT_ORDER.LIBRARY,
        ),
    ]

    def __init__(self, data=None, **kwargs):
        self.nodes = [
            Canvas(**kwargs),
        ]

        self.data = data or {}

    @property
    def width(self):
        return self.nodes[0].attributes.get('width', '')

    @width.setter
    def width(self, new_value):
        self.nodes[0].attributes['width'] = new_value

    @property
    def height(self):
        return self.nodes[0].attributes.get('height', '')

    @height.setter
    def height(self, new_value):
        self.nodes[0].attributes['height'] = new_value
