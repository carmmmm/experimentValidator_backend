# Experimental Validation Project

<img width="1366" alt="Screenshot 2024-07-30 at 10 25 58 AM" src="https://github.com/user-attachments/assets/ae3717da-3d2e-468f-be2e-8e55dec6ba8c">
<img width="1388" alt="Screenshot 2024-07-30 at 10 26 18 AM" src="https://github.com/user-attachments/assets/434a0bad-376f-4032-893d-9fccbfc0564b">

## Overview
This project provides a web-based application for validating experimental designs. It includes a frontend developed with React and a backend developed with Flask, which integrates with OpenAI's API to assess experimental parameters. The application helps researchers validate their experimental designs by inputting key parameters and receiving feedback on their setup.

## Key Features
### Frontend Interface

* A user-friendly React application for inputting experimental parameters.
* Provides a clean and intuitive form for hypothesis, sample size, variables, and API key.
* Displays results of the validation process.

### Backend Validation

* A Flask API that communicates with OpenAI's API to validate experimental designs.
* Handles requests to validate parameters and return feedback.

## Technologies Used
* Frontend: React, MUI (Material-UI)
* Backend: Flask, OpenAI API

## Installation and Setup

### Backend
1. Clone the Backend Repository
```
git clone https://github.com/carmmmm/experimentValidation_backend.git

```
2. Navigate to the Backend Directory

```
cd experimental-validation-backend
```

3. Install Dependencies

```
pip install -r requirements.txt
```

4. Run the Backend Application

```
python app.py
```
This will start the Flask server. The API will be accessible at http://127.0.0.1:5000.

### Frontend
1. Clone the Frontend Repository
```
git clone https://github.com/carmmmm/experimentalValidator_frontend.git
```

2. Navigate to the Frontend Directory
```
cd experimentValidator_frontend
```

3. Install Dependencies

```
npm install
```

4. Run the Frontend Application

```
npm start
```

This will start the React development server. The application will be accessible at http://localhost:3000. 


## Accessing the Application
1. Open Your Web Browser
2. Navigate to http://localhost:3000 to access the frontend application.
3. On the home page, click the "Access the Assessment Tool" button to navigate to the experiment form.
   <img width="1366" alt="Screenshot 2024-07-30 at 10 25 58 AM" src="https://github.com/user-attachments/assets/7b838b55-1ae8-479c-b41b-f56aa7862f80">

5. Fill out the form with the following parameters:
* Hypothesis: Describe your hypothesis for the experiment.
* Sample Size: Provide the sample size for the experiment.
* Variables: List the variables involved in the experiment.
* OpenAI API Key: Enter your OpenAI API key to use the backend validation service.
  <img width="1104" alt="Screenshot 2024-07-30 at 10 26 08 AM" src="https://github.com/user-attachments/assets/39c50432-506a-4723-8075-649efbde39ec">

5. Submit the Form
6. Review the feedback displayed on the page to assess the validity of your experimental design.
   <img width="1379" alt="Screenshot 2024-07-30 at 10 26 37 AM" src="https://github.com/user-attachments/assets/8df2c900-f38b-4611-9f8a-303564946767">


### Example
Form Input:

* Hypothesis: "Increasing temperature will increase reaction rate."
* Sample Size: "50"
* Variables: "Temperature, Reaction Rate"
* OpenAI API Key: "YOUR_OPENAI_API_KEY"

## Troubleshooting
* Ensure both the frontend and backend servers are running.
* Check the browser console and terminal for any errors.
* Verify that the OpenAI API key is correct and has sufficient quota.
