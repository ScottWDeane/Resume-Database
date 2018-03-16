# Resume-Database
HOW-TO:
Using PGAdmin4, create an empty database named "rentMapRaw.db".
Run "inputProgram.py" to create the connection and create the table "resumeTable".
Use the UI to view, create, modify, delete, and search for entries. Whenever you create, update, or delete an entry, the list is refreshed.
Once done, press the "close" button OR the X in the top-right on the menu bar to close the program.

Run the "website.py" program.
This will create a new file in the directory called "RentMapHTML.html"
Open this file "RentMapHTML.html" in chrome. Other browsers not tested.
You will now have an interactive map showing you pins on a map of where your 

EXPLANATION:
The program is three scripts.

These scripts are "inputProgram.py", "backend.py", and "website.py".

The "inputProgram.py" program imports the code from "backend.py", runs it, then proceeds to run itself.

When "inputProgram.py" runs, it executes the "connect()" function inside the "backend.py" script, which attempts to establish a connection to the database object named "rentMapRaw.db". It then uses SQL to check to see if the table "resumeTable" exists. If it does exist, then the program continues. If the table "resumeTable" does NOT exist, then the program creates the table filling it with empty columns named:  companyName, jobTitle, wantedReq, address, salary, avgRent, distance, status. Some are text, some are integers.

After the connection to the database and the verification that the table "resumeTable" exists within the database, the program generates the UI according to the code in "inputProgram.py" using the "tkinter" library and the "grid" methods from within the "tkinter" module for organization.

This UI uses the "tkinter" library to connect methods to the clickable buttons, which activate various SQL commands. You click a button, and the corresponding SQL code runs for you. All changes are saved automatically, no need to worry about lost progress.

The "second" part of the program, "website.py", uses the libraries "folium", "pandas", and "geopy" in order to process the database you created in the previous program. The script "website.py" connects to the database named "rentMapRaw.db", imports all the data into a "pandas" dataframe object, and generates a few new columns inside the dataframe. These are named "coordinates", "latitude", and "longitude". The script then uses geopy to convert the address given from the script "inputProgram.py" and populate the "latitude" and "longtitude" columns with the proper data. 

The program creates a map using the standard "Mapbox Bright" tiles for a base. Using both the original data from "inputProgram.py" and the new generated "latitude" and "longtitude" data, the program then creates a series of "folium" markers to put on the base map. These markers are interactable, and will display the relevant information about that location. This includes all the data in the dataframe object about that particular location: the company name, job title, wanted requirements, the address, the offered salary, the average rent, the distance, and the application status.

~Scott
