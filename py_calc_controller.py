from functools import partial

ERROR_MSG = 'ERROR'
#Controller class to connect to the GUI and model
class PyCalcController():
    """PyCalcsController class"""
    def __init__(self, model, view):
        """[summary]

        Args:
            view ([type]): [description]
        """
        self._evaluate=model
        self._view=view
        self._connect_signals()

    def _calculate_result(self):
        """Calculate the result
        """
        result=self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)
        
    def _build_expression(self, sub_exp):
        """[summary]

        Args:
            sub_exp ([type]): [description]
        """
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()


        expression=self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connect_signals(self):
        """[summary]
        """
        for btn_text, btn in self._view.buttons.items():
            if btn_text not in {'=', 'C'}:
                btn.clicked.connect(partial(self._build_expression, btn_text))

        self._view.buttons['='].clicked.connect(self._calculate_result)
        self._view.display.returnPressed.connect(self._calculate_result)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)


def evaluate_expression(expression):
    """
    Args:
        expression ([type]): [description]
    """
    try:
        result=str(eval(expression, {}, {}))
    except Exception:
        result= ERROR_MSG
    return result
