
import pytest

from numpy.testing import assert_almost_equal
#from openpyxl import load_workbook
import os
import pandas

import roster
from roster.roster import Roster


@pytest.fixture
def r():
    _r = Roster("Jones's Roster 2019")
    _filename = os.path.join(os.path.dirname(os.path.dirname(roster.__file__)), "data", "Jones_2019.xlsx")
    _r.data = _r.read(_filename)
    return _r


def test_show(r):
    return r.show()

def test_student_names(r):
    student_names = r.get_student_names()
    assert len(student_names) == 7
    assert "Robert Waters" in student_names

    ix = r.get_student_id("Catherine Hitchens")
    assert ix == 3
    catherine = r.get_student_by_id(ix)
    catherine = r.get_student_by_fullname("Catherine Hitchens")
    assert isinstance(catherine["Grade"], pandas.Series)
    assert len(catherine["Grade"]) == 10
    ''' Note that the index has been renamed based on assignement number! '''
    assert catherine.loc[5, "Grade"] == 86

    assert_almost_equal(r.class_average, 614.1/7)

def test_write(r):
    assert "Johnny Carson" in r.student_names
    john = r.get_student_by_fullname("Johnny Carson")
    ''' Note that the index has been renamed based on assignement number! '''
    for ix, grade in [(4, 90), (7, 94), (10, 92)]:
        john.loc[ix, "Grade"] = grade
    assert john.loc[4, 'Grade'] == 90
    assert "Johnny Carson" in r.student_names
    assert r.get_student_by_fullname("Johnny Carson").loc[4, 'Grade'] == 90
    assert_almost_equal(r.class_average, 616.6/7)

    filename = os.path.join(os.path.dirname(os.path.dirname(roster.__file__)), "data", "Jones_2019_Updated.xlsx")
    r.save(filename)

    ''' Reimplemented without openpyxl! '''
    desired = Roster("Jones's Roster 2019")
    desired.data = desired.read(filename)
    john = r.get_student_by_fullname("Johnny Carson")
    assert john.loc[4, 'Grade'] == 90
    assert john.loc[7, 'Grade'] == 94
    assert john.loc[10, 'Grade'] == 92
    assert_almost_equal(r.class_average, 616.6/7)

def test_delete_student(r):
    assert len(r.student_names) == 7
    assert r.get_student_id("William Thomas") == 5

    r.data = r.delete_student("Allen Dalton")

    assert len(r.student_names) == 6
    assert r.get_student_id("William Thomas") == 4

    filename =  os.path.join(os.path.dirname(os.path.dirname(roster.__file__)), "data", "Jones_2019_Reduced.xlsx")
    r.save(filename)

    ''' Reimplemented without openpyxl! '''
    desired = Roster("Jones's Roster 2019")
    desired.data = desired.read(filename)
    assert "Roster" in desired.data.keys()
    assert len(desired.student_names) == 6
    assert "Allen Dalton" not in desired.student_names
    assert "William Thomas" in desired.student_names
    john = r.get_student_by_fullname("Johnny Carson")
    assert john.loc[5, 'Grade'] == 92
