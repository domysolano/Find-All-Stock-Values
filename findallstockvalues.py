import re

# Extract stock values from a text file.

# Parameters: file_path (str): Path to the file, encoding (str): File encoding (default: "latin-1")
# After getting errors while running, it was found txt input file had specific encodigns, later known to be latin-1 encoding.
# Latin-1 encoding is common for Spanish text and the file is in spanish.
# latin-1 and  ISO-8859-1 are the same.

# Returns: a list: List of extracted stock values as strings since no math is going to be computed at this time

def extract_stock_values(file_path, encoding="latin-1"):

    # Read the file with specified encoding
    with open(file_path, "r", encoding=encoding) as file:
        content = file.read()

    # Regular expression to find all stock values
    pattern = r'Valor actual: \$(\d+\.?\d*)'

    # Find all matches using all "content" file
    stock_values = re.findall(pattern, content)

    return stock_values #the list having all the stock values

# Parameters: stock_values (list): List of stock values as strings
 # Print formatted stock value results.
 # $ is not capture by regex, so it is literally printed by print()

def print_stock_results(stock_values):
    print("Extracted Stock Values:")
    for i, value in enumerate(stock_values, 1):
        formatted_value = float(value) # Convert to float
        print(f"{i:2}. ${formatted_value:.2f}") # number the stock values and format stock values to 2 decimal places

# Since the output is long, after printing the summary values, it stops outputting to view the results until the user presses Enter.

def wait_for_enter(prompt="Press Enter to continue..."):
    print(f"\n{prompt}")
    input()

def main():

   # File path, txt file is in ClassFiles folder as requested.

    file_path = "informe_acciones.txt"

    stock_values = extract_stock_values(file_path)     # Extract stock values

    print(f"\nTotal values found: {len(stock_values)}") # Use the above returned value for printing the total of stock values found

    print("Colab (not so jupyter) prints a yellow message telling us it is going to print just THE LAST 5000 values since output is too long")
    wait_for_enter("\n📋 Press Enter to view ALL extracted stock values...\n")

    print_stock_results(stock_values)  # Print all stock values
    print(f"\nTotal values found: {len(stock_values)}") #printed twice just in case you cannot see the total at the beginning because of the long output

if __name__ == "__main__":
  main()