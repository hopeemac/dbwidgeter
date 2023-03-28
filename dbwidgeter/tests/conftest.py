from unittest.mock import MagicMock


class Widgets(object):
    def __init__(self):
        self.help = MagicMock()
        self.combobox = MagicMock()
        self.dropdown = MagicMock()
        self.get = MagicMock(return_value="")
        self.getArgument = MagicMock(return_value="")
        self.multiselect = MagicMock()
        self.remove = MagicMock()
        self.removeAll = MagicMock()
        self.text = MagicMock()


class DbUtils(object):
    def __init__(self):
        # self.fs = FS()
        # self.notebook = Workflow()
        self.widgets = Widgets()
        # self.secrets = Secrets()
        # self.library = Library()