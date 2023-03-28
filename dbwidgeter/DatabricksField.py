import logging
from pydantic import Field

from dbwidgeter.utils import WIDGET_TAG, JOB_UNDEFINED, get_or_create_widget_safe


def DatabricksField(field_name, test_widget_value='DUMMY_TEST', **kwargs):
    # Note: Pydantic will Warn if user passes in a Tag value in kwargs
    
    widget_value = get_or_create_widget_safe(field_name, test_widget_value)
    
    widget_is_unset = widget_value in ['', None]
    widget_has_default = 'default' in list(kwargs.keys())

    # In a Databricks Field, the widget value is automatically used by way of the default Field value
    # A default value for the Field can also be specified in case the widget value is unset 
    if (widget_is_unset and widget_has_default) or widget_value == JOB_UNDEFINED:
        pass
    else:
        # overriding default if widget is set or no default
        kwargs['default']=widget_value
            
    return Field(
        tag=WIDGET_TAG,
        **kwargs
    )


# ToDo: Test with Job Parameters
# Test when no kwargs passed into the Field DONE
# Test making a field Optional/Required DONE
# Add License
# Enable from dbwidgeter import DatabricksSettings <-- I think it can be done with the init file DONE
# Need to set the default to widget value but when widget doesn't exist this fails FIXED
