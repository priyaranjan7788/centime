# Created by PriyaRanjan at 10/16/2021
Feature: Verify time series API for a given client
  # Enter feature description here

  Scenario: Validate user gets time series  data
    Given the company name as "IBM" and function as "TIME_SERIES_DAILY" with outputsize as "null"
    When user execute the AlphaAdvantage API
    Then user captures the data for "IBM" company
    And Validates the response is being captured for "IBM"
    And validates the timeserise is captured for "100" datapoints for "IBM"


  Scenario: Validate user gets time series  data when outputsize is compact
  Given the company name as "IBM" and function as "TIME_SERIES_DAILY" with outputsize as "compact"
  When user execute the AlphaAdvantage API
  Then user captures the data for "IBM" company
  And Validates the response is being captured for "IBM"
  And validates the timeserise is captured for "100" datapoints for "IBM"

  Scenario: Validate user gets time series  data when outputsize is full
  Given the company name as "IBM" and function as "TIME_SERIES_DAILY" with outputsize as "full"
  When user execute the AlphaAdvantage API
  Then user captures the data for "IBM" company
  And Validates the response is being captured for "IBM"
  And validates the timeserise is captured for 20 years for "IBM"
    # Enter steps here