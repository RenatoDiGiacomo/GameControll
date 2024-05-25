from os import system
import subprocess
from app.inputData import inputData


def is_mesen_running():
    # Construct the tasklist command to filter for Mesen.exe
    command = ['cmd', '/c', 'tasklist', '|', 'findstr', 'Mesen']

    # Execute the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True)

    # Check if Mesen.exe is in the output
    return 'Mesen' in result.stdout


def mazenRunning():
    MesenRunning = False
    if is_mesen_running():
        MesenRunning = True
        while MesenRunning:
            if is_mesen_running():
                print("Running")
                inputData()
            else:
                print("Mazen Closed")
                MesenRunning = False

    else:
        system("cls")
        print("Open Mesen Emulator before run it\n\n")
