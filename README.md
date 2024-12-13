I.	PROJECT OVERVIEW
=
   Wildwatcher is a system that allows users to track animal sightings.
   This is a system where users can input information such as the animal name, location, date, and the 
   description of the animal's behavior. Furthermore it’s a user friendly system which allows a wide range 
   of individuals to tell their observations about a specific or certain animal.

   On the other hand the system Wildwatcher allows users to view, manage, and delete their sightings the animals 
   that they've seen. This also includes an account management, which enables users to create and delete their
   accounts if necessary. Therefore the system as a valuable tool for analyzing and studying wildlife behaviors.

           Included Features: 
o	Register and Login System.
o	Viewing, adding and deleting animal sighting.
o	Displaying animal sightings with scroll.

           Excluded Features: 
o	Does not include a gps for automatic location detection for animal sighting.
o	Users can’t upload a photo of the animal sighting.
o	Cannot modify the data that have been inputed.

           Target Users: 
o	Wildlife researchers, rangers, locals and anyone interested in tracking animals.

           Measurable outcomes the project aims to achieve. 
o	Provide a filter for location so that a user can focus on a specific location by Q3 2026.
o	Add a feature where a user can download or export the data by Q4 2025.
o	Reduce the time to input the data by 14.5% through improving the inputting system.


II.	PYTHON CONCEPTS AND LIBRARIES
=

   Python Tkinter
   
The use of Tkinter will allows the user to create a graphical user interface where the user can interact with the 
system with the use of buttons, instead of interacting with the terminal. Tkinter will help users to interact with 
the system even those who are not familiar with programming. Then we have the uses of buttons that will help the user 
to login or record an animal sighting. Wherein we can view the data stored in a much readable format.

By using Tkinter it can present a structure of the interface clearly like the data. Tkinter provides built in widgets like
the buttons, scrollbars, entry boxes, which can save the user the time and effort when putting the data needed in a sighting. 
Therefore makes the system more interactive.

   •	Partial Function from functools, it allows to bind certain function in the system. We can this in action in delete_acc.
   The used of partial is to bind the user to the ask_yes_no function without accidentally calling it. There the button will only work 
   if pressed. 

Sqlite3

The system will use Sqlite3 for data storage in the system Wildwatcher.Sqlite3 will provide a simple way to manage
the database in the system. With Sqlite3 it enables the system to retrieve, delete, and insert data. 
This also help in checking the credentials needed when logging in an account. Sqlite3 is a built in
database system that’s in python, sqlite3 doesn’t required any server like phpmyadmin to run the database in the system.

III.	SUSTAINABLE DEVELOPMENT GOALS
=
SDG 15: LIFE ON LAND

The system falls under SDG 15 because it’s a wildlife
monitoring system that enables the user to monitor the animal's behavior overtime. 
It will help people to raise awareness about the behavior of a animal, 
proving wildlife researcher and rangers a valuable data. While the data that’s been collected 
will provide users information that they needed to know the patterns and behavior of an animal. 
Therefore the system is a simple way that will help anyone in volunteering in wildlife tracking.

IV.	PROGRAM/SYSTEM INSTRUCTIONS
=
1.DOWNLOAD OR CLONE ALL THE FILES

2.MAKE SURE THEY'RE IN THE DIRECTORY/FOLDER

3.RUN PROGRAM

LOGIN AND REGISTER:

•	Login: The user will be asked to login first in the system.

•	Register: New users will be asked to register by providing a name and a password.

DASHBOARD/DATA INPUTING:

•	When login is done the user will then be directed to dashboard or the users can input an animal sighting.

•	Then Adding an animal sighting: input animal name, location, date, and description.

•	View Sighting: Display the data that the user have entered.

•	When deleting a sighting: Users will be asked if they want to delete the sighting if yes then they will put the row of sighting that they want to delete.

DELETING AN ACCOUNT/ACCOUNT MANAGEMENT:

•	Delete Account: if the button is pressed the user will be asked if they want to delete their account. This account is permanent.

DATA MANAGEMENT:

•	Display/Hide Data: Users can toggle if they want to see all of the stored animal sighting.           


