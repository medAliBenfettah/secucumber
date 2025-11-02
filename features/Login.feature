Feature: OrangeHRM Login functionality 
    As a user of OrangeHRM
    I want to be able to log in to the application
    So that I can access my account and use the features provided by the application.

    Background: User in the login page
        Given I am on the OrangeHRM login page

    @smoke @positive
    Scenario: Successful login with valid credentials
        When I enter valid username "admin"
        And I enter valid password "admin123"
        And I click on the login button
        Then I should be redirected to the dashboard page
        And I should see the dropdown in the header 

    @negative
    Scenario: Failed login with invalid username
        When I enter invalid username "invalidUsername"
        And I enter valid password "admin123"
        And II click on the login button
        Then I should see and error message "Invalid credentials"

    @negative
    Scenario: Failed login with invalid password
        When  I enter valid username "admn"
        And I enter invalid password "invalidPassword"
        And I click on the login button
        Then I should see and error message "Invalid credentials"

    @negative
    Scenario: Failed login with empty crendentials
        When I leave the username field empty
        And I leave the password field empty
        And I click on the login button
        Then I should see an error message

    @dataDriven
    Scenario Outline: Login with multiple invalid credentials
        When I enter username '<username>'
        And I enter password '<password>'
        And I click on the login button
        Then I should see and error message 

        Examples:
            | username        | password        |
            | invalidUser1    | invalidPass1    |
            | invalidUser2    | invalidPass2    |
            | invalidUser3    | invalidPass3    |
            | Admin           | wrongpass       |