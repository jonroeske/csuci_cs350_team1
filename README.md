# CSUCI, COMP-350 Software Engineering
## Developers: Aaron Urrea, Jon Roeske, Zachary Drake, Paul Kime & Connor Moore
### Team One, Spring 2022
## Description:
### The project is to create software for “Gila Breath Camp,” a summer camp for kids, located in a remote, scenic part of the US. The software must support the work of the camp’s registration clerk.
### Task Requirements:
####- Handling documents
####  - applications to camp
####  - payments
####  - notices of acceptance
####  - arrival instruction packets
####- Processing refunds and post-acceptance issues
####- Dealing with “first day” issues
####  - check-in of campers
####  - assignment of campers to bunkhouses
####  - assignment of campers to “tribes”

***

## Objects

### camp.py
This file contains our Camp object, an object which has five attributes: allCampers, juneCampers, julyCampers, augustCampers, and tempCampers.

 **selfCampers represents every single camper within our camp**
>- **self.allCampers:** A list with length equal to 216. (Max campers in a camp)
 
 
 **juneCampers represents the June session.**
 The first list containing every camper in the session; 
 The second list containing every bunkhouse, and every camper in each bunkhouse;
 The third list containing every tribe, and every camper in each tribe.
>- **self.juneCampers:** A list which contains three lists, known respectively as allJuneCampers, allJuneBunkhouses, and allJuneTribes
>  - **self.juneCampers[0]:** A list with length equal to 72. (Max amount of campers in a session)
>  - **self.juneCampers[1]:** A list of 6 lists, (Max bunkhouses) each with length equal to 12. (Max campers in bunkhouse)
>  - **self.juneCampers[2]:** A list of 6 lists, (Max tribes) each with length equal to 12. (Max campers in tribe)

 **julyCampers represents the July session.**
 The first list containing every camper in the session; 
 The second list containing every bunkhouse, and every camper in each bunkhouse;
 The third list containing every tribe, and every camper in each tribe.
>- **self.julyCampers:** A list which contains three lists, known respectively as allJulyCampers, allJulyBunkhouses, and allJulyTribes
>  - **self.julyCampers[0]:** A list with length equal to 72. (Max amount of campers in a session)
>  - **self.julyCampers[1]:** A list of 6 lists, (Max bunkhouses) each with length equal to 12. (Max campers in bunkhouse)
>  - **self.julyCampers[2]:** A list of 6 lists, (Max tribes) each with length equal to 12. (Max campers in tribe)
>
> 
 **augustCampers represents the August session.** 
 The first list containing every camper in the session; 
 The second list containing every bunkhouse, and every camper in each bunkhouse;
 The third list containing every tribe, and every camper in each tribe.
>- **self.augustCampers:** A list which contains three lists, known respectively as allAugustCampers, allAugustBunkhouses, and allAugustTribes
>  - **self.augustCampers[0]:** A list with length equal to 72. (Max amount of campers in a session)
>  - **self.augustCampers[1]:** A list of 6 lists, (Max bunkhouses) each with length equal to 12. (Max campers in bunkhouse)
>  - **self.augustCampers[2]:** A list of 6 lists, (Max tribes) each with length equal to 12. (Max campers in tribe)

 **tempCampers represents a temporary list of all three sessions**
 Each list represents a different session. When a camper has been assigned a sesison, but has not been accepted, they will be added to one of these three lists.
 When a camper is finally accepted, they will be removed from this list and added to the above lists.
>- **self.tempCampers:** A list which contains three lists, known respectively as tempJuneCampers, tempJulyCampers, and tempAugustCampers
>  - **self.tempCampers[0]:** A list with length equal to 72. (Max amount of campers in a session)
>  - **self.tempCampers[1]:** A list with length equal to 72. (Max amount of campers in a session)
>  - **self.tempCampers[2]:** A list with length equal to 72. (Max amount of campers in a session)

***

### camper.py
This file contains our Camper object, which contains the following attributes:

