Feature: Login Fail

    @login
    Scenario Outline: Invalid Credentials: Unsuccessful Login to App
        Given user is on the login page
        When user enters username "<username>" and password "<password>"
        Then the user is not logged in

        Examples: Invalid username/password permutations
            | username   | password     |
            | user1      | wrong        |
            | wrong      | user1Pass    |