import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis, QCategoryAxis
from PySide6.QtGui import QColor, QPen, QPainter

class ModernGraphWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modern UI Graph")
        self.setGeometry(100, 100, 800, 600)
        
        # Create layout
        layout = QVBoxLayout()

        # Create a chart view
        self.chart_view = QChartView(self.create_chart())
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Add chart to the layout
        layout.addWidget(self.chart_view)
        self.setLayout(layout)

        # Set dark theme background
        self.setStyleSheet("background-color: #2c3e50;")

    def create_chart(self):
        # Create a chart
        chart = QChart()
        chart.setTitle("Sales Over Time")
        chart.setTitleBrush(Qt.white)
        chart.setBackgroundBrush(QColor("#2c3e50"))
        
        # Create a series of data
        series = QLineSeries()
        
        # Add data points with tooltips
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
        data_points = [
            (0, 10), (1, 15), (2, 30),
            (3, 40), (4, 60), (5, 50),
            (6, 80)
        ]
        
        for x, y in data_points:
            series.append(x, y)
        
        # Customize series appearance
        pen = QPen(QColor("#1abc9c"))
        pen.setWidth(3)
        series.setPen(pen)
        
        # Add series to chart
        chart.addSeries(series)

        # Create and customize axes
        axisX = QCategoryAxis()
        axisX.setTitleText("Months")
        axisX.setTitleBrush(Qt.white)
        axisX.setLabelsColor(Qt.white)
        axisX.setGridLineColor(QColor("#34495e"))
        
        # Add categories for months
        for i, month in enumerate(months):
            axisX.append(month, i + 0.5)
        
        axisX.setRange(0, 7)
        
        axisY = QValueAxis()
        axisY.setTitleText("Sales Amount")
        axisY.setTitleBrush(Qt.white)
        axisY.setLabelsColor(Qt.white)
        axisY.setGridLineColor(QColor("#34495e"))
        
        chart.setAxisX(axisX, series)
        chart.setAxisY(axisY, series)
        
        # Remove legend as we only have one series
        chart.legend().hide()
        
        return chart

    def setChartStyle(self):
        # This method is no longer needed as styling is handled directly in create_chart
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = ModernGraphWidget()
    window.show()
    
    sys.exit(app.exec())
