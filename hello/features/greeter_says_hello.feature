# Created by mike.girenko at 8/18/20
Feature: greeter says hello

  In order to start learning Behave
  As reader of The RSpec Book
  I want a greeter to say Hello

  Scenario: greeter says hello
    Given a greeter
      When I send it the greet message
      Then I should see "Hello Behave!"