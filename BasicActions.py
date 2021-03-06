from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_element(driver, xpath):
    # obsluga czekania na widocznosc elementu po xpath
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
    finally:
        pass
