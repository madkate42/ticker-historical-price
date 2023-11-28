# Ticker data 

get like market caps or whatever or like your stuff idk. you wanted price history or whatever.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed the latest version of `Python`
* You have a `<Windows/Linux/Mac>` machine. State if the guide works on any other platform additionally or specifically.

## Setting Up the Python Virtual Environment

To setup the virtual environment, follow these steps:
1. Open your terminal/command prompt.
2. Navigate into the project directory.

To create a virtual environment, run:
```
python3 -m venv ./venv
```
Or, if you're on windows:
```
py -3 -m venv ./venv
```

To activate the virtual environment, on Linux/macOS, run:
```
source venv/bin/activate
```
On Windows, run:
```
venv\Scripts\activate
```
Your terminal will now show the name of your venv, something like this `(venv) $:`, indicating that the virtual environment is now active.

## Installing dependencies
Once the environment is activated, install the project dependencies with:
```
pip install -r requirements.txt
```
It will install all the required packages and libraries stated in `requirements.txt` file in your project.

## Running the code
After installing the dependencies, you can run the program with:
```
python <filename.py>
```
Replace `<filename.py>` with the name of the python file that you want to run.

To exit from the virtual environment, run the following command in your terminal:
```
deactivate
```

### How to use the programs
You can just ask me but. `market_cap.py` gets history of market caps for a ticker, `pdr.py` is where all the stuff is, you find out how to use it yeah?
