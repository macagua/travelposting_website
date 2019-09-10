from djmoney.forms import MoneyWidget


class BootstrapMoneyWidget(MoneyWidget):
    template_name = 'widgets/money_widget.html'
