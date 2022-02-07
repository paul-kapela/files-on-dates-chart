import os
import sys
import time
import pandas
from datetime import date
from pathlib import Path
from plotly import express as plotly

# Variables
data = {
    "date": [],
    "quantity": []
}

directories = []

# Read directories from arguments
if len(sys.argv) < 2:
    print("Podaj katalog")

    exit()
else:
    for directory in sys.argv[1:]:
        if not os.path.exists(directory):
            print("Nieprawidłowy katalog")
            
            exit()
        else:
            directories.append(directory)

# Add directories insidee
for directory in directories:
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            directories.append(os.path.join(root, dir))

# Scan directories for quantity of files
for directory in directories:
    for filename in os.scandir(directory):
        if os.path.isfile(filename):
            file_date = date.fromtimestamp(os.path.getctime(filename))

            if not file_date in data["date"]:
                data["date"].append(file_date)
                data["quantity"].append(1)
            else:
                index = data["date"].index(file_date)
                data["quantity"][index] += 1

# Plot data on a chart
chart = plotly.bar(data, x="date", y="quantity")
chart.show()