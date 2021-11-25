from selenium import webdriver
from tempfile import TemporaryDirectory
from webdriver_manager.chrome import ChromeDriverManager
from server import ChromelessServer, get_default_chrome_options
import helper

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium_stealth import stealth

import inspect, marshal
import picklelib
import types

def browse(entry_function_name, functions, headless = False, use_tor = True):
    server = ChromelessServer(headless, use_tor)
    
    return picklelib.loads(server.recieve({
        "invoked_func_name": entry_function_name,
        "codes": { name: (inspect.getsource(functions[name]), marshal.dumps(functions[name].__code__)) for name in functions},
        "arg": [],
        "kw": {},
        "options": None,
        "REQUIRED_SERVER_VERSION": 2,
    }))