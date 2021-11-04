import numpy as np

ERROR_600 = 'Input is empty or NONE'
ERROR_MSG = 'ERROR'
SUCCESS_MSG = 'Succes'

class MathOperations():
    """Class for all math operations"""
    
    def check_for_correct_input(self, value_one, value_two):
        """[summary]

        Args:
            value_one ([type]): [description]
            value_two ([type]): [description]

        Returns:
            [type]: [description]
        """
        if value_one == '' or value_one == None:
            return ERROR_600
        elif value_two == '' or value_two == None:
            return ERROR_600
        else:
            return True

    def addition(self, value_one, value_two):
        """[summary]

        Args:
            value_one ([type]): [description]
            value_two ([type]): [description]

        Returns:
            [type]: [description]
        """
        if self._check_for_correct_input(self, value_one, value_two) == True:
            return np.add(value_one, value_two)
        else:
            return ERROR_MSG
    
    def subtraction(self, value_one, value_two):
        """[summary]

        Args:
            value_one ([type]): [description]
            value_two ([type]): [description]

        Returns:
            [type]: [description]
        """
        if self._check_for_correct_input(self, value_one, value_two) == True:
            return np.subtract(value_one, value_two)
        else:
            return ERROR_MSG
