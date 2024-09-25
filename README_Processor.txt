# README for the Plate Processor Program

## Overview

Plate Processor is a graphical user interface (GUI) tool designed to assist in performing basic data processing tasks for experimental assayswith 96-well plates. It supports handling both calculation and data plotting tasks, along with optional drug concentration analysis.

The program provides flexibility to handle the assays we do in our lab on 96-well plates, such as Crystal Violet, XTT, and OD600. The UI should make it so the user won't need to write/understand code to process data, but the raw code is included in case issues arise. Remember that while this automates the process, it only understands the inputs. You are ultimately resposible for the data produced from your inputs. 

## Features
- **File Input**: Accepts `.xls`, `.xlsx`, and `.csv` files for data analysis.
- **Options for Processing**:
  - Calculation only
  - Data plotting
  - Normalize data (optional)
- **Assay Type Selection**: Supports standard assays (Crystal Violet , XTT, OD600) and color only.
- **Drug Information Input**: Optionally allows for the entry of drug names, initial concentrations, and dilution factors for drug effect studies.
- **Process Initiation**: A user-friendly "Go" button starts the process.


## System Requirements

- **Operating System**: Compatible with Windows, macOS, and Linux.
- **Python Version**: Python 3.6 or higher is required.
- **Dependencies**: PyQt5, pandas, matplotlib (for data plotting).

## How to Use the Program

1. **File Selection**: 
   - In Section 1, click the "Browse" button to select your data file. Only `.xls`, `.xlsx`, formats are supported.
   
2. **Select Processing Options** (Section 2):
   - Choose between "Calculations only" or "Plot data"
   - The "Normalize" option can be checked to normalize all data against a control in column 11.

3. **Assay Type Selection** (Section 3, appears if "Plot my data" is selected):
   - Choose from predefined assay types (CV, XTT, OD600) or select "Other" for custom assay analysis.
   - If you conducted drug-related experiments, check the box indicating "Did you use drugs?" and fill in the compound name, initial concentration, and dilution factor in Section 4.

4. **Run the Process**:
   - Click the "Go" button to initiate data processing.
   - The program will update the status at the bottom of the window, informing you that it is running and when it is complete.

## Expected Output

- If the "Calculations only" option is selected, the program will process the input data and generate the corresponding numerical results.
- If the "Plot data option is selected, graphical plots based on the selected assay type will be produced.
- If the "Normalize" option is selected, data will be normalized based on the control column in column 11 prior to calculations or plotting.

## Troubleshooting

### Common Issues and Solutions

1. **No file selected**: 
   - **Problem**: The program does not run because no file has been selected.
   - **Solution**: Ensure a valid `.xls`, `.xlsx`, or `.csv` file is selected in Section 1 before clicking the "Go" button.

2. **No processing option selected**:
   - **Problem**: The program requires either "Calculations only" or "Plot my data" to be selected in Section 2.
   - **Solution**: Select at least one of these options before starting the process.

3. **Missing drug information**:
   - **Problem**: The drug checkbox is checked, but no drug data is provided in Section 4.
   - **Solution**: Ensure the compound name, initial concentration, and dilution factor are entered correctly if the drug analysis option is enabled.

4. **Non-numeric input for concentration or dilution factor**:
   - **Problem**: The initial concentration or dilution factor fields in Section 4 contain invalid (non-numeric) data.
   - **Solution**: Ensure that these fields contain valid numbers before clicking "Go."

5. **Program not responding**:
   - **Problem**: The interface appears unresponsive after starting the process.
   - **Solution**: Ensure that the input file is not too large, and that all fields are filled in correctly. If the problem persists, try restarting the program.

## License

This program is distributed under the MIT License.
