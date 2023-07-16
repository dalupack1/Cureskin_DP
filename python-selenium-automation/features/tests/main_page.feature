
Feature: Test scenarios for main page


  Scenario: Top logo takes you to home page
    Given Open Cureskin main page
    When Click on cart
    And Click on logo
    Then Verify user is on homepage
