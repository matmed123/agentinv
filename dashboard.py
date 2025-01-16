from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtChart import QChart, QChartView
from widgets.portfolio_summary import PortfolioSummaryWidget
from widgets.market_chart import MarketChartWidget


class Dashboard(QWidget):
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager
        self.setup_ui()
    def setup_ui(self):
        layout = QGridLayout(self)
        
        # Add portfolio summary widget
        portfolio_summary = PortfolioSummaryWidget(self.data_manager)
        layout.addWidget(portfolio_summary, 0, 0)
        
        # Add market chart widget
        market_chart = MarketChartWidget(self.data_manager)
        layout.addWidget(market_chart, 0, 1, 2, 1)
