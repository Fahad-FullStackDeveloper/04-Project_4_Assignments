Streamlit link:
https://assignments1to6project-8-createapythonstreamlitbmicalc-kxrwan.streamlit.app/



# BMI Calculator Web App

## Overview
This is a simple **BMI (Body Mass Index) Calculator Web App** built using **Python** and **Streamlit**. It allows users to enter their weight and height to calculate their BMI and provides a classification based on BMI categories.

## Features
- Accepts user input for weight (kg) and height (m)
- Calculates BMI using the standard formula: **BMI = weight / (height * height)**
- Displays BMI result with a category classification:
  - **Underweight:** BMI < 18.5
  - **Normal weight:** 18.5 ≤ BMI < 24.9
  - **Overweight:** 25 ≤ BMI < 29.9
  - **Obese:** BMI ≥ 30
- Provides interactive UI with a **Calculate BMI** button
- Displays warnings and success messages based on BMI classification

## Installation
### Prerequisites
Ensure you have Python installed. If not, download and install it from [Python.org](https://www.python.org/).

### Install Streamlit
Run the following command in your terminal or command prompt to install Streamlit:
```sh
pip install streamlit
```

## Usage
### 1. Clone the Repository
```sh
git clone https://github.com/Fahad-FullStackDeveloper/04-Project_4_Assignments/tree/main/assignments%201%20to%206/Project_8_Create%20a%20Python%20Streamlit%20BMI%20Calculator%20Web%20App%20in%20Just%206%20Minutes
cd bmi-calculator-streamlit
```

### 2. Run the Application
Execute the following command:
```sh
streamlit run bmi_calculator.py
```
This will open the application in your web browser.

## File Structure
```
.
├── bmi_calculator.py  # Main application script
├── README.md          # Documentation
└── requirements.txt   # List of dependencies (optional)
```

## Future Enhancements
- Add unit conversion (height in cm/inches, weight in lbs/kg)
- Improve UI with Streamlit themes and sidebar inputs
- Store and analyze BMI data for multiple users

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by **Fahad Khakwani**

---
### Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request.

