# Masker Application

This repository contains the code for the Masker application, which includes a Flask API for image processing and a Tkinter frontend for interacting with the application. Follow the steps below to set up and run both components of the application.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup

### 1. Setting Up the Flask API

1. Open a command prompt or terminal.
2. Navigate to the API directory:

    ```sh
    cd Masker/src/Backend/Processing
    ```

3. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the Flask server:

    ```sh
    python main.py
    ```

    The Flask server will start and run on the default port (usually 5000). Ensure the server is running before proceeding to the next step.

### 2. Setting Up the Tkinter Application

1. Open a new command prompt or terminal.
2. Navigate to the Tkinter application directory:

    ```sh
    cd Masker/src/PyFrontend
    ```

3. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the Tkinter application:

    ```sh
    python main.py
    ```

## Additional Information

- Ensure that the Flask API is running before starting the Tkinter application to allow proper communication between the frontend and backend.

If you encounter any issues, please check the logs for both the Flask API and Tkinter application for debugging information.
