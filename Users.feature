@Regression
Feature: Product Subscription
  To test the USERS backend webservices the following tests have to be done
  1. Using Post to 	https://reqres.in/api/users create a user with "User" = "Toy" and "Job" = "Singer"
      Expected Result: User is created.
                        Http status_code = 201.
                        Http Response contains the text "createdAt"
  2. Delete user 2 in the following API https://reqres.in/api/users/${user}
      Expected Result: The user was deleted
                        Http status_code = 204.
  3. Submit a new register without password to https://reqres.in/api/register without password
      and with "email"="challenge@automation.com"
      Expected Result: The register is not successful due to the lack of password
                        Http status_code = 400.
                        Http Response contains the text "Missing password"

  Scenario: 1. User Creation
      Given The API URL "https://reqres.in/api/users"
       When The payload attribute "User" is "Toy"
        And The payload attribute "Job" is "singer"
        And A post to the API is done
       Then The http status code is "201"
        And The text of the http response contains the text "createdAt"

  Scenario: 2. User Deletion
      Given The API URL "https://reqres.in/api/users/%s"
       When The user to be deleted is "2"
        And A delete command is sent to the delete user API
       Then The http status code is "204"


  Scenario: 3. Submit a new register without password
      Given The API URL "https://reqres.in/api/register"
       When The payload attribute "email" is "challenge@automation.com"
        And A post to the API is done
       Then The http status code is "400"
        And The text of the http response contains the text "Missing password"
