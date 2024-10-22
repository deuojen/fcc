#!/bin/bash

# Salon Appointment Scheduler

echo -e "\n~~~~~ MY SALON ~~~~~\n"

PSQL="psql --username=freecodecamp --dbname=salon --no-align --tuples-only -c"

SERVICES="$($PSQL "SELECT * FROM services")"

SERVICE_FOUND=0
SERVICE_NAME=0

GET_SERVICE() {
  if [[ ! $1 ]]
  then
    echo -e "Welcome to My Salon, how can I help you?\n"
    echo $SERVICES | sed 's/ /\n/g; s/\|/) /g' -E
  else
    echo -e "\nI could not find that service. What would you like today?"
    echo $SERVICES | sed 's/ /\n/g; s/\|/) /g' -E
  fi
  read SERVICE_ID_SELECTED

  # get service_id
  SERVICE_ID=$($PSQL "select service_id from services where service_id='$SERVICE_ID_SELECTED'")
  # if not found
  if [[ $SERVICE_ID > 0 ]]
  then
    # set found to finish the loop
    SERVICE_FOUND=$SERVICE_ID
    SERVICE_NAME=$($PSQL "select name from services where service_id='$SERVICE_ID'")
  fi
}

GET_SERVICE

until [[ $SERVICE_FOUND > 0 ]]
do
  GET_SERVICE again
done

echo -e "\nWhat's your phone number?"
read CUSTOMER_PHONE
CUSTOMER_ID=$($PSQL "select customer_id from customers where phone='$CUSTOMER_PHONE'")
# if not found
if [[ -z $CUSTOMER_ID ]]
then
  echo -e "\nI don't have a record for that phone number, what's your name?"
  read CUSTOMER_NAME
  # insert customer
  INSERT_CUSTOMER_RESULT=$($PSQL "insert into customers(phone, name) values('$CUSTOMER_PHONE', '$CUSTOMER_ID')")
  # get new customer_id  
  CUSTOMER_ID=$($PSQL "select customer_id from customers where phone='$CUSTOMER_PHONE'")
else
  CUSTOMER_NAME=$($PSQL "select name from customers where phone='$CUSTOMER_PHONE'")
  CUSTOMER_ID=$($PSQL "select customer_id from customers where phone='$CUSTOMER_PHONE'")
fi

echo -e "\nWhat time would you like your $SERVICE_NAME, $CUSTOMER_NAME?"
read SERVICE_TIME

# insert appoinment
INSERT_CUSTOMER_RESULT=$($PSQL "insert into appointments(customer_id, service_id, time) values('$CUSTOMER_ID', '$SERVICE_ID', '$SERVICE_TIME')")

echo -e "\nI have put you down for a $SERVICE_NAME at $SERVICE_TIME, $CUSTOMER_NAME."