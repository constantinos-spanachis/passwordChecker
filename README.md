# Password Checker.

An app that allows you to check if your password has been pwned. It uses [this api](https://api.pwnedpasswords.com/range/) 
to send a hashed password that then gets crossed check with the database, and returns the number of times a password has been
pwned. You can either execute the module by adding code underneath it or by installing the package and running it
via the terminal. 

## Installing the app:

To install the app, open a new terminal and then cd to the repostitory that contains the passwordChecker. Then run the 
following command:

```
python setup.py install
```

This will install the python package and it's requirements. 

### Running through the terminal:
To run the password checker and check if your passwords are safe via a terminal, you will have to run the following 
command:

```
check_password -p {password_1} {password_2} {...}
```

The app then collects the passwords you have passed and processes them, and prints the number of times each password has 
been briefed.

### In a python module:

To run the application via a new python module you will have to import the function within your file and then run it 
using a list as your entered parameters which contains the passwords you want to check. Here's a sample code for this:

```python
from password_checker import check_password

list_of_passwords_to_check = [
    "password 1", 
    "password_2",
    "..."
]

check_password(pass_list=list_of_passwords_to_check)
```

You can also import the class that was created for the Password Checker application, by using the following syntax:

```python
from password_checker import PasswordChecker

checker_ = PasswordChecker()

```

## Structure

This package has the code contained within src, and to run any code within that path you will first need to make it your
source repository, by either using the PyCharm Interface, or using your terminal and setting your PYTHONPATH to the 
src path. The code then is split to two sub packages, one for the utils used for this package and one that contains the 
main class, and the code used within the console script.