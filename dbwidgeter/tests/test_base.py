import pytest
import pydantic

from dbwidgeter import DatabricksField, DatabricksSettings


def test_no_default_empty_widget():
    TEST_WIDGET_VALUE = ''

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', test_widget_value=TEST_WIDGET_VALUE)
   
    with pytest.raises(pydantic.ValidationError):
        configs = Widgeter()


def test_default_empty_widget():
    TEST_WIDGET_VALUE = ''

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', default=10, test_widget_value=TEST_WIDGET_VALUE)
   
    configs = Widgeter()
    assert configs.num_epochs == 10


def test_no_default_populated_widget():
    TEST_WIDGET_VALUE = '20'

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', test_widget_value=TEST_WIDGET_VALUE)
   
    configs = Widgeter()
    assert configs.num_epochs == 20


def test_default_populated_widget():
    TEST_WIDGET_VALUE = '20'

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', default=10, test_widget_value=TEST_WIDGET_VALUE)
    
    configs = Widgeter()
    assert configs.num_epochs == 20
