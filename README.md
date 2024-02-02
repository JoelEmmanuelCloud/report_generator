# File Processor App
The `File Processor` App is a simple desktop application built with Python and Tkinter that allows users to process CSV files, generate a PDF report, and view the processing results. The application is designed to provide a user-friendly interface for selecting and processing CSV files, making it useful for tasks such as data analysis and reporting.

## Features

File Selection: Users can easily browse and select one or more CSV files using the "Browse" button.

CSV Processing: The application reads and processes the selected CSV files using the pandas library, summarizing each file's contents.

PDF Report Generation: A PDF report is generated using the ReportLab library, containing a summary of each processed CSV file. The report includes a table of contents with links to each file's section.

Progress Tracking: The application includes a progress bar to track the processing status, providing feedback to the user during file processing.

Getting Started
Clone the Repository:

```bash
https://github.com/JoelEmmanuelCloud/report_generator.git

cd file-processor
````

## Install Dependencies:

```bash
pip install pandas report lab
```

## Run the Application:

```bash
python file_processor_app.py
``````

## Usage:

* Select one or more CSV files by clicking the "Browse" button.
* Click the "Process Files" button to process the selected files.
* The processing results and a link to the generated PDF report will be displayed.

## Dependencies

* Tkinter: Python's standard GUI (Graphical User Interface) package.
* pandas: A data manipulation library for Python used for reading and processing CSV files.
* ReportLab: A PDF generation library for Python used for creating the processing report.

## License
This project is licensed under the MIT License.

## Acknowledgments
* Special thanks to the open-source communities behind Tkinter, pandas, and ReportLab for providing powerful libraries that made this project possible.

Feel free to customize this README file based on your specific project details and requirements.
