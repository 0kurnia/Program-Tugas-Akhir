from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
import os
from Load_data import Load_data
from BPGA import BPGA

class Main(object):
    filename_latih = ''
    filename_uji = ''
    bobot_Vji_bp = []
    bobot_Vj0_bp = []
    bobot_Wkj_bp = []
    bobot_Wk0_bp = []
    bobot_Vji_bpga = []
    bobot_Vj0_bpga = []
    bobot_Wkj_bpga = []
    bobot_Wk0_bpga = []
    kromosom_terbaik = []
    hasil_prediksi = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 659)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                 "background-color: rgb(40, 40, 40);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(200, 600))
        self.frame.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.parameter = QtWidgets.QFrame(self.frame)
        self.parameter.setMinimumSize(QtCore.QSize(300, 650))
        self.parameter.setMaximumSize(QtCore.QSize(1000, 1000))
        self.parameter.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                                     "background-color: rgb(113, 113, 113);")
        self.parameter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.parameter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.parameter.setObjectName("parameter")
        self.frame_6 = QtWidgets.QFrame(self.parameter)
        self.frame_6.setGeometry(QtCore.QRect(10, 8, 170, 82))
        self.frame_6.setMinimumSize(QtCore.QSize(170, 82))
        self.frame_6.setMaximumSize(QtCore.QSize(170, 1000))
        self.frame_6.setStyleSheet("background-color: rgb(213, 213, 105);\n"
                                   "background-color: rgb(200, 200, 200);\n"
                                   "")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.BP = QtWidgets.QRadioButton(self.frame_6)
        self.BP.setGeometry(QtCore.QRect(10, 30, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BP.setFont(font)
        self.BP.setObjectName("BP")
        self.BPGA = QtWidgets.QRadioButton(self.frame_6)
        self.BPGA.setGeometry(QtCore.QRect(10, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BPGA.setFont(font)
        self.BPGA.setObjectName("BPGA")
        self.frame_7 = QtWidgets.QFrame(self.parameter)
        self.frame_7.setGeometry(QtCore.QRect(10, 110, 170, 360))
        self.frame_7.setMaximumSize(QtCore.QSize(1000, 1000))
        self.frame_7.setStyleSheet("background-color: rgb(213, 213, 105);\n"
                                   "background-color: rgb(200, 200, 200);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.crossover_rate = QtWidgets.QLabel(self.frame_7)
        self.crossover_rate.setGeometry(QtCore.QRect(10, 190, 81, 16))
        self.crossover_rate.setObjectName("crossover_rate")
        self.mutasi_rate = QtWidgets.QLabel(self.frame_7)
        self.mutasi_rate.setGeometry(QtCore.QRect(10, 230, 71, 16))
        self.mutasi_rate.setObjectName("mutasi_rate")
        self.training = QtWidgets.QPushButton(self.frame_7)
        self.training.setGeometry(QtCore.QRect(50, 280, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.training.setFont(font)
        self.training.setStyleSheet("background-color: rgb(113, 113, 113);")
        self.training.setObjectName("training")
        self.testing = QtWidgets.QPushButton(self.frame_7)
        self.testing.setGeometry(QtCore.QRect(50, 320, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.testing.setFont(font)
        self.testing.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                   "background-color: rgb(113, 113, 113);")
        self.testing.setObjectName("testing")
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.learning_rate = QtWidgets.QLabel(self.frame_7)
        self.learning_rate.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.learning_rate.setStyleSheet("border-color: rgb(11, 11, 11);")
        self.learning_rate.setObjectName("learning_rate")
        self.Epoch = QtWidgets.QLabel(self.frame_7)
        self.Epoch.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.Epoch.setObjectName("Epoch")
        self.generasi = QtWidgets.QLabel(self.frame_7)
        self.generasi.setGeometry(QtCore.QRect(10, 150, 61, 20))
        self.generasi.setObjectName("generasi")
        self.isi_learningrate = QtWidgets.QLineEdit(self.frame_7)
        self.isi_learningrate.setGeometry(QtCore.QRect(90, 30, 71, 20))
        self.isi_learningrate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.isi_learningrate.setObjectName("isi_learningrate")
        self.isi_generasi = QtWidgets.QLineEdit(self.frame_7)
        self.isi_generasi.setGeometry(QtCore.QRect(90, 150, 71, 20))
        self.isi_generasi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.isi_generasi.setObjectName("isi_generasi")
        self.isi_epoch = QtWidgets.QLineEdit(self.frame_7)
        self.isi_epoch.setGeometry(QtCore.QRect(90, 70, 71, 20))
        self.isi_epoch.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.isi_epoch.setObjectName("isi_epoch")
        self.isi_mutasirate = QtWidgets.QLineEdit(self.frame_7)
        self.isi_mutasirate.setGeometry(QtCore.QRect(90, 230, 71, 20))
        self.isi_mutasirate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.isi_mutasirate.setObjectName("isi_mutasirate")
        self.isi_crossoverrate = QtWidgets.QLineEdit(self.frame_7)
        self.isi_crossoverrate.setGeometry(QtCore.QRect(90, 190, 71, 20))
        self.isi_crossoverrate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.isi_crossoverrate.setObjectName("isi_crossoverrate")
        self.Populasi = QtWidgets.QLabel(self.frame_7)
        self.Populasi.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.Populasi.setObjectName("Populasi")
        self.isi_populasi = QtWidgets.QLineEdit(self.frame_7)
        self.isi_populasi.setGeometry(QtCore.QRect(90, 110, 71, 20))
        self.isi_populasi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.isi_populasi.setObjectName("isi_populasi")
        self.performa_model = QtWidgets.QFrame(self.parameter)
        self.performa_model.setGeometry(QtCore.QRect(10, 490, 170, 90))
        self.performa_model.setMinimumSize(QtCore.QSize(0, 80))
        self.performa_model.setMaximumSize(QtCore.QSize(1000, 1000))
        self.performa_model.setStyleSheet("background-color: rgb(213, 213, 105);\n"
                                          "background-color: rgb(200, 200, 200);")
        self.performa_model.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.performa_model.setFrameShadow(QtWidgets.QFrame.Raised)
        self.performa_model.setObjectName("performa_model")
        self.label_10 = QtWidgets.QLabel(self.performa_model)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.performa_model)
        self.label_11.setGeometry(QtCore.QRect(20, 49, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.hasil_akurasi = QtWidgets.QTextEdit(self.performa_model)
        self.hasil_akurasi.setGeometry(QtCore.QRect(90, 10, 71, 31))
        self.hasil_akurasi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hasil_akurasi.setObjectName("hasil_akurasi")
        self.isi_mse = QtWidgets.QTextEdit(self.performa_model)
        self.isi_mse.setGeometry(QtCore.QRect(90, 50, 71, 31))
        self.isi_mse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.isi_mse.setObjectName("isi_mse")
        self.verticalLayout.addWidget(self.parameter)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 600))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(770, 600))
        self.frame_4.setMaximumSize(QtCore.QSize(770, 600))
        self.frame_4.setStyleSheet("background-color: rgb(113, 113, 113);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setGeometry(QtCore.QRect(8, 8, 750, 100))
        self.frame_3.setMinimumSize(QtCore.QSize(750, 100))
        self.frame_3.setMaximumSize(QtCore.QSize(700, 100))
        self.frame_3.setStyleSheet("background-color: rgb(113, 113, 113);\n"
                                   "background-color: rgb(200, 200, 200);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(10, 60, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.browse_latih = QtWidgets.QPushButton(self.frame_3)
        self.browse_latih.setGeometry(QtCore.QRect(660, 30, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.browse_latih.setFont(font)
        self.browse_latih.setStyleSheet("background-color: rgb(113, 113, 113);")
        self.browse_latih.setObjectName("browse_latih")
        self.browse_uji = QtWidgets.QPushButton(self.frame_3)
        self.browse_uji.setGeometry(QtCore.QRect(660, 60, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.browse_uji.setFont(font)
        self.browse_uji.setStyleSheet("background-color: rgb(113, 113, 113);\n"
                                      "")
        self.browse_uji.setObjectName("browse_uji")
        self.isi_datalatih = QtWidgets.QLineEdit(self.frame_3)
        self.isi_datalatih.setGeometry(QtCore.QRect(80, 30, 561, 21))
        self.isi_datalatih.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.isi_datalatih.setObjectName("isi_datalatih")
        self.isi_datauji = QtWidgets.QLineEdit(self.frame_3)
        self.isi_datauji.setGeometry(QtCore.QRect(80, 60, 561, 21))
        self.isi_datauji.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.isi_datauji.setObjectName("isi_datauji")
        self.hasil_pengujian = QtWidgets.QPushButton(self.frame_4)
        self.hasil_pengujian.setGeometry(QtCore.QRect(270, 120, 201, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hasil_pengujian.setFont(font)
        self.hasil_pengujian.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.hasil_pengujian.setObjectName("hasil_pengujian")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setGeometry(QtCore.QRect(8, 150, 751, 461))
        self.tableWidget.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(26)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(25, item)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browse_latih.clicked.connect(self.open_file_latih)
        self.browse_uji.clicked.connect(self.open_file_uji)
        self.training.clicked.connect(self.start_klasifikasi)
        self.testing.clicked.connect(self.start_pengujian)
        self.hasil_pengujian.clicked.connect(self.tampil_table)

    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Ups Ada yang Salah!")
        msg.setIcon(QMessageBox.Warning)
        msg.show()
        msg.exec_()

    def reset(self):
        self.bobot_Vji_bp = []
        self.bobot_Vj0_bp = []
        self.bobot_Wkj_bp = []
        self.bobot_Wk0_bp = []
        self.bobot_Vji_bpga = []
        self.bobot_Vj0_bpga = []
        self.bobot_Wkj_bpga = []
        self.bobot_Wk0_bpga = []
        self.kromosom_terbaik = []
        self.hasil_prediksi = []

    def open_file_latih(self):
        file_filter = 'Data File(*.csv);'
        self.filename_latih = QFileDialog.getOpenFileName(
            # parent=self,
            caption='select a data file',
            directory=os.getcwd(),
            filter=file_filter
        )
        self.isi_datalatih.setText(self.filename_latih[0])

    def open_file_uji(self):
        file_filter = 'Data File(*.csv *.xlsx);; CSV File(*.csv)'
        self.filename_uji = QFileDialog.getOpenFileName(
            # parent=self,
            caption='select a data file',
            directory=os.getcwd(),
            filter=file_filter
        )
        self.isi_datauji.setText(self.filename_uji[0])

    def tampil_table(self):
        try:
            data_klasifikasi = Load_data.get_data(Load_data, self.filename_uji[0])
            for x in range(len(data_klasifikasi)):
                data_klasifikasi[x].append(self.hasil_prediksi[x])

            self.tableWidget.setColumnWidth(0, 50)
            self.tableWidget.setColumnWidth(1, 50)
            self.tableWidget.setColumnWidth(2, 50)
            self.tableWidget.setColumnWidth(3, 50)
            self.tableWidget.setColumnWidth(4, 50)
            self.tableWidget.setColumnWidth(5, 50)
            self.tableWidget.setColumnWidth(6, 50)
            self.tableWidget.setColumnWidth(7, 50)
            self.tableWidget.setColumnWidth(8, 50)
            self.tableWidget.setColumnWidth(9, 50)
            self.tableWidget.setColumnWidth(10, 50)
            self.tableWidget.setColumnWidth(11, 50)
            self.tableWidget.setColumnWidth(12, 50)
            self.tableWidget.setColumnWidth(13, 50)
            self.tableWidget.setColumnWidth(14, 50)
            self.tableWidget.setColumnWidth(15, 50)
            self.tableWidget.setColumnWidth(16, 50)
            self.tableWidget.setColumnWidth(17, 50)
            self.tableWidget.setColumnWidth(18, 50)
            self.tableWidget.setColumnWidth(19, 50)
            self.tableWidget.setColumnWidth(20, 50)
            self.tableWidget.setColumnWidth(21, 50)
            self.tableWidget.setColumnWidth(22, 50)
            self.tableWidget.setColumnWidth(23, 50)
            self.tableWidget.setColumnWidth(24, 50)
            self.tableWidget.setColumnWidth(25, 50)


            self.tableWidget.setRowCount(len(data_klasifikasi))
            row = 0
            for data in data_klasifikasi:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(data[6])))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data[7])))
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(data[8])))
                self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(data[9])))
                self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(str(data[10])))
                self.tableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem(str(data[11])))
                self.tableWidget.setItem(row, 12, QtWidgets.QTableWidgetItem(str(data[12])))
                self.tableWidget.setItem(row, 13, QtWidgets.QTableWidgetItem(str(data[13])))
                self.tableWidget.setItem(row, 14, QtWidgets.QTableWidgetItem(str(data[14])))
                self.tableWidget.setItem(row, 15, QtWidgets.QTableWidgetItem(str(data[15])))
                self.tableWidget.setItem(row, 16, QtWidgets.QTableWidgetItem(str(data[16])))
                self.tableWidget.setItem(row, 17, QtWidgets.QTableWidgetItem(str(data[17])))
                self.tableWidget.setItem(row, 18, QtWidgets.QTableWidgetItem(str(data[18])))
                self.tableWidget.setItem(row, 19, QtWidgets.QTableWidgetItem(str(data[19])))
                self.tableWidget.setItem(row, 20, QtWidgets.QTableWidgetItem(str(data[20])))
                self.tableWidget.setItem(row, 21, QtWidgets.QTableWidgetItem(str(data[21])))
                self.tableWidget.setItem(row, 22, QtWidgets.QTableWidgetItem(str(data[22])))
                self.tableWidget.setItem(row, 23, QtWidgets.QTableWidgetItem(str(data[23])))
                self.tableWidget.setItem(row, 24, QtWidgets.QTableWidgetItem(str(data[24])))
                self.tableWidget.setItem(row, 25, QtWidgets.QTableWidgetItem(str(data[25])))
                row += 1
            self.reset()
        except:
            self.error()

    def finish_training(self):
        msg = QMessageBox()
        msg.setWindowTitle("Training")
        msg.setText("Training Sudah Selesai")
        msg.setIcon(QMessageBox.Warning)
        msg.show()
        msg.exec_()

    def start_klasifikasi(self):
        try:
            if self.filename_latih[0] == 'C:/Users/Acer/python/Program_TA_Kurnia_Check/dataset/data_tes_latih.csv':
                data_latih = Load_data.get_data(Load_data, self.filename_latih[0])
                data_latih_normalisasi = data_latih
            else:
                data_latih = Load_data.get_data(Load_data, self.filename_latih[0])
                data_latih_normalisasi = Load_data.preprocess_data(Load_data, data_latih)
            populasi = int(self.isi_populasi.text())

            if (self.BP.isChecked()):
                print("BP")
                data_kromosom = BPGA.data_random(BPGA)
                # Melakukan Pembagian bobot berdasarkan kromosom
                for i in range(0, 1): 
                    # Pembagian bobot Vji(input ke hidden) berdasarkan kromosom
                    self.bobot_Vji_bp = BPGA.bobot_input_hidden(BPGA, data_kromosom, i)
                    # Pembagian bobot Vj0(bias hidden) berdasarkan kromosom
                    self.bobot_Vj0_bp = BPGA.bobot_bias_hidden(BPGA, data_kromosom, i)
                    # Pembagian bobot Wkj(hidden ke output) berdasarkan kromosom
                    self.bobot_Wkj_bp = BPGA.bobot_hidden_output(BPGA, data_kromosom, i)
                    # Pembagian bobot Wk0 (bias output) berdasarkan kromosom
                    self.bobot_Wk0_bp = BPGA.bobot_bias_output(BPGA, data_kromosom, i)

                    iterasi = int(self.isi_epoch.text())
                    for r in range(iterasi):

                        y_output_all = []
                        # Setelah mendapat inisialisasi bobot dari kromosom, maka dilanjutkan dengan perhitungan algoritma backpropagation
                        for b in range(len(data_latih_normalisasi)):
                            #   1)Perhitungan FeedForward
                            # Menghitung nilai keluaran pada hidden layer
                            z_net,z_hidden, y_net, y_output, eror_prediksi = BPGA.feed_forward(BPGA, data_latih_normalisasi, self.bobot_Vji_bp,
                                                                                  self.bobot_Vj0_bp, self.bobot_Wkj_bp, self.bobot_Wk0_bp, b)
                            y_output_all.append(y_output)

                            banyak_data = len(data_latih[b])
                            learning_rate = float(self.isi_learningrate.text())

                            delta_Vji, delta_Vj0, delta_Wkj, delta_Wk0 = BPGA.backward(BPGA, data_latih_normalisasi,
                                                                                       self.bobot_Wkj_bp, eror_prediksi,
                                                                                       z_hidden, learning_rate, b)
                            # Melakukan perubahan bobot hidden ke output
                            for x in range(len(self.bobot_Wkj_bp)):
                                self.bobot_Wkj_bp[x] = self.bobot_Wkj_bp[x] + delta_Wkj[x]
                            # Melakukan perubahan bobot bias output
                            self.bobot_Wk0_bp = self.bobot_Wk0_bp + delta_Wk0

                            # Melakukan perubahan bobot input ke hidden
                            for x in range(len(self.bobot_Vji_bp)):
                                for y in range(len(self.bobot_Vji_bp[0])):
                                    self.bobot_Vji_bp[x][y] = self.bobot_Vji_bp[x][y] + delta_Vji[x][y]

                            # Melakukan perubahan bobot bias output
                            for x in range(len(self.bobot_Vj0_bp)):
                                self.bobot_Vj0_bp[x] = self.bobot_Vj0_bp[x] + delta_Vj0[x]

                            mse = BPGA.mse(BPGA, data_latih, y_output_all, banyak_data)

                        print("Nilai mse pada iterasi ke {} {}".format(r, mse))

                    result = []
                    for i in y_output_all:
                        if i > 0.5:
                            result.append(1)
                        else:
                            result.append(0)

                    nilai_benar = 0
                    for x in range(len(data_latih)):
                        if data_latih[x][-1] == result[x]:
                            nilai_benar += 1
                    print("nilai benar pada data latih", nilai_benar)
                    nilai_akurasi = nilai_benar / len(data_latih)
                    print("nilai akurasi pada training", nilai_akurasi)
                    Main.finish_training(self)

            else:

                print("BPGA")

                data_kromosom = BPGA.data_kromosom(BPGA, populasi)

                # Melakukan Pembagian bobot berdasarkan kromosom

                fitness_all = []

                kromosom_elitism = []

                mse_elitism = []

                iterasi = int(self.isi_epoch.text())

                generasi = int(self.isi_generasi.text())

                for r in range(generasi):
                    mse_all = []
                    for i in range(len(data_kromosom)):
                        # Pembagian bobot Vji(input ke hidden) berdasarkan kromosom
                        self.bobot_Vji_bpga = BPGA.bobot_input_hidden(BPGA, data_kromosom, i)
                        # Pembagian bobot Vj0(bias hidden) berdasarkan kromosom
                        self.bobot_Vj0_bpga = BPGA.bobot_bias_hidden(BPGA, data_kromosom, i)
                        # Pembagian bobot Wkj(hidden ke output) berdasarkan kromosom
                        self.bobot_Wkj_bpga = BPGA.bobot_hidden_output(BPGA, data_kromosom, i)
                        # Pembagian bobot Wk0 (bias output) berdasarkan kromosom
                        self.bobot_Wk0_bpga = BPGA.bobot_bias_output(BPGA, data_kromosom, i)

                        y_output_all = []

                        # Setelah mendapat inisialisasi bobot dari kromosom, maka dilanjutkan dengan perhitungan algoritma backpropagation
                        for b in range(len(data_latih_normalisasi)):
                            #   1)Perhitungan FeedForward
                            # Menghitung nilai keluaran pada hidden layer
                            z_net, z_hidden, y_net, y_output, eror_prediksi = BPGA.feed_forward(BPGA,
                                                                                                data_latih_normalisasi,
                                                                                                self.bobot_Vji_bpga,

                                                                                                self.bobot_Vj0_bpga,
                                                                                                self.bobot_Wkj_bpga,
                                                                                                self.bobot_Wk0_bpga, b)

                            y_output_all.append(y_output)
                            banyak_data = len(data_latih[b])
                            learning_rate = float(self.isi_learningrate.text())
                            delta_Vji, delta_Vj0, delta_Wkj, delta_Wk0 = BPGA.backward(BPGA, data_latih_normalisasi,

                                                                                       self.bobot_Wkj_bpga,
                                                                                       eror_prediksi,

                                                                                       z_hidden, learning_rate, b)

                            # Melakukan perubahan bobot hidden ke output
                            for x in range(len(self.bobot_Wkj_bpga)):
                                self.bobot_Wkj_bpga[x] = self.bobot_Wkj_bpga[x] + delta_Wkj[x]
                            # Melakukan perubahan bobot bias output
                            self.bobot_Wk0_bpga = self.bobot_Wk0_bpga + delta_Wk0
                            # Melakukan perubahan bobot input ke hidden
                            for x in range(len(self.bobot_Vji_bpga)):
                                for y in range(len(self.bobot_Vji_bpga[0])):
                                    self.bobot_Vji_bpga[x][y] = self.bobot_Vji_bpga[x][y] + delta_Vji[x][y]
                            # Melakukan perubahan bobot bias output

                            for x in range(len(self.bobot_Vj0_bpga)):
                                self.bobot_Vj0_bpga[x] = self.bobot_Vj0_bpga[x] + delta_Vj0[x]

                        # menghitung nilai MSE untuk mengetahui performa metode

                        mse = BPGA.mse(BPGA, data_latih, y_output_all, banyak_data)
                        mse_all.append(round(mse, 4))

                    print("mse_all di iterasi ke{}{}".format(r, mse_all))
                    mse_elitism.append(mse_all)

                    # ====================================Tahapan Algoritma Genetika=======================================

                    fitness = BPGA.fitness(BPGA, mse_all)
                    fitness_all.append(fitness)

                    kromosom_parent = BPGA.parent_selection(BPGA, fitness, populasi, data_kromosom)

                    # parent selection
                    data_kromosom = kromosom_parent

                    # Tahap crossover
                    crosover_rate = float(self.isi_crossoverrate.text())
                    cross_over = BPGA.cross_over(BPGA, crosover_rate, data_kromosom, populasi)

                    # Tahap Mutation
                    mutasi_rate = float(self.isi_mutasirate.text())
                    mutasi = BPGA.mutasi(BPGA, mutasi_rate, populasi, data_kromosom)

                    kromosom_elitism.append(data_kromosom)

                #Pengambilan kromosom terbaik dengan fitness tertinggi(mse terendah)
                a = 0
                b = 0
                gbest = fitness_all[0][0]

                for x in range(len(fitness_all)):
                    for y in range(len(fitness_all[0])):
                        if gbest <= fitness_all[x][y]:
                            gbest = fitness_all[x][y]
                            a = x
                            b = y

                kromosom_elitsm_terbaik = kromosom_elitism[a][b]
                print("index kromsom terbaik")
                print("a:{},b:{}".format(a, b))
                print("fitness kromosom terbaik", gbest)
                print("kromosom terbaik", kromosom_elitsm_terbaik)
                #print("mse", mse_elitism[a][b])

                self.kromosom_terbaik = kromosom_elitsm_terbaik

                # pelatihan dengan bobot dari kromosom terbaik
                data_elitism = []
                for i in range(0, 1):
                    data_elitism.append(self.kromosom_terbaik)
                    self.bobot_Vji_bpga = BPGA.bobot_input_hidden(BPGA, data_elitism, i)
                    self.bobot_Vj0_bpga = BPGA.bobot_bias_hidden(BPGA, data_elitism, i)
                    self.bobot_Wkj_bp = BPGA.bobot_hidden_output(BPGA, data_elitism, i)
                    self.bobot_Wk0_bpga = BPGA.bobot_bias_output(BPGA, data_elitism, i)

                    for itr in range(iterasi):
                        y_output_all = []
                        for b in range(len(data_latih_normalisasi)):
                            # feedforward
                            z_net, z_hidden, y_net, y_output, eror_prediksi = BPGA.feed_forward(BPGA,
                                                                                                data_latih_normalisasi,

                                                                                                self.bobot_Vji_bpga,

                                                                                                self.bobot_Vj0_bpga,
                                                                                                self.bobot_Wkj_bpga,

                                                                                                self.bobot_Wk0_bpga, b)

                            y_output_all.append(y_output)

                            # backward
                            banyak_data = len(data_latih[b])
                            delta_Vji, delta_Vj0, delta_Wkj, delta_Wk0 = BPGA.backward(BPGA, data_latih_normalisasi,

                                                                                       self.bobot_Wkj_bpga,
                                                                                       eror_prediksi,

                                                                                       z_hidden, learning_rate, b)

                            # Update Bobot
                            for x in range(len(self.bobot_Wkj_bpga)):
                                self.bobot_Wkj_bpga[x] = self.bobot_Wkj_bpga[x] + delta_Wkj[x]

                            self.bobot_Wk0_bpga = self.bobot_Wk0_bpga + delta_Wk0

                            for x in range(len(self.bobot_Wkj_bpga)):

                                for y in range(len(self.bobot_Vji_bpga[0])):
                                    self.bobot_Vji_bpga[x][y] = self.bobot_Vji_bpga[x][y] + delta_Vji[x][y]

                            for x in range(len(self.bobot_Vj0_bpga)):
                                self.bobot_Vj0_bpga[x] = self.bobot_Vj0_bpga[x] + delta_Vj0[x]

                        mse = BPGA.mse(BPGA, data_latih, y_output_all, banyak_data)
                        print("Nilai mse pada iterasi ke {} {}".format(itr, mse))

                result = []
                for i in y_output_all:
                    if i > 0.5:
                        result.append(1)
                    else:
                        result.append(0)

                print("hasilprediksi", y_output_all)

                print(result)
                nilai_benar = 0
                for x in range(len(data_latih)):

                    if data_latih[x][-1] == result[x]:
                        nilai_benar += 1
                print("nilai benar", nilai_benar)
                nilai_akurasi = nilai_benar / len(data_latih)
                print("nilai akurasi", nilai_akurasi)
                Main.finish_training(self)
        except:
            self.error()

    def start_pengujian(self):
        try:
            if self.filename_uji[0] == 'C:/Users/Acer/python/Program_TA_Kurnia_Check/dataset/data_tes_uji.csv':
                data_uji = Load_data.get_data(Load_data, self.filename_uji[0])
                data_uji_normalisasi = data_uji
            else:
                data_uji = Load_data.get_data(Load_data, self.filename_uji[0])
                data_uji_normalisasi = Load_data.preprocess_data(Load_data, data_uji)
            if (self.BP.isChecked()):
                print("uji bp")
                y_output_all_final = []
                for b in range(len(data_uji_normalisasi)):
                    z_net_final,z_hidden_final, y_net_final, y_output_final, eror_prediksi_final = BPGA.feed_forward(BPGA, data_uji_normalisasi, self.bobot_Vji_bp,
                                                                                  self.bobot_Vj0_bp, self.bobot_Wkj_bp, self.bobot_Wk0_bp, b)
                    y_output_all_final.append(y_output_final)
                    banyak_data_testing = len(data_uji[0])
                mse_testing = round(BPGA.mse(BPGA, data_uji, y_output_all_final, banyak_data_testing), 4)
                self.isi_mse.setText(str(mse_testing))
                print("mse data uji", mse_testing)
                print(y_output_all_final)
                #print("youtput",len(y_output_all_final))

                for i in y_output_all_final:
                    #print(i)
                    if i > 0.5:
                        self.hasil_prediksi.append(1)
                    else:
                        self.hasil_prediksi.append(0)
                print(self.hasil_prediksi)
                #print(len(self.hasil_prediksi))
                nilai_benar = 0
                for x in range(len(data_uji)):
                    if data_uji[x][-1] == self.hasil_prediksi[x]:
                        nilai_benar += 1
                print("nilai benar", nilai_benar)
                nilai_akurasi = (nilai_benar / len(data_uji))*100
                print("nilai akurasi", nilai_akurasi)
                self.hasil_akurasi.setText(str(nilai_akurasi))


            else:
                y_output_all_final = []
                for b in range(len(data_uji_normalisasi)):
                    z_net,z_hidden, y_net, y_output, eror_prediksi = BPGA.feed_forward(BPGA, data_uji_normalisasi, self.bobot_Vji_bpga,
                                                                          self.bobot_Vj0_bpga, self.bobot_Wkj_bpga, self.bobot_Wk0_bpga, b)
                    y_output_all_final.append(y_output)
                    banyak_data_testing = len(data_uji[b])

                mse_testing = round(BPGA.mse(BPGA, data_uji, y_output_all_final, banyak_data_testing), 4)
                self.isi_mse.setText(str(mse_testing))
                print("mse data uji", round((mse_testing), 4))

                print("hasil prediksi", y_output_all_final)
                for i in y_output_all_final:
                    if i > 0.5:
                        self.hasil_prediksi.append(1)
                    else:
                        self.hasil_prediksi.append(0)
                print(self.hasil_prediksi)
                #print(len(self.hasil_prediksi))
                nilai_benar = 0

                for x in range(len(data_uji)):
                    if data_uji[x][-1] == self.hasil_prediksi[x]:
                        nilai_benar += 1
                print("nilai benar", nilai_benar)
                nilai_akurasi = (nilai_benar / len(data_uji))*100
                print("nilai akurasi", nilai_akurasi)
                self.hasil_akurasi.setText(str(nilai_akurasi))
        except:
            self.error()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Metode"))
        self.BP.setText(_translate("MainWindow", "BP"))
        self.BPGA.setText(_translate("MainWindow", "BPGA"))
        self.crossover_rate.setText(_translate("MainWindow", "Crossover Rate"))
        self.mutasi_rate.setText(_translate("MainWindow", "Mutation Rate"))
        self.training.setText(_translate("MainWindow", "Training"))
        self.testing.setText(_translate("MainWindow", "Testing"))
        self.label_8.setText(_translate("MainWindow", "Parameter"))
        self.learning_rate.setText(_translate("MainWindow", "Learning rate"))
        self.Epoch.setText(_translate("MainWindow", "Epoch"))
        self.generasi.setText(_translate("MainWindow", "Generasi"))
        self.Populasi.setText(_translate("MainWindow", "Populasi"))
        self.label_10.setText(_translate("MainWindow", "Akurasi"))
        self.label_11.setText(_translate("MainWindow", "MSE"))
        self.label_2.setText(_translate("MainWindow", "Aplikasi Penilaian Pengajuan Kredit"))
        self.label_12.setText(_translate("MainWindow", "Data Latih"))
        self.label_13.setText(_translate("MainWindow", "Data Uji"))
        self.browse_latih.setText(_translate("MainWindow", "Browse"))
        self.browse_uji.setText(_translate("MainWindow", "Browse"))
        self.hasil_pengujian.setText(_translate("MainWindow", "Hasil Klasifikasi Data Uji"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "X2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "X3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "X4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "X5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "X6"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "X7"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "X8"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "X9"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "X10"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "X11"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "X12"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "X13"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "X14"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "X15"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "X16"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "X17"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "X18"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "X19"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "X20"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "X21"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "X22"))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "X1"))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "X24"))
        item = self.tableWidget.horizontalHeaderItem(24)
        item.setText(_translate("MainWindow", "Aktual"))
        item = self.tableWidget.horizontalHeaderItem(25)
        item.setText(_translate("MainWindow", "Prediksi"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
