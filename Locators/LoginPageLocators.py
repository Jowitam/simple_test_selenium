class LoginPageLocators(object):
    CONTAINER_page = "//div[@ng-app= 'loginFrontend']"
    CONTAINER_login = CONTAINER_page + "//section[contains(@class, 'm-card m-flex-auto')]"

    BUTTON_login = CONTAINER_login + "//button[@id='login-button']"

    MESSAGE_wrong_email = CONTAINER_login + "//div[@id='wrong-login-message']//span"