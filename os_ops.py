import os
import subprocess as sp

paths = {
    'visualstudio': 'C:\\Users\\gonre\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_visualstudio():
    sp.Popen(paths['visualstudio'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])     

