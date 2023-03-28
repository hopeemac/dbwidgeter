# dbwidgeter

The DB Widgeter package was designed to better handle Databricks Notebook and Job configurations defined by Databricks widgets. This package is built on the core concepts of [Pydantic](https://docs.pydantic.dev/).

This package in partnership with Pydantic enables:
1. Automatic Type conversion and checking (Ex. '10' to 10, 'false' to `False`)
2. Ability to set default field values for Databricks widgets that are shared across Notebooks and Jobs
3. A centralized location for all widget information (descriptions, defaults, etc) in 1 class
4. Ability to set a widget value as Required (if a default is not specified the fields will be considered Required)

This package also enables 1 source for the following 3 widget actions:
1. Creating Notebook Widgets
2. Loading Values from Widgets (Notebook and Job)
3. Printing/Logging Widget Values

The Databricks Widgeter will automatically raise an error stopping the job or notebook with a clear error message if the widget input does not meet the expectations outlined in the Widgeter class. 

Two primary helpers are available from this package `DatabricksSettings` and `DatabricksField`. The `DatabricksSettings` class automatically converts all empty strings (the Databricks Widgets default value) to Nones to enable automatic use of Pydantic's required field checking.

A `DatabricksField` automatically uses Databricks widget as the value for that field if the Widget is populated. Using an DatabricksField class will also automatically enable the creation of a widget with that name via the `make_widgets()` function.

The package also provides 2 validors for handling of 2 key Databricks widget validation, converting a comma-separated string list to a list (`validate_parse_string_to_list`) and validating the widget value is amongst a list of accepted values (`validate_confirm_in_list`).


## Getting Started

To install

Note: This package has NOT been published to PyPi and thus requires manual building and installing
`pip install dbwidgeter` 

To use the DBWidgeter, a DatabricksSettings class should be defined in your notebook.

## Example Usage
```
from dbwidgeter import DatabricksSettings, DatabricksField
from dbwidgeter.validators import validate_confirm_in_list, validate_parse_string_to_list

class Widgeter(DatabricksSettings):
    num_epochs: int = DatabricksField('num_epochs', 
        description='Something', 
        gt=20,
        default=100)
    publish_model: bool = DatabricksField('publish_model', 
        description='Boolean of whether the model should be published', 
        default=False)
    env: str = DatabricksField('env', 
        description='The environment', 
        default='prod')
    labels: list = DatabricksField('labels', 
        description='list of model labels', 
        default=['cat', 'dog'])
    
    _validate_env_confirm_in_list = validate_confirm_in_list('env', ['prod', 'staging', 'dev'])
    _validate_labels_parse_string_to_list = validate_parse_string_to_list('labels')


configs = Widgeter()
print(configs)
```

## Limitations
Widget Input Types dropdown are not supported. Only Databricks Text Input Widgets are supported
Databricks Automatic Refresh after Widgets change will not work correctly