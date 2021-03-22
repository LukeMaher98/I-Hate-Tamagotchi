import PySimpleGUI as sg

loginLayout = [[sg.Text("Please enter your login details", key='-OUTPUT-')],
          [sg.Text("Username:")],
          [sg.Input(key='-USERNAME-')],
          [sg.Text("Password:")],
          [sg.Input(key='-PASSWORD-', password_char='*')],
          [sg.Button('Confirm'), sg.Button('Signup'), sg.Button('Exit')]]

loginHeading = "TheAter Login"

signupLayout = [[sg.Text("Please enter your login details", key='-OUTPUT-')],
          [sg.Text("Username:")],
          [sg.Input(key='-USERNAME-')],
          [sg.Text("Password:")],
          [sg.Input(key='-PASSWORD-', password_char='*')],
          [sg.Text("Confirm Password:")],
          [sg.Input(key='-CONFIRM-', password_char='*')],
          [sg.Button('Submit'), sg.Button('Login'), sg.Button('Exit')]]

signupHeading = "TheAter Signup"


