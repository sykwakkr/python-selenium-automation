# Created by jkwak at 8/7/24
Feature: Tests for Wikipedia search
  # Wikipedia main page functions test on mobile

  Scenario: User can search on Wikipedia
    Given HW11 Click to Skip onboarding
    When HW11 Click on search field
    And HW11 Search for Python (programming language)
    Then HW11 Verify first result is Python (programming language)
