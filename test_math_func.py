import math_func
import pytest
import sys    # gives the version of python


#If you want to skip the test case --------
@pytest.mark.skip(reason="Do not run this test case")
def test_add():
    assert math_func.add(5,7)==12
    assert math_func.add(6)==10

# If you want to skip the test case with any condition-------
@pytest.mark.skipif(sys.version_info > (3,3), reason="The version is greater than 3.3")
def test_add():
    assert math_func.add(8,3)==11
    assert math_func.add(8)==12

def test_prod():
    assert math_func.prod(6,7)==42
    assert math_func.prod(6)==24    


def test_add_string():
    result = math_func.add('Hello', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Helloooo' not in result


def test_john_data():
    db = math_func.studentDB()
    db.connect('data_file.json')
    john_data= db.get_data('John')
    assert john_data['name'] == 'John'
    assert john_data['age'] == 20

def test_smith_data():
    db = math_func.studentDB()
    db.connect('data_file.json')
    smith_data = db.get_data('Smith')
    assert smith_data['name'] == 'Smith'
    assert smith_data['age'] == 22












