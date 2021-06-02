# How to setup the project

Install python3.x 
Install virtualenv

    pip install virtualenv

Activate virtualenv
    
    
    1. virtualenv -p python3 env`
    2. source env/bin/activate

Install all requirements/dependencies

    pip install -r requirements.txt

# Run Main script

To run the task, we need to run below command

    python entry_point.py

# Output

Check `output` folder for filtered users data based on distance by 

# Testing

all the functional tests are writter in `tests` folder

1. To check if the distance is calculated right or not.
2. To Check if the file size is large then we are breaking into small files right or not.
3. To Check if the filtering function is working right or not

in order to run the test cases, run below command

    pytest

