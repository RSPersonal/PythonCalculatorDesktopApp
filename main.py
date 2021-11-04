import sys
from PyQt5.QtCore import QLine, Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from py_calc_controller import PyCalcController, evaluate_expression

__version__ = '0.1'
__author__ = 'Raphael Sparenberg'


class PyCalcUi(QMainWindow):
    """[summary]

    Args:
        QMainWindow (object): [description]
    """
    def __init__(self):
        """View initializer
        """
        super().__init__()
        self.setWindowTitle('PyCalc')
        self.setFixedSize(650, 480)
        self.generalLayout= QVBoxLayout()
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self._centralWidget)
        self._createDisplay()
        self._createButtons()
        
    def _createDisplay(self):
        """
        """
        self.display=QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
        
    def _createButtons(self):
        self.buttons = {}
        buttons_layout = QGridLayout()
        buttons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 4),
        }
        for btn_text, pos in buttons.items():
            self.buttons[btn_text] = QPushButton(btn_text)
            self.buttons[btn_text].setFixedSize(40, 40)
            buttons_layout.addWidget(self.buttons[btn_text], pos[0], pos[1])
        
        self.generalLayout.addLayout(buttons_layout)   
        
    def setDisplayText(self, text):
        """[summary]

        Args:
            text ([type]): [description]
        """
        self.display.setText(text)
        self.display.setFocus()
        
    def displayText(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.display.text()

    def clearDisplay(self):
        """[summary]
        """
        self.setDisplayText('')
             

def main():
    """Main Function
    """
    py_calc=QApplication([])
    view=PyCalcUi()
    view.show()
    model= evaluate_expression
    PyCalcController(model=model, view=view)
    sys.exit(py_calc.exec_())

if __name__ == '__main__':
    main()
