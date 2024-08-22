# Created by jkwak at 7/15/24
Feature: context global variable practice
  # Enter feature description here

  Scenario: verify if context object shares data
    When add items in a list in step1
      And add items in a list in step2
      And add step1_items in step2_list
    Then verify all list items in step3
    # Enter steps here