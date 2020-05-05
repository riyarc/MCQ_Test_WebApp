# MCQ Test WebApp
This is an MCQ test portal for conducting MCQ tests online.

## Features of our project

1. Admin can add users,test-setters and questions setters. 
2. The permissions of all the users can be changed by the admin.
3. Admin has access to all the features of other users.
4. Question-setters can add new questions and can edit and delete them.
5. Test-setters create tests, associate questions with the test,add test's starting time and then add contestants that are eligible for that test.
6. Contestants can Login into the portal and once they click on start test, the timer will start.
7. The progress of the user is saved even if the browser gets closed due to any technical glitch.

## Installation Procedure

1. Download the project or clone it from github https://github.com/riya-rc/MCQ_Test_WebApp and unzip it.
2. In terminal cd to the MCQ_Test_WebApp.
```
cd MCQ_Test_WebApp
```
3. Run these commands in terminal.
```
 pip install -r requirements.txt
 python manage.py makemigrations
 python manage.py migrate
 ```
 
4. Start server using this command in terminal 
```
python manage.py runserver
```
5. Now go to http://127.0.0.1:8000/ 

## Steps to run the project
Follow these steps to run the project

### 1. Create Admin
1. Create admin by "python manage.py createsuperuser" and enter your details.

### 2. Login through admin login page
1. Go to http://127.0.0.1:8000/admin and login as superuser.

### 3. Create Question-Setters and Test Setters

1. Create users by clicking on groups and then add groups.
2. Create a group giving the permissions accordingly.
3. Add users by clicking on users and adding the details.
4. Then add groups for the user and check the staff status.
6. Save the changes and new question-setter/Test setter accordingly and can login from the same admin interface.

### 4. Create Questions

1. Click on Questions.
2. Click on Add Questions.
3. Enter the details of the question and click on SAVE.

### 5. Create Test

#### 1. Creating a new test

1. Click on Test.
2. Click on Add test.
3. Enter Numeric Test id, Test name, Test duration and Test URL.
4. Test URL should be the format "tests/test_id" where test id is the test id entered.
5. Save the Test.

#### 2. Associating questions to the test

1. Click on Associations.
2. Click on Add Associatinos.
3. Select the question and the Test that is to be associated and save.

### 6. Add the users as contestants

1. Click on contestants and add users, who are eligible of giving tests.

### 7. Adding Users to give Test

To add the Users that are egigible to give the test:

1. Click on Users Test
2. Click on add Users Test 
3. Select the user, and test and enter the start time of the test and Save  

### 8. Attempt the test

1. Enter into the Home Page of the website.
2. Login using the contestant credentials.
3. Start the test and click on submit after finishing the test.
