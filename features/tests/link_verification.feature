
Feature: Test scenarios for links


  Scenario: Top logo takes you to home page
    Given Open search results page
    When Click on Cureskin logo
    Then Verify user is on homepage
