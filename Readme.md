

## Pre requisites

1. Download and install python version >3.5 --> https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe
2. Make sure you install the following modules:
   2.1 pip install requests
   2.2 pip install json
   2.3 pip install pandas
   2.4 pip install datetime

---

## How to Run?

1. Open Main.py
2. Run the file either in any IDE like VSCode or through command line
3. Give the user inputs when prompted for

---

## Files Description

1. Main.py --> will be the starting point of the program
2. ExceptionHandler.py --> can be used to maintain the custom exceptions that are thrown at any point of time.
3. Utils.py --> can be used for any utility classes that are to be maintained in the code base which is common to the complete project.
4. ResearchPublication.py --> used to maintain all functions/tasks related to research publication api's

---

## Program Design

1. User can just only fetch the queried data in the designed format.
2. User was not given any right to read complete data at any point of time.
3. Exceptions are handled by custom exception handler.(more custom exceptions can be added going forward)
4. All functions related to Research Publication API's are maintained separately.

---

## Program Description

1. function : get_with_retry(url,request_params)
   a. If connection error occurs then it retries 3 times with incremental
   sleep and if not successful then it raises exception
   b. Incase of any other error it raises exception immediately
2. class : ResearchPublication
   It is used to fetch data from the plos.org url and then print the
   detials of publications which are requested by the user
3. function : get_publications_keys():
   a. Public method which is used to get all the keys in the publication object
   b. Response output will be in JSON format
4. function : \_\_get_author_search(self,author_name):
   a. Private method which is used to get the publications by author name
   b. It parses data from the response we get from API GET call
5. function : \_\_get_date_search(self,from_date,to_date):
   a. Private method which is used to get the publications between from data and to date
   b. It parses data from the response we get from API GET call
6. function : \_\_print_data(self,fields_to_display):
   a. Private method which is used to format and print the data and calculate the total score and avg score
   b. This method uses pandas library for displaying the data in the tabular format
7. function : print_formatted_search_data(self,fields_to_display,author_name,from_date,to_date):
   a. Public method which is used to print data in tabular format after certain redirections
   b. User can only access this method

---

## Possible unit test cases

1. TC-1: When no publication data is present
   Incase of absense of the publications data we stop moving ahead as we dont have any data to query upon.
   User info message will be - No data found to perform further actions

2. TC-2: Invalid field names
   When user enters invalid field names then we raise an exception saying 'All the fields entered are not present in the valid set'

3. TC-3: Invalid author name
   When user enters an author name who is not associated with any publication we raise exception saying 'No publications found for your search'

4. TC-4: Invalid date format(from_date/to_date)
   When user enters an invalid date format then we raise an exception saying 'Invalid format entered for date- should be YYYY-MM-DD'

5. TC-5: Connection problem - exception after 3 retries check

   1. turn off your internet.
   2. run the code
   3. code should raise an exception after 3 retries

6. TC-6: Connection problem - continuing smoothly for <3 retries
   1. turn off your internet.
   2. run the code
   3. turn on your internet after retry 1
   4. program should show you the output
