import pytest
from selenium import webdriver

#Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#Chrome
# options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications": 2}
# options.add_experimental_option("prefs", prefs)

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

#Firefox
# options = webdriver.FirefoxOptions()
# options.set_preference('dom.webnotifications.enabled', False)

#Edge
# options = webdriver.EdgeOptions()
# Prefs=("profile.default_content_setting_values.notifications", 2)
# options.set_capability("prefs",Prefs)


@pytest.fixture(scope="function")
def setup(request):
    browser = "chrome"
    if browser.lower() == "chrome":

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    else:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.get("https://demoqa.com/")
    driver.maximize_window()
    request.cls.driver = driver

