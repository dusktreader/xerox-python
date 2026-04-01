Feature: main module

  Scenario: main produces expected output
    When the main function is called
    Then the output contains "Ritchie Blackmore"
