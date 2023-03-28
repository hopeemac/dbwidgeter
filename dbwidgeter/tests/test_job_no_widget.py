import pytest
import pydantic

from dbwidgeter import DatabricksField, DatabricksSettings
from dbwidgeter.utils import JOB_UNDEFINED


def test_no_default_job_widget_undefined():
    TEST_WIDGET_VALUE = JOB_UNDEFINED

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', test_widget_value=TEST_WIDGET_VALUE)
   
    with pytest.raises(pydantic.ValidationError):
        configs = Widgeter()


def test_default_job_widget_undefined():
    TEST_WIDGET_VALUE = JOB_UNDEFINED

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', default=10, test_widget_value=TEST_WIDGET_VALUE)
   
    configs = Widgeter()
    assert configs.num_epochs == 10