#########################
# CodeAcademy Self-Learning
# Spring 2023
# Assignment 1
# Eduardo Salinas
#########################


# Function to ask user to input package weight in pounds and does a check to make sure its numerical
def customer_weight_input(prompt):
  prompt = "\n What is the weight of the package that you wish to deliver? \n Enter a number: "
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print(
        "\n Only type in the number of pounds, in numerals, of your package. No letters please. Enter here: ")

# Function to ask user to input shipping choice and does a check to make sure its numerical
def shipping_choice_input(prompt):
  prompt = "\n Type 1 for Ground Shipping. Type 2 for Premium Ground Shipping. Type 3 for Drone Shipping. \n Enter a number: "
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print(
        "\n Only type in the shipping choice number, in numerals, of your package. No letters please. Enter here: ")
      
# Prints the prompt/function to the user of the shipping choice
customer_weight = customer_weight_input(input)
shipping_choice = shipping_choice_input(input)

# Ground shipping calculations
if shipping_choice == 1:
  if customer_weight <= 2:
    ground_shipping_calculations = customer_weight * 1.50 + 20.00
  elif customer_weight >= 2 and customer_weight <= 6:
    ground_shipping_calculations = customer_weight * 3.00 + 20.00
  elif customer_weight >= 6 and customer_weight <= 10:
    ground_shipping_calculations = customer_weight * 4.00 + 20.00
  elif customer_weight > 10:
    ground_shipping_calculations = customer_weight * 4.75 + 20.00

  print(f"The price is ${ground_shipping_calculations}")

# Premium Ground Shipping calculations
if shipping_choice == 2:
  premium_ground_shipping_calculations = 125

  print(f"The price is ${premium_ground_shipping_calculations}")

# Drone shipping calculations
if shipping_choice == 3:
  if customer_weight <= 2:
    drone_shipping_calculations = customer_weight * 4.50
  elif customer_weight >= 2 and customer_weight <= 6:
    drone_shipping_calculations = customer_weight * 9.00
  elif customer_weight >= 6 and customer_weight <= 10:
    drone_shipping_calculations = customer_weight * 12.00
  elif customer_weight > 10:
    drone_shipping_calculations = customer_weight * 14.25

  print(f"The price is ${drone_shipping_calculations}")