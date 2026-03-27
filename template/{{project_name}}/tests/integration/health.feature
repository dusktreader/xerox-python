Feature: health endpoint

  Scenario: health check returns no content
    Given the FastAPI test client is ready
    When I GET "/health"
    Then the response status is 204
