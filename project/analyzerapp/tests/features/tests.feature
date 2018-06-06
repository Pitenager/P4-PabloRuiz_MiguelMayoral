Feature: All the application

    Scenario: DateField empty
        When I put a date into DateField
        And I click the analyze button
        Then I should see the results:
    
    Scenario: Analyze without date
        When I dont set a date
        And I click the analyze button
        Then I should see the results:
        
    Scenario: Executing with invalid date
        When I write an invalid date in the dateField
        Then I click the analyze button
        And I should see the error message

    Scenario: Reset the textarea
        When I write a date into datefield
        Then I click the analyze button
        Then I click the reset button
        And I should see the resultarea empty

    Scenario: Textarea with some text in it
        When I write a date into datefield
        And I click the analyze button
        Then The datefield looks empty

    Scenario: Reset with no text
        When I have the datefield empty
        And I click the reset button
        Then The datefield continues empty

    Scenario: Writing a date and cheking that the results are correct
        When I put a date into DateField
        And I click the analyze button
        Then I should see the results:
        And The results should be in Order
        Then I click the reset button
        And I should see the resultarea empty