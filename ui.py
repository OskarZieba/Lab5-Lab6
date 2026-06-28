import sys
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QFileDialog, QMessageBox)
from project import load_data, save_data

class DataConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.input_file = ""
        self.output_file = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Data Converter")
        self.setMinimumSize(400, 200)

        layout = QVBoxLayout()

        # Input selection
        input_layout = QHBoxLayout()
        self.input_label = QLabel("Input file: Not selected")
        self.btn_select_input = QPushButton("Select Input")
        self.btn_select_input.clicked.connect(self.select_input)
        input_layout.addWidget(self.btn_select_input)
        input_layout.addWidget(self.input_label)
        layout.addLayout(input_layout)

        # Output selection
        output_layout = QHBoxLayout()
        self.output_label = QLabel("Output file: Not selected")
        self.btn_select_output = QPushButton("Select Output")
        self.btn_select_output.clicked.connect(self.select_output)
        output_layout.addWidget(self.btn_select_output)
        output_layout.addWidget(self.output_label)
        layout.addLayout(output_layout)

        # Convert button
        self.btn_convert = QPushButton("Convert")
        self.btn_convert.clicked.connect(self.convert_data)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)

    def select_input(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Input File", "", "All Files (*.json *.xml *.yml *.yaml)"
        )
        if file_path:
            self.input_file = file_path
            self.input_label.setText(f"Input: {os.path.basename(file_path)}")

    def select_output(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Select Output File", "", "JSON (*.json);;XML (*.xml);;YAML (*.yml *.yaml)"
        )
        if file_path:
            self.output_file = file_path
            self.output_label.setText(f"Output: {os.path.basename(file_path)}")

    def convert_data(self):
        if not self.input_file or not self.output_file:
            QMessageBox.warning(self, "Error", "Please select both input and output files.")
            return

        try:
            data = load_data(self.input_file)
            save_data(self.output_file, data)
            QMessageBox.information(self, "Success", "Data converted successfully!")
        except SystemExit:
            QMessageBox.critical(self, "Error", "An error occurred during conversion.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred:\n{e}")

def run_ui():
    app = QApplication(sys.argv)
    ex = DataConverterUI()
    ex.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_ui()
