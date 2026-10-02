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

<img width="1377" height="914" alt="1" src="https://github.com/user-attachments/assets/41118b0e-4e64-48d4-ad00-3b92ec49223e" />

<img width="1377" height="914" alt="2" src="https://github.com/user-attachments/assets/bda0d5ad-cf85-4bfa-9465-3a80d016fc08" />

<img width="1377" height="914" alt="3" src="https://github.com/user-attachments/assets/ff1a3390-9cde-4334-9ccd-768aee5eb76e" />

<img width="1377" height="914" alt="4" src="https://github.com/user-attachments/assets/196245ae-798b-4d63-81b8-7c52c1b2e8c2" />

<img width="1377" height="914" alt="5" src="https://github.com/user-attachments/assets/dab2db39-3593-48b1-90b1-0a88f2377abe" />

<img width="1377" height="914" alt="6" src="https://github.com/user-attachments/assets/85c9bfeb-fb03-4e47-9243-2867d468ad00" />


### 2. Clone the Repository
```bash
git clone https://github.com/mina-sawiris/Hospital_OOP_Project_Python.git
