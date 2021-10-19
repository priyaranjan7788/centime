# Created by PriyaRanjan at 10/16/2021
Feature: Verify time series API for a given client with Throttle Limit
  # Enter feature description here

  Scenario: Validate user gets time series data with Throttle Limit of 5 request in a min
    Given the company name as "IBM" and function as "TIME_SERIES_DAILY" with outputsize as "null"
    When user submits "5" API request in a time frame of a min for "IBM"
    Then Validates the "5" response is being captured for "IBM"

  Scenario: Validate user gets time series data with Throttle Limit of more than 5 request in a min
     Given the company name as "IBM" and function as "TIME_SERIES_DAILY" with outputsize as "null"
    When user submits "7" API request in a time frame of a min for "IBM"
    Then Validates the "7" response is being captured for "IBM"