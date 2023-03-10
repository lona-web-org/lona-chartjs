class ChartjsChart{
    constructor(lona_window) {
        this.lona_window = lona_window;
    }

    setup() {
        this.canvas = this.root_node;
        this.ctx = this.canvas.getContext('2d');
        this.chart = new Chart(this.ctx, this.data);
    }

    data_updated() {
        this.chart.data = this.data;
        this.chart.update();
    }

    deconstruct() {
        this.chart.destroy();
    }
}


Lona.register_widget_class('ChartjsChart', ChartjsChart);
