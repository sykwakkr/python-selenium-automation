# Created by jkwak at 8/7/24
Feature: Test for Youtube watch search
  # Youtube watch search page functions on mobile

  Scenario: User can search on Youtube
    Given HW11 Click search field for watch
    When HW11 Search YouTube for "jinny's kitchen season 2"
    Then HW11 Verify "Jinny's Kitchen Season 2" is found
