# Hospital Management System

## Overview
The Hospital Management System is a Python-based desktop application featuring a Graphical User Interface (GUI). It relies on Object-Oriented Programming (OOP) principles to manage hospital departments, patients, and staff. 

The application follows the **Model-View-Controller (MVC)** architectural pattern. This design physically separates the application's internal data handling from its user interface, allowing multiple developers to work on different parts of the system simultaneously without causing conflicts.

---

## Project Structure (MVC Architecture)

Our repository is organized to maintain a clean separation of concerns. Here is a breakdown of where different components of the application live:

*   **`models/` (The Backend Logic)**
    *   Contains the pure OOP data structures (`Person`, `Patient`, `Staff`, `Department`, `Hospital`).
    *   These files handle data relationships and business logic. There is absolutely no GUI code in this directory.
*   **`views/` (The Frontend GUI)**
    *   Contains all the code responsible for drawing the screen, windows, buttons, and input forms.
    *   Responsible only for displaying data and capturing user input, not processing it.
*   **`controllers/` (The Application Glue)**
    *   Acts as the bridge between the `models` and `views`. 
    *   When a user clicks a button in the view, the controller processes that action, updates the models accordingly, and tells the view to refresh.
*   **`data/` (Data Persistence)**
    *   Stores the JSON or database files used to save the hospital state when the application is closed.
*   **`tests/` (Quality Assurance)**
    *   Contains unit tests to ensure that the core backend models and data storage functions behave as expected.

---

## Installation & Setup

Follow these steps to set up the project on your local machine.

### 1. Prerequisites
*   Ensure you have **Python 3.8+** installed.
*   (Optional but recommended) Install `git` for version control.

## Application Screenshots

Here is a look at the Graphical User Interface in action:

<img width="1377" height="914" alt="1" src="https://github.com/user-attachments/assets/2a980930-37dc-46ff-8361-90ec9b9ca901" />
<br><br><br>
<img width="1377" height="914" alt="2" src="https://github.com/user-attachments/assets/92903fcb-f2af-4f8d-9cd0-1ada92a0dec1" />
<br><br><br>
<img width="1377" height="914" alt="5" src="https://github.com/user-attachments/assets/6c2f24d6-b75d-4f64-805e-a46be8b61ef6" />
<br><br><br>
<img width="1377" height="914" alt="3" src="https://github.com/user-attachments/assets/3a3a01f0-058b-41bb-b07b-85618b6959b3" />
<br><br><br>
<img width="1377" height="914" alt="4" src="https://github.com/user-attachments/assets/324a68ee-7bd7-42f7-b8a8-ed6df4b3f9d2" />
<br><br><br>
<img width="1377" height="914" alt="6" src="https://github.com/user-attachments/assets/4bc31a8f-42f4-4c08-8905-09a186cc6a3e" />


### 2. Clone the Repository
```bash
git clone https://github.com/mina-sawiris/Hospital_OOP_Project_Python.git
