import json
import py4j
import logging
from pydantic import Field, validator

from pyspark.sql import SparkSession


WIDGET_TAG = 'widget'
JOB_UNDEFINED = 'JOB_MODE_WIDGET_UNDEFINED'


# https://stackoverflow.com/questions/51885332/how-to-load-databricks-package-dbutils-in-pyspark
def get_dbutils():
    try:
        from pyspark.dbutils import DBUtils
        spark = SparkSession.builder.getOrCreate()
        dbutils = DBUtils(spark)
    except ImportError:
        import IPython
        dbutils = IPython.get_ipython().user_ns["dbutils"]
    return dbutils


def make_widgets(widgeter_class):
    dbutils = get_dbutils()
    properties = json.loads(widgeter_class.construct().schema_json())['properties']
    widget_list = [field for field, details in properties.items() if WIDGET_TAG in details.get('tag', [])]
    dbutils.widgets.removeAll()
    [dbutils.widgets.text(widget, '') for widget in widget_list]
    return widget_list


def get_or_create_widget_safe(field_name, dbutils):
    try:
        widget_value = dbutils.widgets.get(field_name)
    except py4j.protocol.Py4JJavaError:
        dbutils.widgets.text(field_name, '')
        try:
            widget_value = dbutils.widgets.get(field_name)
            logging.warning(f"Notebook Mode: Widget for '{field_name}' has not been defined, creating empty widget")
        except py4j.protocol.Py4JJavaError:
            logging.warning(f"Job Mode: Widget for '{field_name}' has not been defined, setting value to None/Default")
            widget_value = JOB_UNDEFINED
    return widget_value
