# Created by mike.girenko at 8/18/20
Feature: greeter says Hello!

  Scenario: run a greeter test
    Given greeter exists
      When greeter receives greet() message
      Then greeter says Hello