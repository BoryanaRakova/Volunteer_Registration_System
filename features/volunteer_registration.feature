Feature: Volunteer Registration

  Scenario: Successful volunteer registration
    Given a volunteer provides the name "Anna Smith"
    And the volunteer provides the email "anna@email.com"
    When the volunteer submits the registration form
    Then the system should display "Volunteer registered successfully"

  Scenario: Missing email address
    Given a volunteer provides the name "Anna Smith"
    And the volunteer does not provide an email address
    When the volunteer submits the registration form
    Then the system should display "Error: Email is required"

  Scenario: Duplicate volunteer registration
    Given a volunteer with the email "anna@email.com" is already registered
    When another volunteer submits the same email "anna@email.com"
    Then the system should display "Error: Volunteer already registered"

  Scenario: Invalid email format
    Given a volunteer provides the name "Anna Smith"
    And the volunteer provides the email "annaemail.com"
    When the volunteer submits the registration form
    Then the system should display "Error: Invalid email address"