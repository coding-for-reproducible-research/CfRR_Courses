# Data Analysis Introduction

## Learning Objectives

In this lesson, we will:

- Introduce the data analysis task
- Create a project folder for the task, download some data, and place this into it.

## Scenario: A miracle arthritis inflammation cure

Our imaginary colleague “Dr. Maverick” has invented a new miracle drug that promises to cure arthritis inflammation flare-ups after only 3 weeks since initially taking the medication! Naturally, we wish to see the clinical trial data, and after months of asking for the data they have finally provided us with a CSV spreadsheet containing the clinical trial data.

The CSV file contains the number of inflammation flare-ups per day for the 60 patients in the initial clinical trial, with the trial lasting 40 days. Each row corresponds to a patient, and each column corresponds to a day in the trial. Once a patient has their first inflammation flare-up they take the medication and wait a few weeks for it to take effect and reduce flare-ups.

To see how effective the treatment is we would like to:

- Calculate the average inflammation per day across all patients.
- Plot the result to discuss and share with colleagues.

![3-step flowchart shows inflammation data records for patients moving to the Analysis step
where a heat map of provided data is generated moving to the Conclusion step that asks the
question, How does the medication affect patients?](
../fig/lesson-overview.svg "Lesson Overview")

## Download the data

First, we need to open JupyterLab, and create a new folder for our project. In this folder, lets create a new folder called data. We can then download some data from [here](https://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-data.zip).

Unzip this folder, and move the `.csv` files into the same folder as your Jupyter notebook, or JupyterLab instance. This can be done by dragging them across onto the sidebar.
