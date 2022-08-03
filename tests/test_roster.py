import pytest

from openpyxl import load_workbook
from roster import Roster
import pandas

@pytest.fixture
def data():
    with Roster("Jones's Roster 2019") as r:
        data = r.read("Jones_2019.xlsx")
        return data

@pytest.fixture
def test_student_names(data):
    with Roster("Jones's Roster 2019") as r:
        r.data = data

        student_names = r.get_student_names()

        assert len(student_names) == 7
        assert "Robert Waters" in student_names

        catherine = r.get_student("Catherine Hitchens")
        assert catherine["id"] == 3
        assert isinstance(catherine["grades"], pandas.Series)
        assert len(catherine["grades"]) == 10
        assert catherine["grades"][4] == 86

        assert r.class_average() == 614.1/7

def test_write(self):
    with Roster("Jones's Roster 2019") as r:
        r.data = data

        john = r.get_student("Johnny Carson")
        for assignment, grade in [(3, 90), (6, 94), (9, 92)]:
            john["grades"][assignment] = grade
        assert r.class_average() == 616.6/7
        r.save("Jones_2019_Updated.xlsx")

    wb = load_workbook("Jones_2019_Updated.xlsx")
    assert wb.get_sheet_by_name("Student_1")["B12"].value == 94
    wb.close()

def test_delete_student(self):
    with Roster("Jones's Roster 2019") as r:
        r.data = data

        student_count = len(r.get_student_names())
        assert student_count == 7
        assert r.get_student("William Thomas")["id"] == 5

        r.delete_student("Allen Dalton")

        student_count = len(r.get_student_names())
        assert student_count == 6
        assert r.get_student("William Thomas")["id"] == 4
        r.save("Jones_2019_Reduced.xlsx")

    wb = load_workbook("Jones_2019_Reduced.xlsx")
    sheet_names = wb.get_sheet_names()
    assert len(sheet_names) == 7
    assert sheet_names[0] == "Roster"
    assert sheet_names[-1] == "Student_6"
    assert wb.get_sheet_by_name("Student_3")["B7"].value == 92
    wb.close()
