# MCQ Test WebApp
This is an MCQ test portal for conducting MCQ tests online.

## Features of our project

1. Admin can add users,test-setters and questions setters. 
2. The permissions of all the users can be changed by the admin.
3. Admin has access to all the features of other users.
4. Question-setters can add new questions and can edit and delete them.
5. Test-setters create tests ,associate questions with the test,add test's starting time and then add contestants that are eligible for that test.
6. Contestants can Login into the portal and once they click on start test, the timer will start.
7. The progress of the user is saved even if the browser gets closed due to any technical glitch.

## Installation Procedure

1. In terminal cd to the MCQ_Test_WebApp.
```
cd MCQ_Test_WebApp
```
2. Run these commands in terminal.
```
 pip install -r requirements.txt
 python manage.py migrate
 python manage.py makemigrations
 python manage.py migrate
 ```
 
3. Start server using this command in terminal 
```
python manage.py runserver
```

## Steps to run the project
Follow these steps to run the project

### 1. Enter into the portal
After starting the portal a development server will start.
```
base dir path /home/meghna_batra/Videos/MCQ_Test_WebApp/static
base dir path /home/meghna_batra/Videos/MCQ_Test_WebApp/static
Performing system checks...

System check identified no issues (0 silenced).
May 03, 2020 - 20:34:49
Django version 1.11.25, using settings 'MCQ_Portal.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
Enter the URL displayed here into the web browser and this redirect to the home page of the website.
### 2. Create Admin
Create admin by entering this command in terminal
```
python manage.py createsuperuser
```
### 3. Login through admin login page
To go to the admin login.Add "/admin" in the URL.
For Example, here the URL is "http://127.0.0.1:8000/" , so to access admin login the URL will be
```
http://127.0.0.1:8000/admin
```
Now enter the admin login credentials in the login page.
### 4. Create Question-Setters and Test Setters

1. Click on groups and then click on add groups.
2. Create a group giving the permissions accordingly.
3. Then from the homepage, Click on users, and then click on add users.
4. Create username and password for the new user and click on save.
5. Then add groups for the user and check the staff status.
6. Save the changes and new question-setter/Test setter accordingly ad they can login from the same login page as admin.

### 5. Create Questions

1. Click on Questions.
2. Click on Add Questions.
3. Enter the details of the question and click on SAVE.

### 6. Create Test

#### Creating a new test

1. Click on Test.
2. Click on Add test.
3. Enter Numeric Test id, Test name, Test duration and Test URL.
4. Test URL should be the format "tests/test_id" where test id is the test id entered.
5. Save the Test.

#### Associating questions to the test

1. Click on Associations.
2. Click on Add Associatinos.
3. Select the question and the Test that is to be associated and save.

### 7. Adding Users to give Test

To add the Users that are egigible to give the test:

1. Click on Users Test
2. Click on add Users Test 
3. Select the user , and test and enter the start time of the test and Save  

### 8. Attempt the test

1. Enter into the Home Page of the website.
2. Login using the contestant credentials.
3. Start the test and click on submit after finishing the test.

