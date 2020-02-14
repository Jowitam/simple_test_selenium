class StartPageLocators(object):
    CONTAINER_start_page = "//div[@class = 'main-wrapper']"
    CONTAINER_show_main = CONTAINER_start_page + "//div[@data-box-name='Showcase main']"
    CONTAINER_login = CONTAINER_show_main + "//div[@data-box-name='logged out user context']"
    BUTTON_login = CONTAINER_login + "//div[@data-box-name='login button']"

    BUTTON_close_rodo = "//div[@data-role='rodo-dialog']//button[@data-role='close-and-accept-consent']"
