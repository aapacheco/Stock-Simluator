# Stock Simluator
This Python application reads stock information from a CSV file using threads to parse it. The program allows for multiple threads to be run in parallel, each processing a subset of the CSV data to improve performance.

## Installation
To use this program, follow these steps:

1. Clone this repository to your local machine.
2. Install Python 3 and the required dependencies.
3. Open a command prompt or terminal window and navigate to the project directory.
4. Run the command python stock_info.py to start the program.

## Usage
To use the program, follow these steps:

1. The program reads in a CSV file that represents the stock information.
2. The program prompts the user to enter the number of threads to use for processing the data.
3. The program then creates the specified number of threads and assigns each thread a subset of the data to process.
4. Each thread parses its assigned data and calculates the average closing price for each symbol.
5. The program outputs the average closing prices for each symbol.

## Technologies Used
This program uses the following technologies:

* Python 3 for the programming language
* Python csv and os libraries for reading and writing to the csv files
* Threading library for creating and managing threads

## Credits
This program was created by Anthony Pacheco. If you have any questions or issues with the program, please contact me at aapacheco94@gmail.com.
