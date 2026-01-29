import pytest
from login_form import LoginForm


# classes in this sense operate as test suites
# add a description just by using a comment
class TestEmailValidation:

    # each test case is going to have a fresh form
    @pytest.fixture
    def form(self):
        return LoginForm()
    
    
    @pytest.mark.parametrize(
        "email",
       [
            "user@example.com",
            "2342Sharo@example.com",
            "user@crypto.co",
            "user@domain.ai",
            "user@test.org",
            "john.doe@gmail.com",
            "jane_doe123@yahoo.ca",
            "first.last@company.io",
            "user123@sub.domain.com",
            "alpha.beta@education.edu",
            "test-user@service.net",
            "user+tag@gmail.com",
            "simple@example.co.uk",
            "customer.support@helpdesk.com",
            "dev_team@startup.tech"
        ]
    ) 
    

    #positive test case
    def test_valid_email(self, form, email):
           assert LoginForm.validate_email(form, email) is True 
           
           
    @pytest.mark.parametrize(
        "email",
        [
            "user@.com",
            "$$$$.com",
            "user@com",
            "user@domain.c",
            "user@domain..@@@.com"
        ]
    )       
           
    #negative test case
    def test_invalid_email(self, form, email):
           assert LoginForm.validate_email(form, email) is False
           
           
class TestPasswordValidation:
    
    @pytest.fixture
    def form(self):
        return LoginForm()
    
    
    #Positive test cases for password validation
    @pytest.mark.parametrize(
        "password",
        [
            "Password123",
            "SecurePass456",
            "MySecret789",
            "Admin123456",
            "UserPass987654"
        ]
    )
    
    def test_valid_password(self, form, password):
        assert LoginForm.validate_password(form, password) is True
        
        
    #Negative test cases for password validation
    @pytest.mark.parametrize(
        "password",
        [
            None,
            "",
            "short",
            "nouppercase1",
            "ThisPasswordIsWayTooLong" * 10
        ]
    )

    def test_invalid_password(self, form, password):
        assert LoginForm.validate_password(form, password) is False