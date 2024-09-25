import sys
import os
import importlib
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QFileDialog,
    QCheckBox, QComboBox, QGroupBox, QFormLayout, QMessageBox, QToolBar, QAction, QMenu,QMainWindow, QDialog, QVBoxLayout
)
from PyQt5.QtGui import (QFont, QIcon)
from PyQt5.QtCore import Qt

class ProcessorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Processor")
        self.setGeometry(100, 100, 700, 475)  # Set the window size to 550 in height
        
        
        # Create UI elements
        self.create_menubar()
        self.create_file_input_section()
        self.create_option_section()
        self.create_assay_section()
        self.create_drug_section()

        # Initially hide Section 3 and Section 4
        self.assay_section.hide()
        self.drug_section.hide()

        # Go Button
        self.create_go_button()


    # Menu bar creation
    def create_menubar(self):
        menubar = self.menuBar()

        # Creating Help Menu
        help_menu = menubar.addMenu('Help')

        readme_action = QAction('README', self)
        example_action = QAction('Example', self)
        git_action = QAction('GitHub', self)

        # Connecting the actions to dummy functions
        readme_action.triggered.connect(self.show_readme)
        example_action.triggered.connect(self.fill_example_data)
        git_action.triggered.connect(self.open_git)

        help_menu.addAction(readme_action)
        help_menu.addAction(example_action)
        help_menu.addAction(git_action)

        # Creating Libraries Menu
        libraries_menu = menubar.addMenu('Libraries')

        libraries = ['PyQt5', 'matplotlib', 'pandas', 'numpy', 'seaborn', 'sys', 'os', 'webbrowser']

        for library in libraries:
            library_action = QAction(library, self)
            library_action.triggered.connect(lambda checked, lib=library: self.check_library(lib))  # Connect each library check
            libraries_menu.addAction(library_action)

        # Creating placeholder actions for Entry1 and Entry2
        entry1_action = QAction('', self)
        entry2_action = QAction('', self)

        # Adding Entry1 and Entry2 to the menubar directly (not as submenus)
        menubar.addAction(entry1_action)
        menubar.addAction(entry2_action)

        entry1_action.triggered.connect(self.entry1_clicked)
        entry2_action.triggered.connect(self.entry2_clicked)

    # Function to show README content (for demo purposes)
    def open_git(self):
        webbrowser.open('https://github.com/Alvarortor')
    def show_readme(self):
        os.startfile("README_Processor.txt")

    # Fill example data into all sections when 'Example' is clicked
    def fill_example_data(self):
        # Section 1: File input with "Example_file.xlsx"
        self.file_path_box.setText("Example_file.xlsx")
        self.file = os.path.join(os.getcwd(), "Example_file.xlsx")  # Simulate full path

        # Section 2: Check all checkboxes
        self.calc_only_checkbox.setChecked(True)
        self.plot_data_checkbox.setChecked(True)
        self.norm_checkbox.setChecked(True)

        # Section 3: Select "CV" in assay type, check drug checkbox
        self.assay_type_combo.setCurrentText("CV")
        self.drug_checkbox.setChecked(True)

        # Section 4: Set compound name, initial concentration, and dilution factor
        self.compound_name_input.setText("Drug")
        self.init_concentration_input.setText("1")
        self.dilution_factor_input.setText("2")

    # Placeholder function for Entry1 clicked
    def entry1_clicked(self):
        print("Entry 1 clicked")

    # Placeholder function for Entry2 clicked
    def entry2_clicked(self):
        print("Entry 2 clicked")

    # Check if the library is installed
    def check_library(self, library_name):
        """Check if the library is installed. If not, prompt to install."""
        try:
            importlib.import_module(library_name)
            self.show_message(f"{library_name} is installed.")
        except ImportError:
            self.show_install_dialog(library_name)

    # Show a message dialog with the library status
    def show_message(self, message):
        QMessageBox.information(self, "Library Check", message)

    # Dialog to install the library if not found
    def show_install_dialog(self, library_name):
        dialog = QDialog(self)
        dialog.setWindowTitle(f"{library_name} not installed")
        

        layout = QVBoxLayout()

        label = QLabel(f"{library_name} is not installed. Would you like to install it now?")
        label.setFont(QFont('Arial', 12))
        layout.addWidget(label)

        install_button = QPushButton(f"Install {library_name} now")
        install_button.clicked.connect(lambda: self.install_library(library_name, dialog))
        install_button.setFont(QFont('Arial', 10))
        
        cancel_button = QPushButton("Cancel")
        cancel_button.setFont(QFont('Arial', 10))
        
        
        layout.addWidget(install_button)
        layout.addWidget(cancel_button)
        
        
        dialog.setLayout(layout)
        dialog.exec_()

    # Run the pip install command
    def install_library(self, library_name, dialog):
        os.system(f"pip install {library_name}")
        dialog.accept()
        QMessageBox.information(self, "Library Install", f"{library_name} installed.")
        QMessageBox.setFont(QFont('Arial', 12))









    # Section 1: File Input
    def create_file_input_section(self):
        self.file_input = QGroupBox("Section 1: File Input", self)
        self.file_input.setFont(QFont("Arial", 12))
        self.file_input.setGeometry(10, 45, 670, 100)

        # Label for prompt
        file_label = QLabel("Select your file:", self.file_input)
        file_label.setFont(QFont("Arial", 10))
        file_label.setGeometry(10, 50, 150, 25)

        # Line edit for file path
        self.file_path_box = QLineEdit(self.file_input)
        self.file_path_box.setPlaceholderText("No file selected")
        self.file_path_box.setReadOnly(True)
        self.file_path_box.setFont(QFont("Arial", 10))
        self.file_path_box.setGeometry(150, 50, 400, 25)

        # Button to search for file
        self.browse_button = QPushButton("Browse", self.file_input)
        self.browse_button.setFont(QFont("Arial", 10))
        self.browse_button.setGeometry(570, 50, 80, 25)
        self.browse_button.clicked.connect(self.browse_files)

    # Browse for file with filter for .xls, .xlsx, or .csv
    def browse_files(self):
        file_filter = "Excel Files (*.xls *.xlsx)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a file", "", file_filter)


        if file_path:
            self.file = file_path  # Store the full file path in the variable
            file_name = os.path.basename(file_path)  # Extract only the file name from the path
            self.file_path_box.setText(file_name)  # Display only the file name in the QLineEdit


    # Section 2: Checkbox for Calculation and Plot Options
    def create_option_section(self):
        self.option_section = QGroupBox("Section 2: Options", self)
        self.option_section.setFont(QFont("Arial", 12))
        self.option_section.setGeometry(10, 150, 330, 120) 

        # Checkbox for calculations
        self.calc_only_checkbox = QCheckBox("Calculations only", self.option_section)
        self.calc_only_checkbox.setFont(QFont("Arial", 10))
        self.calc_only_checkbox.setGeometry(10, 30, 150, 25)
        self.calc_only_checkbox.setChecked(False)
        self.calc_only_checkbox.stateChanged.connect(self.toggle_assay_section)

        # Checkbox for plotting
        self.plot_data_checkbox = QCheckBox("Plot my data", self.option_section)
        self.plot_data_checkbox.setFont(QFont("Arial", 10))
        self.plot_data_checkbox.setGeometry(10, 90, 150, 25)
        self.plot_data_checkbox.stateChanged.connect(self.toggle_assay_section)
        
        #Checkbox for normalizing data
        self.norm_checkbox = QCheckBox("Normalize data", self.option_section)
        self.norm_checkbox.setFont(QFont("Arial", 10))
        self.norm_checkbox.setGeometry(10, 60, 150, 25)


    # Toggle the visibility of the Assay section based on the checkboxes
    def toggle_assay_section(self):
        self.drug_checkbox.setChecked(False)  # Ensure the drug checkbox is always unchecked initially

        if self.plot_data_checkbox.isChecked() or self.calc_only_checkbox.isChecked():
            self.assay_section.show()
        else:
            self.assay_section.hide()
            self.drug_section.hide()  # Hide Section 4 when Assay is hidden

    # Section 3: Assay Type (appears when "Plot my data" is checked)
    def create_assay_section(self):
        self.assay_section = QGroupBox("Section 3: Assay Type", self)
        self.assay_section.setFont(QFont("Arial", 12))
        self.assay_section.setGeometry(350, 150, 330, 120)  # Fixed size, right of Section 2

        assay_type_label = QLabel("Select Assay Type:", self.assay_section)
        assay_type_label.setFont(QFont("Arial", 10))
        assay_type_label.setGeometry(10, 30, 150, 25)

        self.assay_type_combo = QComboBox(self.assay_section)
        self.assay_type_combo.setFont(QFont("Arial", 10))
        self.assay_type_combo.setGeometry(150, 30, 150, 25)
        self.assay_type_combo.addItems(["CV", "XTT", "OD600", "Other"])

        # Checkbox for drug use in analysis
        self.drug_checkbox = QCheckBox("Is this a drug plate?", self.assay_section)
        self.drug_checkbox.setFont(QFont("Arial", 10))
        self.drug_checkbox.setGeometry(10, 70, 300, 40)
        self.drug_checkbox.stateChanged.connect(self.toggle_drug_section)

    # Toggle the visibility of the Drug section based on the checkbox
    def toggle_drug_section(self):
        if self.drug_checkbox.isChecked():
            self.drug_section.show()
        else:
            self.drug_section.hide()

    # Section 4: Drug Info (appears when drug use checkbox is checked)
    def create_drug_section(self):
        txt_box_size = 220
        self.drug_section = QGroupBox("Section 4: Drug Info", self)
        self.drug_section.setFont(QFont("Arial", 12))
        self.drug_section.setGeometry(10, 280, 400, 150)  # Fixed size

        compound_name_label = QLabel("Compound Name:", self.drug_section)
        compound_name_label.setFont(QFont("Arial", 10))
        compound_name_label.setGeometry(10, 30, 150, 25)

        self.compound_name_input = QLineEdit(self.drug_section)
        self.compound_name_input.setFont(QFont("Arial", 10))
        self.compound_name_input.setGeometry(170, 30, txt_box_size, 25)  # Adjusted position

        init_concentration_label = QLabel("Initial Concentration:", self.drug_section)
        init_concentration_label.setFont(QFont("Arial", 10))
        init_concentration_label.setGeometry(10, 70, 150, 25)

        self.init_concentration_input = QLineEdit(self.drug_section)
        self.init_concentration_input.setFont(QFont("Arial", 10))
        self.init_concentration_input.setGeometry(170, 70, 50, 25)  # Adjusted position
        
        self.unit_label = QLabel("\u03bcg/mL",self.drug_section)
        self.unit_label.setFont(QFont("Arial", 10))
        self.unit_label.setGeometry(230, 70, 75, 25)  # Adjusted position
        
        dilution_factor_label = QLabel("Dilution Factor:", self.drug_section)
        dilution_factor_label.setFont(QFont("Arial", 10))
        dilution_factor_label.setGeometry(10, 110, 150, 25)

        self.dilution_factor_input = QLineEdit(self.drug_section)
        self.dilution_factor_input.setFont(QFont("Arial", 10))
        self.dilution_factor_input.setGeometry(170, 110, 50, 25)  # Adjusted position

    # Go Button at the bottom
    def create_go_button(self):
        
        self.go_button = QPushButton("Process\nData!", self)
        self.go_button.setStyleSheet("background-color : red; color: black") 
        self.go_button.setFont(QFont("Arial", 28))
        self.go_button.setGeometry(430, 290, 250, 140)
        self.go_button.clicked.connect(self.on_go_clicked)

    # Handle Go button click
    def on_go_clicked(self):

        script = "PlateReader.py"
        
        # Check if a file is selected
        if not self.file_path_box.text():
            QMessageBox.warning(self, "Error", "Section 1 Error:\nNo file selected.")
            return

        # Check if an option is selected
        if not (self.calc_only_checkbox.isChecked() or self.plot_data_checkbox.isChecked()):
            QMessageBox.warning(self, "Error", "Section 2 Error:\nNo option selected.")
            return

        # Check if the drug section is shown but fields are empty
        if self.drug_checkbox.isChecked() and (
                not self.compound_name_input.text() or
                not self.init_concentration_input.text() or
                not self.dilution_factor_input.text()):
            QMessageBox.warning(self, "Error", "Section 4 Error: Missing drug information.")
            return
        # Check if initial concentration is a valid number
        try:
            float(self.init_concentration_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Section 4:\nInitial concentration must be a number.")
            return
        # Check if dilution factor is a valid number
        try:
            float(self.dilution_factor_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Section 4:\nDilution factor must be a number.")
            return


        # Get file path
        file_path = self.file_path_box.text()

        if self.calc_only_checkbox.isChecked() and self.plot_data_checkbox.isChecked():
            option_selected = "calcandplot"
        elif self.calc_only_checkbox.isChecked():
            option_selected = "calc"
        elif self.plot_data_checkbox.isChecked():
            option_selected = "plot"
        else:
            option_selected = ""  # Default if none (shouldn't happen because of previous check)

        # Get normalize option
        norm_selected = "norm" if self.norm_checkbox.isChecked() else "nonorm"

        # Get assay type if "Plot my data" is selected
        assay_type = self.assay_type_combo.currentText() if self.plot_data_checkbox.isChecked() else ""

        # Get drug info if there
        drug_info = ""
        if self.drug_checkbox.isChecked():
            compound_name = self.compound_name_input.text()
            initial_concentration = self.init_concentration_input.text()
            dilution_factor = self.dilution_factor_input.text()
            drug_info = f"{compound_name} {initial_concentration} {dilution_factor}"

        # Arguments
        arguments = f'{script} {file_path} {option_selected} {norm_selected} {assay_type} {drug_info}'
        os.system(arguments)
        #print(arguments)
        



# Running the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProcessorApp()
    window.show()
    sys.exit(app.exec_())
