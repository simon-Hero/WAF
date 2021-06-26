from utils.read import get_config

data = {
    "WebDriverWaitTime": get_config("WebDriverWaitTime")
}

WebDriverWaitTime = data.get("WebDriverWaitTime")



