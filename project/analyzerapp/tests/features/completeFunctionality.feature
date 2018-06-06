Feature: Test all functionalities like the final user

    Scenario: Writing a date and cheking that the results are correct
        When I put a date into DateField
        And I click the analyze button
        Then I should see the results:
        And The results should be in Order
        Then I click the reset button
        And I should see the resultarea empty
        
