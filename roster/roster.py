#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem Statement
Mrs. Jones, a teacher at Billings Elementary School, has been asked by the administration to track her students' grades in a roster stored in an Excel file.

Unfortunatly, Mrs. Jones had a bad experience with Excel as a child and as solemnly sworn never to use Excel again.

Your task is to create a Python class for reading and manipulating a provided Excel file so Mrs. Jones doesn't haven't to use Excel to successfully record her students' grades.

One easy solution would have been to show Mrs Jones libreoffice Calc or google Sheet but we have rolled these options out as they would have no need for coding.

'''

from autologging import logged, TRACE, traced

from IPython.display import display
import openpyxl
import pandas as pd


@traced
@logged
class Roster():
    """ This class will represent a Roster-like Spreadsheet.
    """
    
    def __init__(self, name:str=None):
        self.__log.info('Instance of Roster Class')
        self.name = name
        self.data = {}

    @property
    def student_names(self) -> list:
        _student_names = self.data['Roster']
        return sorted(_student_names.loc[:, 'Full Name'])

    def get_student_names(self) -> list:
        '''
        function added for compatibility but it should be marked as "to be deprecated".
        '''
        return self.student_names

    def get_student_id(self, fullname:str) -> int:
        ix = self.data['Roster'][self.data['Roster']['Full Name'] == fullname].index[0]
        return ix

    def get_student_by_id(self, ix:int) -> pd.DataFrame:
        return self.data[f"Student_{ix}"]

    def get_student_by_fullname(self, fullname:str) -> pd.DataFrame:
        ix = self.get_student_id(fullname)
        return self.get_student_by_id(ix)

    def get_student(self, fullname:str) -> pd.DataFrame:
        return self.get_student_by_fullname(fullname)

    def calculate_class_average(self) -> float:
        for key in self.data.keys():
            if key.startswith('Student_'):
                ix = int(key.replace('Student_', ''))
                self.data['Roster'].loc[ix, 'Class Grade'] = self.data[key]['Grade'].mean()
        return self.data['Roster']['Class Grade'].mean()

    @property
    def class_average(self) -> float:
        '''
        function added for compatibility but it should be marked as "to be deprecated".
        '''
        return self.calculate_class_average()

    def delete_student(self, fullname:str):
        ''' Not implemented yet. '''
        pass

    def read(self, filename:str) -> dict:
        sheetnames = pd.ExcelFile(filename).sheet_names
        _dfs = {}
        if 'Roster' in sheetnames:
            _dfs['Roster'] = pd.read_excel(filename, sheet_name='Roster').set_index('ID')
            _dfs['Roster']['Full Name'] = _dfs['Roster']['First Name'] + ' ' + _dfs['Roster']['Last Name']
        for sheetname in sheetnames:
            if sheetname.startswith('Student_'):
                _dfs[sheetname] = pd.read_excel(filename, sheet_name=sheetname, skiprows=list(range(4))).set_index('Assignment')
        return _dfs

    def show(self):
        display(self.data['Roster'])
        for key in self.data.keys():
            if key.startswith('Student_'):
                display(self.data[key])

    def to_excel(self, filename:str):
        with pd.ExcelWriter(filename) as writer:
            for key in self.data.keys():
                sheetname = key
                self.data[key].to_excel(writer, sheet_name=sheetname)

    def save(self, filename:str):
        '''
        function added for compatibility but it should be marked as "to be deprecated".
        '''
        return self.to_excel(filename)

    def add(self, entry:str):
        '''
        Add up two integer numbers.

        This function simply wraps the ``+`` operator, and does not
        do anything interesting, except for illustrating what
        the docstring of a very simple function looks like.

        Parameters
        ----------
        entries : pd.DataFrame
            Marks to add.

        Returns
        -------
        pd.DataFrame
            The concat of ``num1`` and ``num2``.

        See Also
        --------
        subtract : Subtract one integer from another.

        Examples
        --------
        >>> add(2, 2)
        4
        >>> add(25, 0)
        25
        >>> add(10, -10)
        0
        '''
        _df = pd.concat(self.data, entry)

    def replace(self, entry:str):
        pass

    def sort(self):
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
