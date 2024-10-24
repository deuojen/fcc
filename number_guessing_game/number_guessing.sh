#!/bin/bash

# Build a Number Guessing Game

PSQL="psql -X --username=freecodecamp --dbname=number_guess --no-align --tuples-only -c"

echo "Enter your username:"
read USERNAME

USERNAME_ID=$($PSQL "SELECT user_id FROM users WHERE username = '$USERNAME'")
BEST_GUESS=1001
GAMES_PLAYED=0

if [[ -z $USERNAME_ID ]]
then
  INSERT_USER_RESULT=$($PSQL "insert into users(username, best_guess, games_played) values('$USERNAME', $BEST_GUESS, $GAMES_PLAYED)")
  echo -e "\nWelcome, $USERNAME! It looks like this is your first time here."
else
  BEST_GUESS=$($PSQL "SELECT best_guess FROM users WHERE user_id =$USERNAME_ID")
  GAMES_PLAYED=$($PSQL "SELECT games_played FROM users WHERE user_id =$USERNAME_ID")
  echo -e "\nWelcome back, $USERNAME! You have played $GAMES_PLAYED games, and your best game took $BEST_GUESS guesses."
fi

RANDOM_NUMBER=$(( RANDOM % 1000 + 1))
NUMBER_OF_GUESS=0
GAME_FINISHED=0

GUESS_THE_NUMBER() {
  if [[ ! $1 ]]
  then
    echo -e "\nGuess the secret number between 1 and 1000:"
    read CURRENT_GUESS
    (( NUMBER_OF_GUESS++ ))
  fi

  if [[ $CURRENT_GUESS =~ ^[0-9]+$ ]]
  then
    if [[ $CURRENT_GUESS -eq $RANDOM_NUMBER ]]
    then
      # end game
      (( GAME_FINISHED++ ))
      (( GAMES_PLAYED++ ))
      if [[ $NUMBER_OF_GUESS -lt $BEST_GUESS ]]
      then
        UPDATE_USER_RESULT=$($PSQL "update users set best_guess=$NUMBER_OF_GUESS, games_played=$GAMES_PLAYED where username='$USERNAME'")
      else
        UPDATE_USER_RESULT=$($PSQL "update users set games_played=$GAMES_PLAYED where username='$USERNAME'")
      fi
      echo -e "\nYou guessed it in $NUMBER_OF_GUESS tries. The secret number was $RANDOM_NUMBER. Nice job!"

    elif [[ $CURRENT_GUESS -lt $RANDOM_NUMBER ]]
    then
      # random number is greater
      echo -e "\nIt's higher than that, guess again:"
      read CURRENT_GUESS
      (( NUMBER_OF_GUESS++ ))
    elif [[ $CURRENT_GUESS -gt $RANDOM_NUMBER ]]
    then
      # random number is lesser 
      echo -e "\nIt's lower than that, guess again:"
      read CURRENT_GUESS
      (( NUMBER_OF_GUESS++ ))
    fi
  else
    # not a number
    echo -e "\nThat is not an integer, guess again:"
    read CURRENT_GUESS
    # (( NUMBER_OF_GUESS++ ))
  fi
}

GUESS_THE_NUMBER

until [[ $GAME_FINISHED -eq 1 ]]
do
  GUESS_THE_NUMBER again
done
