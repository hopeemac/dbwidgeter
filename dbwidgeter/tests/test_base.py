import pytest
import pydantic

from dbwidgeter import DatabricksField, DatabricksSettings


def test_no_default_empty_widget(dbutils_fixture_empty):

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', dbutils=dbutils_fixture_empty)
   
    with pytest.raises(pydantic.ValidationError):
        configs = Widgeter()


def test_default_empty_widget(dbutils_fixture_empty):

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', default=10, dbutils=dbutils_fixture_empty)
   
    configs = Widgeter()
    assert configs.num_epochs == 10


def test_no_default_populated_widget(dbutils_fixture):

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', dbutils=dbutils_fixture)
   
    configs = Widgeter()
    assert configs.num_epochs == 20


def test_default_populated_widget(dbutils_fixture):

    class Widgeter(DatabricksSettings):
        num_epochs: int = DatabricksField('num_epochs', default=10, dbutils=dbutils_fixture)
    
    configs = Widgeter()
    assert configs.num_epochs == 20
