Feature: Click execute having an invalid date

    Scenario: Executing with invalid date
        When I write an invalid date in the dateField
        Then I click the analyze button
        And I should see the error message
        
