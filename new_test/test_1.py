from testsite import OperationHelper



def test_step1(browser):
    testpage = OperationHelper(browser)

    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_login("test")

    testpage.click_login_button()

    assert testpage.get_error_text() == "401"


# def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, hello_code):
#     input1 = site.find_element("xpath", x_selector1)
#     # input1.clear()
#     input1.send_keys(testdata["valid_login"])
#
#     input2 = site.find_element("xpath", x_selector2)
#     # input2.clear()
#     input2.send_keys(testdata["valid_pswd"])
#
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#
#     username = site.find_element("xpath", x_selector4).text
#     assert username == hello_code
#
#
# def test_step3(new_post_button, add_title, add_content, add_description, save_button, new_post_check):
#     post_btn = site.find_element("xpath", new_post_button)
#     post_btn.click()
#     input_title = site.find_element("xpath", add_title)
#     input_title.send_keys("New test post")
#
#     input_description = site.find_element("xpath", add_description)
#     input_description.send_keys("New post test selenium")
#
#     input_content = site.find_element("xpath", add_content)
#     input_content.send_keys("Add new content with selenium auto test")
#
#     save_btn = site.find_element("xpath", save_button)
#     site.driver.sleep(5)
#     save_btn.click()
#     site.driver.sleep(5)
#
#     post_check = site.find_element("xpath", new_post_check).text
#     site.driver.close()
#     assert post_check == "New test post"



