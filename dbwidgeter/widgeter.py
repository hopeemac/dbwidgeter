from dbwidgeter.DatabricksSettings import DatabricksSettings
from dbwidgeter.DatabricksField import DatabricksField
from dbwidgeter.validators import validate_confirm_in_list, validate_parse_string_to_list
from dbwidgeter.utils import make_widgets


class Widgeter(DatabricksSettings):
    num_epochs: int = DatabricksField('num_epochs', 
        description='Something', 
        gt=20,
        default=100)
    publish_model: bool = DatabricksField('publish_model', 
        description='Boolean of whether the model should be published', 
        default=False)
    env: str = DatabricksField('env', 
        description='The environment')
    labels: list = DatabricksField('labels', 
        description='list of model labels', 
        default=['cat', 'dog'])
    
    _env_confirm_in_list = validate_confirm_in_list('env', ['prod', 'staging', 'dev'])
    _labels_parse_string_to_list = validate_parse_string_to_list('labels')
