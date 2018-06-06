Feature: Reset
    
    Scenario: Reset the textarea
        When I write a date into datefield
        Then I click the analyze button
        Then I click the reset button
        And I should see the resultarea empty