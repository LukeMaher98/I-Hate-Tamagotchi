# The-A-Ter
Prerequisites:
    - Python 3 (Possible incompatibilities if -v < 3.9)  
    - PySimpleGui (pip install pysimplegui)  
    - Software Metrics (pip install requests) (see guide below)  

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

Software Metrics:
    - For recording our software metrics we use Loggly  
    - Users will need to run the command "pip install requests"   
    - Follow the guide to send logs to Loggly - https://documentation.solarwinds.com/en/Success_Center/loggly/Content/getting-started/gsg-send_data.html  
    - Users DO NOT need to send logs in order for the program to run correctly.  
    - A link to our dashboard (Only Developers have Access) - https://samuelpf98.loggly.com/dashboards/dashboard/65e60a9c-e6fe-49e4-9749-cb0920f1d648/view  
    
Dev Ops:
    -   User Flow diagrams for several primary use cases  
    -   Overview of adherence to Agile software devlopment principles  
