import pydantic

from dbwidgeter.validators import convert_all_empty_strings_to_none


class DatabricksSettings(pydantic.BaseSettings):
    _ = convert_all_empty_strings_to_none()
