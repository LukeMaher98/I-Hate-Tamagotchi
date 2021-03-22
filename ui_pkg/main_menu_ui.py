import PySimpleGUI as sg

userLayout = [[sg.Text("Welcome to TheAter")],
          [sg.Button('Screenings')],
          [sg.Button('Concessions')],
          [sg.Button('My Bookings')],
          [sg.Button('Logout')]]

adminLayout = [[sg.Text("Welcome to TheAter")],
          [sg.Button('Alter Screenings')],
          [sg.Button('Alter Concessions')],
          [sg.Button('Bookings Review')],
          [sg.Button('View Ticket Sales')],
          [sg.Button('View Concession Sales')],
          [sg.Button('Logout')]]

adminHeading = "TheAter Admin Menu"

userHeading = "TheAter Main Menu"