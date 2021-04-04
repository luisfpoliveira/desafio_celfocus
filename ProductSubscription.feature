@Regression
Feature: Product Subscription
  To test product subscription the site automatic test framework
  1. Will open https://qa-automation-challenge.github.io/sandbox/
  2. Select type "Special"
  3. Select support plan  "Full"
  4. Choose a duration of 6 months
  5. Click the "Calculate" button
  Expected Result: Price is 2249.10$

  Scenario: Price calculation
      Given The "chrome" browser is open in the URL "https://qa-automation-challenge.github.io/sandbox/"
       When Select "type" "Special"
        And Select "support" "Full"
        And Choose a "duration" of "6" months
        And Click the "calculate" "button"
       Then The text in "price" is "2249.10 $"