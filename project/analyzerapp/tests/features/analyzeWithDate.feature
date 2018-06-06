Feature: Click analyze having a date in DateField

    Scenario: DateField empty
        When I put a date into DateField
        And I click the analyze button
        Then I should see the results:
        
