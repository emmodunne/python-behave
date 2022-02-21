Feature: Login

    @login
    Scenario: Valid Credentials: Successful Login to App
        Given user is on the login page
        When user enters username "user1" and password "user1Pass"
        Then the user is logged in
