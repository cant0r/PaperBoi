from collections.abc import Iterator

import requests
from PaperBoi.Models.Magazine import Magazine
from selenium import webdriver

from PaperBoi.Providers import IMPLICIT_TIMEOUT_SECONDS, PAGE_LOAD_TIMEOUT_SECONDS


class BaseProvider:

    def __init__(self) -> None:
        self.requests_session = requests.Session()
        self._init_selenium()

    def DownloadMagazines() -> Iterator[Magazine]:
        pass

    def _init_selenium(self):
        edge_options = webdriver.EdgeOptions()
        edge_options.accept_insecure_certs = True
        edge_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.web_driver = webdriver.Edge(edge_options)
        self.web_driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT_SECONDS)
        self.web_driver.implicitly_wait(IMPLICIT_TIMEOUT_SECONDS)
        self.web_driver.set_window_size(1920, 1080)
        self.web_driver.minimize_window()
