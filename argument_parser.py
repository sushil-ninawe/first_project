import argparse

def calculate_sum(dig_1, dig_2):
  """Calculates the sum of two digits.

  Args:
      dig_1: The first digit (integer).
      dig_2: The second digit (integer).

  Returns:
      The sum of the two digits (integer).
  """
  return dig_1 + dig_2

if __name__ == "__main__":
  # Define the argument parser
  parser = argparse.ArgumentParser(description="Calculate the sum of two digits")

  # Add arguments with default values
  parser.add_argument("--dig_1", type=int, default=0, help="The first digit (default: 0)")
  parser.add_argument("--dig_2", type=int, default=0, help="The second digit (default: 0)")

  # Parse arguments
  args = parser.parse_args()

  # Get the digits from arguments
  dig_1 = args.dig_1
  dig_2 = args.dig_2

  # Calculate and print the sum
  sum = calculate_sum(dig_1, dig_2)
  print(f"The sum of {dig_1} and {dig_2} is: {sum}")