> **self.name:** The camper's name; Type: String
> 
> **self.age:** The camper's age; Type: Int
> 
> **self.gender:** The camper's gender; Type: String
> 
> **self.address:** The camper's address; Type: String
> 
> **self.hasPartner:** Identifier if the camper has a partner; Type: Bool
> 
> **self.partner:** The camper's partner; Type: Camper
> 
> **self.session:** The camper's assigned session; Type: Int
> 
> **self.bunkhouse:** The camper's assigned bunkhouse; Type: Int
> 
> **self.tribe:** The camper's assigned tribe; Type: Int
> 
> **self.checkedIn:** Identifier if the camper has a partner; Type: Bool
> 
> **self.appNoticeIsSent:** Identifier if the camper has had an acceptance notice sent; Type: Bool
> 
> **self.dateAppNoticeSent:** The date the camper's acceptance notice was sent; Type: datetime.Date
> 
> **self.materials:** The various materials of the camper; Type: Materials

*** 

### materials.py
This file contains our Materials object, a sub-object for the Camper object. Materials contains the following attributes:

> 
> **self.medical:** Identifier if the camper has completed medical forms; Type: Bool
>  
> **self.legal:** Identifier if the camper has completed legal forms; Type: Bool
>  
> **self.emergencyContacts:** Identifier if the camper has emergency contacts; Type: Bool
>  
> **self.helmet:** Identifier if the camper has a helmet; Type: Bool
>  
> **self.boots:** Identifier if the camper has boots; Type: Bool
>  
> **self.sleepingBag:** Identifier if the camper has a sleeping bag; Type: Bool
>  
> **self.waterBottle:** Identifier if the camper has a water bottle; Type: Bool
>  
> **self.sunscreen:** Identifier if the camper has sunscreen; Type: Bool
>  
> **self.bugSpray:** Identifier if the camper has a bug spray; Type: Bool

***

### values.py
This is where we hold various dictionaries and static values to be used across the program as a whole:

 **STATUS_CODES is a dictionary of various status codes:**
> **SUCCESS**
> 
> **NO_CAMPER**
> 
> **NO_CAMPER_SESSION**
> 
> **NO_CAMPER_BUNKHOUSE**
> 
> **NO_CAMPER_TRIBE**
> 
> **NO_SESSION**
> 
> **NO_BUNKHOUSE**
> 
> **NO_TRIBE**
> 
> **NO_CAPACITY**
> 
> **DUPLICATE**
> 
> **ARGUMENT_ERROR**

 **GLOBAL_VALUES is a dictionary of various values:**
> **maxCampersTotal**
> 
> **maxCampersInSession**
> 
> **maxGendersInSession**
> 
> **maxBunkhouses**
> 
> **maxCampersinBunkhouse**
> 
> **maxTribes**
> 
> **maxCampersInTribes**

 **TODAYS_DATE represents a date, which can be manipulated to represent a different point in time**

 **JUNE_SESSION_DATE represents a static date: June 6, 2022**

 **JULY_SESSION_DATE represents a static date: July 4, 2022**

 **AUGUST_SESSION_DATE represents a static date: August 8, 2022**

 There are also three different sort keys that we use elsewhere in the project:
> **sortByName(camper):** Returns "", else camper.name 
> 
> **sortByAge(camper):** Returns "", else camper.age
> 
> **sortByAssignmentRequest(camper):** Returns "", else camper.getHasPartner

***

## Handlers

#### dataHandler.py
This is the file we use for managing the persistent data of our application. Within it are two functions with the following purposes:

- **initializeData():**
 >This will load data from our database folder to be used in the application. 
 >If there are valid .pickle files within our database folder, the function will load the contents of the files into our Camp object summerCamp, which is used globally throughout the application. 
 >If there are no files, or missing files, those files will be created. 


- **shutDown():** 
 >This will load data from our summerCamp Camp object into the four files within our database.

***

#### uiHandler.py
This is the file we use for managing the UI of our application. Within it are nine functions with the following purposes:

- **mainMenu():** 
 >Prints the Main Menu UI.


- **camperSubMenu():** 
 >Prints the Camper Sub-Menu UI.


- **debugSubMenu():** 
 >Prints the Debug Sub-Menu UI.


- **showCredits():** 
 >Prints the credits of the team which developed this program.


- **showVersion():**
 >Prints the current version number of the project. This is stored in a variable known as "versionNumber".


- **clearScreen():** 
 >Clears the screen. Implementation checks for the OS of the system, so this works on Unix and Windows systems.


