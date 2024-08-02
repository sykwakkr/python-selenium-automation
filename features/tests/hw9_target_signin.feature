# Created by jkwak at 7/30/24
Feature: Sign In Page Test
  # Test sign-in page

  Scenario Outline: Alert message with incorrect e,ail ad password
    Given HW9 Open Target sign in page
    When HW9 Enter incorrect email and password combination
      And HW9 Click login button
    Then HW9 Verify that 'We can't find your account.' alert message is shown
    Then HW8 Pause <time> seconds at the end to review the result of step
    Examples:
    |time |
    |1    |
#    |1    |
#    |1    |
#    |1    |
#    |1    |
