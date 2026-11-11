Feature: info endpoints

  Background:
    Given the FastAPI test client is ready

  Scenario: config endpoint returns settings
    When I GET "/info/config"
    Then the response status is 200
    And the response body is valid JSON

  Scenario: stats endpoint returns stats
    When I GET "/info/stats"
    Then the response status is 200
    And the response body is valid JSON
