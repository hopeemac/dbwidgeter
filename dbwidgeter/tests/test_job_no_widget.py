import pytest
import pydantic

from dbwidgeter import DatabricksField, DatabricksSettings
from dbwidgeter.utils import JOB_UNDEFINED


def test_no_default_job_widget_undefined(dbutils_fixture_undefined):

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', dbutils=dbutils_fixture_undefined)
   
    with pytest.raises(pydantic.ValidationError):
        configs = Widgeter()


def test_default_job_widget_undefined(dbutils_fixture_undefined):

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', default=10, dbutils=dbutils_fixture_undefined)
   
    configs = Widgeter()
    assert configs.num_epochs == 10
