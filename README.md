#Supermarket Checkout Using Python OOP concept by Dheeraj

This project implements a Agritech Supermarket Checkout Assignment process that calculates the total price of items added to the cart by the customer. It supports individual pricing and special offers for bulk purchases. The project now includes a FastAPI application to interact with the checkout system.

## Setup

1. Ensure you have Python 3.7 or later installed on your system.
2. Clone this repository or download the project files.

### Setting up a Virtual Environment

It's recommended to use a virtual environment for this project. Here's how to set it up:

1. Open a terminal and navigate to the project directory.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the FastAPI Application

1. Ensure your virtual environment is activated.
2. Run the following command:
   ```
   uvicorn app.main:app --reload
   ```
3. The API will be available at `http://localhost:8000`.

## API Endpoints

- POST `/checkout`: Calculate the total price for a given list of items
- GET `/run_tests`: Run all tests and return the results
- GET `/pricing_rules`: Get the current pricing rules

## Running Tests

1. Ensure your virtual environment is activated and you have installed the requirements.
2. Run the tests using the following command:
   ```
   pytest
   ```

## Docker Support

To run the application in a Docker container:

1. Ensure you have Docker installed on your system.
2. Build the Docker image:
   ```
   docker build -t supermarket-checkout-by-dheeraj .
   ```
3. Run the Docker container:
   ```
   docker run -p 8000:8000 supermarket-checkout-by-dheeraj
   ```
4. The API will be available at `http://localhost:8000`.

## Project Structure

- `app/`: Contains the main application code
  - `main.py`: FastAPI application
  - `checkout.py`: Main implementation of the checkout system
  - `models.py`: Pydentic Models
  - `test_checkout.py`: Unit tests for the checkout system
- `Dockerfile`: Instructions for building a Docker image of the application
- `README.md`: This file, containing setup and usage instructions
- `requirements.txt`: List of Python dependencies for the project

