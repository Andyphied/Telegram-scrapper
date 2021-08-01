# Telescrapy

## SETUP TELEGRAM APP

1. Visit [my.telegram.org]("https://my.telegram.org/auth") and login

2. Click on API development tools and fill the required fields, for platform select other and ignore the url field

3. On submiting, copy or take note of the required variables as shown in .samaple.env file in project folder. They would be needed at a later time

## HOW TO SETUP

With a python version greater than 3.6 installed, the following steps should be followed to run the script

1. Ensure pip is installed globally and at the recent version

   ```
   -m pip install pip --upgrade
   ```

2. Install python virtual environment

   ```
   pip install virtualenv
   ```

3. Navigate into project folder

4. Create virtual enviroment run

   ```
   virtualenv .venv
   ```

5. Activate virtual environment

   ```
   source .venv/bin/activate
   ```

6. Install required python packages

   ```
   pip install -r requirements.txt
   ```

7. Create .env file

   ```
   cp .sample.env .env
   ```

8. Replace the variables in `env` with correesponding values gotten from telegram

9. Ensure mobile phone is close by before running script

10. Start the script

    ```
    python telescrapy.py
    ```

11. Input passcode sent to your mobile phone either as a text message or as a telegram message from telegram

12. If 2 step Authorization is activated, supply your passeord next and follow the rest of the instructions

### Notes

- Ensure to take out or copy csv file before running script again.
