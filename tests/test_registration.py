from pages.registration_page import RegistrationPage
from data.registration_data import REGISTRATION_DATA
import allure

@allure.title("Verify user can register successfully")
def test_registration_success(browser):
    registration_page = RegistrationPage(browser)
    valid_data = REGISTRATION_DATA["valid"]
    
    registration_page.open()
    registration_page.click_registration_menu()
    
    assert "Sign up" in registration_page.get_registration_popup_screen()
    
    registration_page.input_registration_form(
        valid_data["username"],
        valid_data["password"]
    )
    registration_page.click_registration_button()
    
    assert valid_data["expected_message"] in registration_page.get_registration_success_message()
    
@allure.title("Verify user cannot register using existing username")
def test_registration_failed(browser):
    registration_page = RegistrationPage(browser)    
    invalid_data = REGISTRATION_DATA["invalid"]
    
    registration_page.open()
    registration_page.click_registration_menu()
    
    assert "Sign up" in registration_page.get_registration_popup_screen()
    
    registration_page.input_registration_form(
        invalid_data["username"],
        invalid_data["password"]
    )
    registration_page.click_registration_button()
    
    assert invalid_data["expected_message"] in registration_page.get_registration_error_message()