from collections.abc import Iterator
from selenium.webdriver.common.by import By
import base64

from PaperBoi.Models.Magazine import Magazine
from PaperBoi.Providers.BaseProvider import BaseProvider

BASE_ADDRESS = "https://www.spar.hu"
MAGAZINE_URI_XPATH = "//a[starts-with(@title, 'spar-szorolap')]"


class SparProvider(BaseProvider):
    def __init__(self) -> None:
        super().__init__()

    def DownloadMagazines(self) -> Iterator[Magazine]:
        self.web_driver.get(f"{BASE_ADDRESS}/ajanlatok")
        magazine_anchors = self.web_driver.find_elements(By.XPATH, MAGAZINE_URI_XPATH)

        for magazine_anchor in magazine_anchors:

            magazine_bytes = self.requests_session.get(magazine_anchor.get_attribute("href")).content
            base64_magazine = base64.b64encode(magazine_bytes).decode("ascii")

            yield Magazine(
                f"{magazine_anchor.get_attribute('href')}",
                magazine_anchor.get_attribute("title"),
                base64_magazine,
            )


if __name__ == "__main__":
    print("You cannot execute this module directly!")
    exit(-1)
