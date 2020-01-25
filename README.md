# Flask Application with CORs Logic

Simple application that highlights the use of CORs requests.

## Getting Started

1. Install all packages via pipenv
2. Create a `.flaskenv` file in the root of the application. Generally, this can be directly copied from `.flaskenv.example`
3. Create a `start.bat` file in the root of the application. This can be copied from the `start.bat.example` file.

## Run the Application

Execute the `start.bat` file. This shold start your Flask application, listening on the port specified in your `.flaskenv` file. It should also spin up a python **SimpleHTTPServer**, listening on the part you've specified in your `start.bat` file.

Navigate to the public app's url and you're all set.

### Note

The public and api logic is hardcoded to use localhost ports 9000 and 8000, respectively. If you need to change these ports, you'll need to alter the port references in the code.