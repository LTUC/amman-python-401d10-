# Lab: Ten Thousand - version 1

## Overview

Today you'll begin working in pairs on a command line version of the dice game `Ten Thousand` by expanding your understanding of Python standard library.
- This will be a unique experience as you will be expected to use code from the internet (chatGPT)
  - This will enhance your ability to read and understand code written by others.
- In addition to your README.md, you will create a chatgpt.md file. This file will include:
  - The prompt that you used to generate code
  - the actual code you got from ChatGPT.
  - any subsequent prompts that you ask for changes.
  - NOTE: Failure to provide this file will result in your assignment not being graded and if not submitted on time will be late.

## Feature Tasks and Requirements

- Project named `ten-thousand`.
- Today is all about tackling the highest risk and/or highest priority features - **scoring** and **dice rolling**.
  - Define a `GameLogic` class in `ten_thousand/game_logic.py` file.
  - Handle calculating score for dice roll
    - Add `calculate_score` static method to GameLogic class.
    - The input to `calculate_score` is a tuple of integers that represent a dice roll.
    - The output from `calculate_score` is an integer representing the roll's score according to **rules of game**.
  - Handle rolling dice
    - Add `roll_dice` static method to GameLogic class.
    - The input to `roll_dice` is an integer between 1 and 6.
    - The output of `roll_dice` is a tuple with random values between 1 and 6.
    - The length of tuple must match the argument given to `roll_dice` method.

- Using the parameters above, use ChatGPT to generate code blocks.
  - You must document every single line of code with a **detailed** description of what the code is doing.
- Run the provided tests against the code that you obtained from ChatGPT.
- The provided tests are the source of truth
- NOTE: ChatGPT does not always provide the correct code.
  - Be specific with your requests to ChatGPT.

## Implementation Notes

- Review [rules of game](https://en.wikipedia.org/wiki/Dice_10000){:target="\_blank"}
- Play game [online](http://www.playonlinedicegames.com/farkle){:target="\_blank"}

### User Acceptance Tests

- Starter tests will be provided that cover cases listed below
  - All tests must pass as written
  - But additional tests are expected

#### Testing - Roll Dice

- When rolling 1 to 6 dice ensure...
  - A sequence of correct length is returned
  - Each item in sequence is an integer with value between 1 and 6

#### Testing - Calculate Score

***NOTE*** If there are differences between testing scores and online, the **tests** will be considered correct.

- zilch - roll with no scoring dice should return 0
- ones - rolls with various number of 1s should return correct score
- twos - rolls with various number of 2s should return correct score
- threes - rolls with various number of 3s should return correct score
- fours - rolls with various number of 4s should return correct score
- fives - rolls with various number of 5s should return correct score
- sixes - rolls with various number of 6s should return correct score
- straight - 1,2,3,4,5,6 should return correct score
- three_pairs - 3 pairs should return correct score
- two_trios - 2 sets of 3 should return correct score
- leftover_ones - 1s not used in set of 3 (or greater) should return correct score
- leftover_fives - 5s not used in set of 3 (or greater) should return correct score

## Stretch Goals

- Research `parametrized tests` in PyTest
- Research `Behavior Driven Development`

## Configuration

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="\_blank"} for detailed instructions.
