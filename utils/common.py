import os

from utils.read import get_config

data = {
    "WebDriverWaitTime": get_config("WebDriverWaitTime"),
    "page_path": os.path.abspath(os.path.dirname(os.getcwd()) + get_config("page_path")),
    "case_path": os.path.abspath(os.path.dirname(os.getcwd()) + get_config("case_path"))
}

WebDriverWaitTime = data.get("WebDriverWaitTime")
page_path = data.get("page_path")
case_path = data.get("case_path")



