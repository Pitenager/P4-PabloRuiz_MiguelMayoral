Feature: Reset with no text

    Scenario: Reset with no text
        When I have the datefield empty
        And I click the reset button
        Then The datefield continues empty