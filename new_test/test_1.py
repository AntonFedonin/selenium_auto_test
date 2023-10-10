from testsite import OperationHelper
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    testsite = OperationHelper(browser)
    testsite.go_to_site()
    testsite.enter_login("test")
    testsite.enter_pass("test")
    testsite.click_login_button()
    assert testsite.get_error_text() == "401"


def test_step2(browser):
    testsite = OperationHelper(browser)
    testsite.go_to_site()
    testsite.enter_login(testdata["valid_login"])
    testsite.enter_pass(testdata["valid_pass"])
    testsite.click_login_button()

    assert testsite.get_login_name_text() == f'Hello, {testdata["valid_login"]}'


def test_step3(browser):
    testsite = OperationHelper(browser)
    testsite.click_new_post_button()
    testsite.add_title("Hello world")
    testsite.add_description("New test, new word")
    testsite.add_content("Запускаю новый автотест. Возможно сработает, но это не точно")
    testsite.click_save_post_button()
    assert testsite.get_post_title_text() == "Create Post"


def test_step4(browser):
    testsite = OperationHelper(browser)
    testsite.go_to_contact()
    print(testsite.get_contact_us_text())
    assert testsite.get_contact_us_text() == "Contact us!"


def test_step5(browser):
    testsite = OperationHelper(browser)
    # testsite.go_to_contact()
    testsite.enter_contact_name("Test")
    testsite.enter_contact_email("123@mail.ru")
    testsite.enter_content_in_contact("Enter test content")
    testsite.click_contact_us_button()
    print(testsite.get_alert_text())
