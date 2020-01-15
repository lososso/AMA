import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QComboBox, QGroupBox, QRadioButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.product_groupbox = QGroupBox('Product GroupBox')
        self.information_groupbox = QGroupBox('Information Groupbox')
        self.initui()
        self.widgets_definition()

    def initui(self):
        self.setWindowTitle('AMA stock & management V0.1')
        self.show()
        self.showMaximized()

    def widgets_definition(self):
        self.main_layout.addWidget(self.product_groupbox, 0, 0)
        self.main_layout.addWidget(self.information_groupbox, 0, 1)
        self.setLayout(self.main_layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
