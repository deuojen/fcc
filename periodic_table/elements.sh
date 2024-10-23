#!/bin/bash

# Build a Periodic Table Database

PSQL="psql -X --username=freecodecamp --dbname=periodic_table --tuples-only -c"

 

if [[ $1 ]]
then
  ##echo -e "\n$1"
  if [[ $1 =~ ^[0-9]+$ ]]
  then
    ELEMENT_RESULT=$($PSQL "SELECT atomic_number, symbol, name, atomic_mass, melting_point_celsius, boiling_point_celsius, type
      FROM elements left join properties using(atomic_number) left join types using(type_id)
      WHERE atomic_number='$1'")
  else
    ELEMENT_RESULT=$($PSQL "SELECT atomic_number, symbol, name, atomic_mass, melting_point_celsius, boiling_point_celsius, type
      FROM elements left join properties using(atomic_number) left join types using(type_id)
      WHERE symbol='$1' or name='$1'")
  fi
  if [[ -z $ELEMENT_RESULT ]]
  then
    echo "I could not find that element in the database."
  else
    echo "$ELEMENT_RESULT" | while read ATOMIC_NUMBER BAR SYMBOL BAR NAME BAR ATOMIC_MASS BAR MELTING_POINT_CELSIUS BAR BOILING_POINT_CELSIUS BAR TYPE
    do
      echo "The element with atomic number $ATOMIC_NUMBER is $NAME ($SYMBOL). It's a $TYPE, with a mass of $ATOMIC_MASS amu. $NAME has a melting point of $MELTING_POINT_CELSIUS celsius and a boiling point of $BOILING_POINT_CELSIUS celsius."
    done
  fi
else
  echo "Please provide an element as an argument."
fi
