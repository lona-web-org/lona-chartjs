function ChartjsChart(lona_window) {
    this.lona_window = lona_window;

    this.setup = function() {
        var lona_window = this.lona_window;

        this.canvas = this.nodes[0];
        this.ctx = this.canvas.getContext('2d');
        this.chart = new Chart(this.ctx, this.data);
    };

    this.data_updated = function() {
        this.chart.data = this.data.data;
        this.chart.update();
    };
};

Lona.register_widget_class('ChartjsChart', ChartjsChart);
