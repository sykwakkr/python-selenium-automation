# Created by jkwak at 7/29/24
Feature: Help Page Test
  # Option test

  Scenario Outline: User can select a topic option for help
    Given HW9 Open Return & Exchange help topic page
    Then HW9 Verify the correct "Returns" page opened
    When HW9 Select "Promotions & Coupons" topic page
    Then HW9 Verify the correct "Current promotions" page opened
    Then HW8 Pause <time> seconds at the end to review the result of step
    Examples:
    |time |
    | 1   |
#    | 1   |
#    | 1   |
#    | 1   |
#    | 1   |