- **showMessage(message, kwargs):** 
 >This will print a message according to the arguments located in **kwargs.
 >The parameter "message" itself can be either a singular string, or a list of strings. 
 >In the case of a list of strings, it will print every string in the list for each line. 
 >Else, it will print a singular message. Kwargs has three arguments which can also affect how the function prints:
 > - _"topBracket":_ Will print a bracket at the top of the message.
 >
 > - _"bottomBracket":_ Will print a bracket at the bottom of the message.
 > 
 > - _"wait":_ Will time.sleep() for the integer value within kwargs["wait"].


- **showPrompt(message, kwargs):** 
 >This will print a message, as well as prompting the user for an input depending on its purpose. 
 >The function will then return the input. The parameter "message" itself can be either a singular string, or a list of strings. 
 >In the case of a list of strings, it will print every string in the list for each line. Else, it will print a singular message. 
 >Kwargs has three arguments which can also affect how the function prints:
 > - _"topBracket":_ Will print a bracket at the top of the message.
 > 
 > - _"bottomBracket":_ Will print a bracket at the bottom of the message.
 > 
 > - _"prompt":_ This is an optional message, with the exact same specifications of "message". 
 >  It will be printed below the message with special formatting.


- **printCamperUI(camper, kwargs):** 
 >This will print relevant information about a camper object that is given. 
 >If there is not a camper instance, or there are no kwargs arguments, then it will return. 
 >Kwargs has several arguments which can also affect how the function prints:
>
 > - _"topBracket":_ Will print a bracket at the top of the message.
 > 
 > - _"bottomBracket":_ Will print a bracket at the bottom of the message.
 > 
 > - _"camperCreation":_ This will print out the basic information of the camper. This is used solely for when a new Camper object is created.
 > 
 > - _"attribute":_ This will print camper information based on the attribute argument. The following attribute arguments are as follows:
 >   - _"applicationStatus":_ This will print the status of the camper's application. ("Pending", "Approved", or "Rejected)
 >   - _"appNotice":_ This will print the date that the camper received their acceptance notice. If the camper has not been accepted, it will print N/A.
 >   - _"balance":_ This will print the camper's current balance.
 >   - _"bunkhouse":_ This will print the camper's current bunkhouse.
 >   - _"checkedIn":_ This will print the camper's check-in status.
 >   - _"hasPartner":_ If the camper has a partner, this will print the partner's full name.
 >   - _"materials":_ If the camper has an initialized Materials object, it will print the status of the Material's attributes. 
 >    (Medical, Legal, Emergency Contacts, Helmet, Boots, Sleeping Bag, Water Bottle, Sunscreen, Bug Spray). If not, it will print N/A.
 >   - _"session":_ If the camper has a session, it will print the session. If not, will print "None".
 >   - _"sessionDate":_ If the camper has a session, it will print the date that the session begins.
 >   - _"tribe":_ This will print the camper's current tribe.
 >   
 > - _"simple":_ This will print the camper's name, and if the camper has a partner, will print the partner's name:
 > 
 > - _"detailed":_ This will print ALL relevant info about the camper:
 >   - *Name*
 >   - *Partner* (If the camper has a partner)
 >   - *Age*
 >   - *Gender*
 >   - *Address*
 >   - *Balance*
 >   - *Application Status*
 >   - (If appStatus is Approved)
 >     - *Date of Acceptance*
 >     - *Materials*
 >     - *Check-In Status*
 >     - *Session* (If camper has session)
 >     - *Bunkhouse* (If camper has bunkhouse)
 >     - *Tribe* (If camper has Tribe)

***

### Main Menu
#### The Main Menu of our program, which has access to several categories of commands, as well as access to our two sub menus.

***

#### camperCommands.py
This is the file we use for creation, deletion, and displaying of individual and all campers within our database. Within are four functions:

- **signUpCamper():** 
 >This will prompt the user to input a name, age, gender, and address. 
 > - If any are incorrectly inputted, the user will be prompted to try again, ensuring that they are able of creating a camper with input mistakes. 
 > - Once all four attributes are assigned, the user will be displayed the camper, and asked if they would like to continue creation. 
 > - If yes, then the camper will be created and added to the "allCamper" list in summerCamp. 
 > - If not, then the user will be prompted if they would like to try again. If yes, the process will repeat, if not, will exit to the main menu.


