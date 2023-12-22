from PyQt6.QtWidgets import (QApplication, QLabel, QWidget,
                             QGridLayout, QLineEdit, QPushButton, QComboBox)
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Efficiency Calculator")
        grid = QGridLayout()

        # Create Widgets
        self.combo = QComboBox()
        self.combo.addItems(['Mana Reservation Efficiency (P0E)', 'DEF (GBF)'])

        self.inputs_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Efficiency")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add Widgets to grid
        grid.addWidget(self.combo, 0, 0)
        grid.addWidget(self.inputs_line_edit, 0, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        measure = ""
        measure_type = ""
        if self.combo.currentText() == 'Mana Reservation Efficiency (P0E)':
            measure = "Реальная резервация"
            measure_type = "от изначальной резервации скилла"
        if self.combo.currentText() == 'DEF (GBF)':
            measure = "Процент входящего урона"
            measure_type = "изначального урона"
        final = 100 / (100 + int(self.inputs_line_edit.text())) * 100
        self.output_label.setText(f"{measure} - {final}% от {measure_type}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
