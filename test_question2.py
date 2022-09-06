from selenium.webdriver import ChromeDriver

XPATH_SUBMIT_LOGIN_BTN = '//input[id="submit"]'
XPATH_USERNAME_FIELD = '//input[id="username"]'
XPATH_PASSWORD_FIELD = '//input[id="password"]'

def test_can_open_site(driver:WebDriver):
    driver.get("https://www.vision.qa2.freestyleiot.com/")

def test_can_login_to_site(driver:WebDriver):
    login_url = "https://www.vision.qa2.freestyleiot.com/login"
    driver.get("https://www.vision.qa2.freestyleiot.com/")
    valid_username = "bob123"
    valid_password = "OsrghSAD#*&^@"
    username_field = driver.find_element(By.XPATH, XPATH_USERNAME_FIELD)
    password_field = driver.find_element(By.XPATH, XPATH_PASSWORD_FIELD)
    username_field.send_keys(valid_username);
    password_field.send_keys(valid_password);

    submit_login_button = driver.find_element(By.XPATH, XPATH_SUBMIT_LOGIN_BTN)
    submit_login_button.click()

    #Usually here I would check the return and see if there is a wrong username password or complete failure or whatever
    if driver.current_url == login_url:
        return "Failed because the login failed"


if __name__ == '__main__':
    # would need to be expanded on to run multiple different browsers.
    # I suspect most of these tests should be run on different browers
    driver = new ChromeDriver ();
    tests = {
        "test_can_open_site": test_can_open_site,
        "test_can_login_to_site": test_can_login_to_site
    }

    results = {}

    for key, test in tests:
        result = test(driver)
        results[key] = result

    for key, result in results:
        if result === True:
            print(f"test {key}: Pass")
        else:
            print(f"test {key}: Failed - {result}")
