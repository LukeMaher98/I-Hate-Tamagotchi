# I-Hate-Tamagotchi
Prerequisites:
    - Python 3 (Possible incompatibilities if -v < 3.9)  
    - PySimpleGui (pip install pysimplegui)  

How To Run:
    - Copy repository into workspace  
    - run main.py with "python main.py"  

Walkthrough:
    - A user is prompted at the entry ui to login  
    - A regular user can sign up for a new account, or log in if a previous customer  
    - Users will be brought to the user main menu  
    - Here they can:  
        - See current screenings, make bookings for tickets, or purchase them  
        - See the concessions and purchase them  
        - Redeem their bookings to purchase tickets  
    - Admins already have defined accounts and are brought to the admin menu  
    - Here they can:  
        - Alter screenings and concessions  
        - View ticket and concession sales  
        - View current bookings   
    - Users can log out when they are finished  

ADDED VALUE 

Unit Tests:
    - In the same directory used to run the initial program run the unit tests with the following command:
        python -m unittest -v unittests/test_utils.py   
    - The tests should run automatically  
    - Each tests case will print either 'ok' or 'FAIL'  
    - In the case of a failure the actual and expected results will be printed for the user to compare    