- **withdrawCamper():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to main menu. 
 > - If the camper has made payments, (balance < 1000) return to main menu, else the camper in question will be displayed with all detail.
 > - The user will be prompted if they would like to continue with deletion. If yes, the camper is removed from all lists in summerCamp, else return to main menu.


- **printCamper():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to main menu. 
 >It will then print all relevant data attached to the camper.


- **printAllCampers():** 
 >This will print ALL campers in summerCamp. It will only display the campers name, and if applicable, the name of the camper's partner. 
 >It will also count the composition of males/females and total number of campers

***

#### financialCommands.py
This is the file where we can view a camper's balance, process payments and process refunds. There are three central functions within this file:

- **viewBalance():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to main menu.
 >It will then print the balance of the current camper.


- **processPayment():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to main menu.
 > - If the camper's balance is equal to 1000, print that no payments were made, then return to main menu.
 > - Else, prompt the user for how much they would like to pay. If the payment is greater than 1000, automatically set balance to 0.
 > - Else, set balance to the current balance minus their input. Then print balance and return to main menu.


- **processRefund():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to main menu.
 >- If the camper's balance is equal to zero, print that the balance is fully paid, then return to main menu.
 >- Else, if the user was never sent an acceptance letter, prompt that a full refund it in order. 
 >- Else, if the user was sent an acceptance letter, they will recieve a percentage based on the time difference:
 >  - 90% if within three weeks of notice,
 >  - 45% if within six weeks of notice,
 >  - None if greater than six weeks
 >- Prompt, and assign if yes or exit if no.

***

#### sessionsCommands.py

- **viewSessions():**
>This will print all campers within every session, as well as showing gender composition and total amount of campers.


- **viewBunkhouses():** 
 >This will prompt the user to select a session. This will print all bunkhouses within that session, along with campers within every bunkhouse, 
 >as well as showing gender composition and total amount of campers.

- **viewTribes():** 
 >This will prompt the user to select a session. This will print all tribes within that session, along with campers within every tribe, 
 >as well as showing gender composition and total amount of campers.

***

### Camper Sub-Menu
#### This sub menu will allow us to further manipulate our campers, their assignment, and their status.

***

#### applicationCommands.py
This is the file for managing camper applications, such as the ability to view, accept, or reject any application. Within it holds three functions:

- **viewCamperApplication():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to camper menu. 
 >It will then print the status of the camper's application, then return to camper menu.


- **acceptCamperApplication():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to camper menu. 
 > - If the camper has already been accepted, will print status and return to camper menu.
 > - If the camper has already been rejected, will print status and return to camper menu.
 > - If the camper hasn't selected a session they'd wish to join, return to camper menu.
 > - If the camper is applying less than two months before their desired session, return to camper menu.
 > - If the camper is applying more than eight months before their desired session, return to camper menu.
 > - If the camper has an unpaid balance, return to camper menu.
 > 
 >FINALLY, we will prompt whether the user will be accepted. If yes, remove from temporary session list and assign to actual session list.


- **rejectCamperApplication():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to camper menu. 
 >We will prompt whether the user will be rejected. If yes, remove from temporary session list. Since the camper is rejected, they will no longer be able to be accepted again.
 >The camper must be recreated . 

***

#### assignmentCommands.py
This is the file that allows for the assignment of a camper to a session, bunkhouse, and tribe. This file also offers the ability to process a pair request between two campers. There are four distinct functions:

- **assignCamperToSession():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to camper menu. 
 > - If the user has a session and the user has been accepted, then print their application status, as well as return to camper menu.
 >   - In the event that the clerk resets the sessions, we're going to need a way to reassign already accepted campers to other sessions. This logic respects that.
 > 
 >We will then print the sessions, as well as their availability. Then we will prompt the user to select a session
 >- If todaysDate is less than two months away from the session start date, try again
 >- If there is not enough availibity in the session, try again
 >
 >We will then set the users session to the session, then add the user to the session list in summerCamp.


- **assignCamperToBunkhouse():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to camper menu. 
 >   - If the user has not been accepted, then print their application status, as well as return to camper menu.
 >   - If the user does not have a session, return to camper menu
 >   - If the user is not checked in, return to camper menu
 >   - If the user already has a bunkhouse, ask if they'll like to change bunkhouses. If yes, continue, if not return to camper menu.
 >   
 > We will then print the bunkhouses, as well as their availability. Then we will prompt the user to select a bunkhouse.
 > NOTE: The bunkhouses are gender specific, so there is no cross-gender assignment.
 > - If there is not enough availibity in the bunkhouse, try again
