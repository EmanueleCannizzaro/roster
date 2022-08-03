#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Problem Statement
Mrs. Jones, a teacher at Billings Elementary School, has been asked by the administration to track her students' grades in a roster stored in an Excel file.

Unfortunatly, Mrs. Jones had a bad experience with Excel as a child and as solemnly sworn never to use Excel again.

Your task is to create a Python class for reading and manipulating a provided Excel file so Mrs. Jones doesn't haven't to use Excel to successfully record her students' grades.

One easy solution would have been to show Mrs Jones libreoffice Calc or google Sheet but we have rolled these options out as they would have no need for coding.

'''

import openpyxl
import pandas

class Roster():
    """ This class will represent a Roster-like Spreadsheet.
    """
    
    def __init__(self, name:str=None):
        self.name = name
        self.data = {}

    def get_student_names(self):
        pass

    def get_student(self, fullname:str):
        pass

    def calculate_class_average():
        pass

    def class_average(self):
        return self.calculate_class_average()

    def delete_student(self):
        pass

    def read(self, filename:str):
        sheetnames = pd.ExcelFile(filename).sheetnames
        _dfs = pd.read_excel(filename, sheetname='Roster')
        return _dfs

    def show(self):
        display(self.data['Roster'])
        for key in self.data.keys():
            if key.startswith('Student_'):
                display(self.data[key])

    def to_excel(self, filename:str)
        with as writer:
            for key in self.data.keys():
                sheetname = key
                self.data[key].to_excel(writer, sheet_name=sheetname)

    def save(self, filename:str):
        return self.to_excel(filename)

    def add(self, entry:str)
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

    def replace(self, entry:str)
        pass

    def sort(self):
        pass
