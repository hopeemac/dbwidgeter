from unittest.mock import MagicMock
import pytest
import py4j

from dbwidgeter.utils import JOB_UNDEFINED


def widget_values_lookup_generator(widget_values):
    def widget_value_lookup(widget):
        try:
            return widget_values[widget]
        except KeyError:
            return JOB_UNDEFINED
    return widget_value_lookup


class DbUtils(object):
    def __init__(self, widget_values):
        self.widget_values = widget_values

        self.widgets = MagicMock()
        self.widgets.get = MagicMock(side_effect=widget_values_lookup_generator(self.widget_values))


@pytest.fixture
def dbutils_fixture():
    widget_values = {
        'num_epochs': '20',
    }
    return DbUtils(widget_values)


@pytest.fixture
def dbutils_fixture_undefined():
    widget_values = {}
    return DbUtils(widget_values)


@pytest.fixture
def dbutils_fixture_empty():
    widget_values = {
        'num_epochs': ''
    }
    return DbUtils(widget_values)
