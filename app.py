import os

import openpyxl
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QInputDialog, QMessageBox
from MessagePack import print_info_msg

import design


class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self, marker: str = ''):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setupUi(self)

        # ToolTips stylesheet
        self.setStyleSheet("""QToolTip {
                            border: 1px solid black;
                            padding: 3px;
                            border-radius: 3px;
                            opacity: 200;
                        }""")

        self.lineEditFile.setText('не выбран')
        self.lineEditDir.setText(os.getcwd())

        self.startButton.clicked.connect(self._start_click)
        self.selectDirButton.clicked.connect(self._select_dir_path)
        self.selectFileButton.clicked.connect(self._select_file_path)

    def _select_dir_path(self):
        path = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        if path != '':
            self.lineEditDir.setText(path)
        print_info_msg(f'path: {path}')

    def _select_file_path(self):
        filter_ = "Excel(*.csv *.xlsx)"
        path = QFileDialog.getOpenFileName(self, 'Выберите файл', os.getcwd(), filter=filter_)[0]
        if path != '':
            self.lineEditFile.setText(path)
            self.wb = openpyxl.load_workbook(path)
            self.comboBox.addItems(self.wb.sheetnames)
        print_info_msg(f'path: {path}')

    def _start_click(self):
        reply = QMessageBox.question(self, 'Старт', f'Файл: {self.lineEditFile.text()}\n'
                                                    f'Лист: {self.comboBox.currentText()}\n'
                                                    f'Папка выгрузки: {self.lineEditDir.text()}\n'
                                                    f'Продолжить?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes and os.path.exists(self.lineEditFile.text()):
            ws = self.wb[self.comboBox.currentText()]
            self.data = []
            for row in ws.rows:
                row_ = []
                for cell in row:
                    row_.append(cell.value)
                self.data.append(row_)
            print('rows count:', len(self.data))
