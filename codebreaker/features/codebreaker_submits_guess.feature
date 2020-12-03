Feature: code-breaker submits guess

  The code-breaker submits a guess of four numbers.  The game marks the guess
  with + and - signs.

  For each number in the guess that matches the number and position of a number
  in the secret code, the mark includes one +. For each number in the guess
  that matches the number but not the position of a number in the secret code,
  a - is added to the mark.

  As a code-breaker
  I want to submit a guess
  So that I can try to break the code

  Scenario Outline: submit guess
    Given the secret code is "<code>"
    When I guess "<guess>"
    Then the mark should be "<mark>"

    Scenarios: no matches
      | code | guess | mark |
      | 1234 | 5555  |      |

     Scenarios: all numbers correct
      | code | guess | mark |
      | 1234 | 1234  | ++++ |