>
 > We will then set the users bunkhouse to the bunkhouse, then add the user to the session's bunkhouse list in summerCamp.


- **assignCamperToTribe():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to camper menu. 
 >   - If the user has not been accepted, then print their application status, as well as return to camper menu.
 >   - If the user does not have a session, return to camper menu
 >   - If the user is not checked in, return to camper menu
 >   - If the user already has a bunkhouse, ask if they'll like to change bunkhouses. If yes, continue, if not return to camper menu.
 >   
 > We will then print the tribes, as well as their availability. Then we will prompt the user to select a tribe.
 > - If there is not enough availibity in the tribe, try again
>
 > We will then set the users tribe to the tribe, then add the user to the session's tribe list in summerCamp.

***

#### firstDayCommands.py
This file allows us to view the acceptance notice date of a camper, to allow them to fill out required forms, and to check them in. It has three functions:

- **viewAcceptanceNoticeStatus():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to camper menu. 
 >If the camper is not accepted, return to camper menu.
 >Else, print the status and date of the camper's acceptance notice


- **fillOutForms():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to camper menu. 
 >It will then create a materials object for the camper object, if one does not already exist.
 >It will then prompt yes or no questions for the following materials:  - Medical Forms
 > - Legal Forms
 > - Emergency Contacts
 > - Helmet
 > - Boots
 > - Sleeping Bag
 > - Water Bottle
 > - Sunscreen
 > - Bug Spray
 >
 >If user inputs yes, then set material to True, else remind the user they must complete before check in.
 >Once complete, it will print the forms status to the user, then return to camper menu.
 >NOTE: The camper may return to fill out other forms at a different times. Only incomplete forms will be prompted.


- **checkInCamper():** 
 >This will prompt the user for a name, at which if "allCampers" contains the camper, then the camper will be selected, else return to camper menu. 
 > - If the camper is not accepted, return to camper menu.
 > - If the camper does not have materials, or has incomplete materials, print materials and return to camper menu.
 > - If the user has an outstanding balance, (balance > 0) print balance and return to camper menu
 > 
 > After all that, set the camper to checked in, then return to menu.

### Debug Sub-Menu
#### This menu is used for testing and debugging primarily. In a real clerk program, this section would not be included.

***

#### automationCommands.py
This file was to be used to automatically assign campers to sessions, bunkhouses, and tribes. Due to time constraints, as well as difficult algorithms to create, it was scrapped in final release.

***

#### debugCommands.py
This file is used to print debug information regarding the lists located in summerCamp. It is pretty self-explanatory.

***

#### populationCommands.py
This file is used to edit the population of the different lists stored within summerCamp. It has five distinct files:

- **populateMaxCampers():** 
 >Using random and faker, we will populate every slot within our "allCampers" list that does not have a camper.
 >The camper's name, age, address, and gender will be randomly generated, but there will always be an equal amount of Males and Females.
 >Here, we also find every camper with the same last name. They then have a 1/4 chance of being partners, given they are the same gender.


- **resetAllCampers():** 
 >Very simply, this reinitializes summerCamp, to be completely empty


- **resetAllSessions():** 
 >This goes through every session, (June, July, August) and every camper encountered, they will have their session, bunkhouse, and tribe set to False
 > They will then be updated.
 > Finally, all sessions will be reinitialized


- **resetAllBunkhouses():** 
 >This goes through every session, (June, July, August) and every camper encountered, they will have their bunkhouse set to False
 > They will then be updated.
 > Finally, all bunkhouses will be reinitialized


- **resetAllTribes():** 
 >This goes through every session, (June, July, August) and every camper encountered, they will have their tribe set to False
 > They will then be updated.
 > Finally, all tribes will be reinitialized

***

#### timeCommands.py
This file is used to manipulate time, which is an important aspect when it comes to camper applications and refunds. It has two functions:

- **changeTodaysDate:** 
 >This will edit the value TODAYS_DATE to a date in datetime format. This will then be reflected across the application, and used in calculations.


- **resetTodaysDate:** 
 >This will edit the value TODAYS_DATE to the current date in datetime format. This will then be reflected across the application, and used in calculations.
