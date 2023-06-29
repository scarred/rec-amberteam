Prerequisites:
1. Python installed (3.7.*)
2. Pip installed

Installing packages:
1. Go to the project root directory (rec-amberteam) and run the following command: pip install -r requirements.txt

To run the tests, run "pytest" command.
WebDriver timeout and browser can be set in config.ini file.

Most operations are logged to files in "logs" directory.

TODO:
- Fix test 4 (assertion fails despite proper trail setup)
- Re-factor
- Fix screenshots on failure
- Support for more browsers