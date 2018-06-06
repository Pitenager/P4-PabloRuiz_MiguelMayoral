Feature: Analyze
        
    Scenario: Analyze without date
        When I dont set a date
        And I click the analyze button
        Then I should see the results: