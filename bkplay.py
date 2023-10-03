import datetime
import os
import shutil
from zipfile import ZipFile
import fdb
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from bkp_connectionstring import connectionstring
import time
import schedule


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 445)
        self.getcon = connectionstring()  # cria objeto da classe connectionstring
        self.getcon.createdatabase()
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 991, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_fb = QtWidgets.QWidget()
        self.tab_fb.setObjectName("tab_fb")
        self.cb_qui_fb = QtWidgets.QCheckBox(parent=self.tab_fb)
        self.cb_qui_fb.setGeometry(QtCore.QRect(730, 30, 31, 20))
        self.cb_qui_fb.setObjectName("cb_qui_fb")
        self.cb_sex_fb = QtWidgets.QCheckBox(parent=self.tab_fb)
        self.cb_sex_fb.setGeometry(QtCore.QRect(770, 30, 31, 20))
        self.cb_sex_fb.setObjectName("cb_sex_fb")
        self.lbl_user_fb = QtWidgets.QLabel(parent=self.tab_fb)
        self.lbl_user_fb.setGeometry(QtCore.QRect(150, 10, 51, 16))
        self.lbl_user_fb.setObjectName("lbl_user_fb")
        self.lbl_ip_fb = QtWidgets.QLabel(parent=self.tab_fb)
        self.lbl_ip_fb.setGeometry(QtCore.QRect(380, 10, 16, 16))
        self.lbl_ip_fb.setObjectName("lbl_ip_fb")
        self.lbl_pass_fb = QtWidgets.QLabel(parent=self.tab_fb)
        self.lbl_pass_fb.setGeometry(QtCore.QRect(280, 10, 41, 16))
        self.lbl_pass_fb.setObjectName("lbl_pass_fb")
        self.cb_ter_fb = QtWidgets.QCheckBox(parent=self.tab_fb)
        self.cb_ter_fb.setGeometry(QtCore.QRect(650, 30, 31, 20))
        self.cb_ter_fb.setObjectName("cb_ter_fb")
        self.lbl_port_fb = QtWidgets.QLabel(parent=self.tab_fb)
        self.lbl_port_fb.setGeometry(QtCore.QRect(500, 10, 31, 16))
        self.lbl_port_fb.setObjectName("lbl_port_fb")
        self.edt_port_fb = QtWidgets.QLineEdit(parent=self.tab_fb)
        self.edt_port_fb.setGeometry(QtCore.QRect(500, 30, 51, 22))
        self.edt_port_fb.setText("3050")
        self.edt_port_fb.setObjectName("edt_port_fb")
        self.cb_sab_fb = QtWidgets.QCheckBox(parent=self.tab_fb)
        self.cb_sab_fb.setGeometry(QtCore.QRect(810, 30, 31, 20))
        self.cb_sab_fb.setObjectName("cb_sab_fb")
        self.edt_id_fb = QtWidgets.QLineEdit(parent=self.tab_fb)
        self.edt_id_fb.setGeometry(QtCore.QRect(20, 90, 113, 22))
        self.edt_id_fb.setObjectName("edt_id_fb")
        self.edt_bd_fb = QtWidgets.QLineEdit(parent=self.tab_fb)
        self.edt_bd_fb.setGeometry(QtCore.QRect(160, 90, 221, 22))
        self.edt_bd_fb.setObjectName("edt_bd_fb")
        self.btn_save_fb = QtWidgets.QPushButton(parent=self.tab_fb)
        self.btn_save_fb.setGeometry(QtCore.QRect(890, 380, 75, 24))
        self.btn_save_fb.setObjectName("btn_save_fb")
        self.btn_save_fb.clicked.connect(self.insertData_FB)
        self.edt_pass_fb = QtWidgets.QLineEdit(parent=self.tab_fb)
        self.edt_pass_fb.setGeometry(QtCore.QRect(280, 30, 81, 22))
        self.edt_pass_fb.setObjectName("edt_pass_fb")
        self.edt_pass_fb.setText("masterkey")
        self.edt_pass_fb.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.btn_destino_fb = QtWidgets.QPushButton(parent=self.tab_fb)
        self.btn_destino_fb.setGeometry(QtCore.QRect(760, 90, 75, 24))
        self.btn_destino_fb.clicked.connect(self.destino)
        self.btn_testebkp_fb = QtWidgets.QPushButton(parent=self.tab_fb)
        self.btn_testebkp_fb.setGeometry(QtCore.QRect(660, 90, 75, 24))
        self.btn_testebkp_fb.clicked.connect(self.backup_eco)
        self.cb_seg_fb = QtWidgets.QCheckBox(parent=self.tab_fb)
        self.cb_seg_fb.setGeometry(QtCore.QRect(610, 30, 31, 20))
        self.cb_seg_fb.setObjectName("cb_seg_fb")
        self.timeEdit_fb = QtWidgets.QTimeEdit(parent=self.tab_fb)
        self.timeEdit_fb.setGeometry(QtCore.QRect(860, 30, 51, 22))
        self.timeEdit_fb.setObjectName("timeEdit_fb")
        self.lbl_bd_fb = QtWidgets.QLabel(parent=self.tab_fb)
        self.lbl_bd_fb.setGeometry(QtCore.QRect(160, 70, 161, 16))
        self.lbl_bd_fb.setObjectName("lbl_bd_fb")
        self.edt_user_fb = QtWidgets.QLineEdit(parent=self.tab_fb)
        self.edt_user_fb.setGeometry(QtCore.QRect(150, 30, 91, 22))
        self.edt_user_fb.setObjectName("edt_user_fb")
        self.edt_user_fb.setText("sysdba")
        self.savedata_fb = QtWidgets.QPushButton(parent=self.tab_fb)
        self.savedata_fb.setGeometry(QtCore.QRect(870, 90, 91, 24))
        self.savedata_fb.setObjectName("savedata_fb")
        self.savedata_fb.clicked.connect(self.checkfields_fb)
        self.lbl_id_fb = QtWidgets.QLabel(parent=self.tab_fb)
        self.lbl_id_fb.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.lbl_id_fb.setObjectName("lbl_id_fb")
        self.cb_qua_fb = QtWidgets.QCheckBox(parent=self.tab_fb)
        self.cb_qua_fb.setGeometry(QtCore.QRect(690, 30, 31, 20))
        self.cb_qua_fb.setObjectName("cb_qua_fb")
        self.cb_dom_fb = QtWidgets.QCheckBox(parent=self.tab_fb)
        self.cb_dom_fb.setGeometry(QtCore.QRect(570, 30, 31, 20))
        self.cb_dom_fb.setObjectName("cb_dom_fb")
        self.lbl_time_fb = QtWidgets.QLabel(parent=self.tab_fb)
        self.lbl_time_fb.setGeometry(QtCore.QRect(860, 10, 41, 16))
        self.lbl_time_fb.setObjectName("lbl_time_fb")
        self.edt_ip_fb = QtWidgets.QLineEdit(parent=self.tab_fb)
        self.edt_ip_fb.setGeometry(QtCore.QRect(380, 30, 101, 22))
        self.edt_ip_fb.setObjectName("edt_ip_fb")
        self.edt_ip_fb.setText("127.0.0.1")
        self.search_dtb = QtWidgets.QPushButton(parent=self.tab_fb)
        self.search_dtb.setGeometry(QtCore.QRect(390, 90, 61, 24))
        self.search_dtb.setObjectName("search_dtb")
        self.search_dtb.clicked.connect(self.find_database)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.tab_fb)
        self.tableWidget.setGeometry(QtCore.QRect(10, 121, 961, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(87)
        self.tabWidget.addTab(self.tab_fb, "")
        self.tab_pg = QtWidgets.QWidget()
        self.tab_pg.setObjectName("tab_pg")
        self.cb_qui = QtWidgets.QCheckBox(parent=self.tab_pg)
        self.cb_qui.setGeometry(QtCore.QRect(730, 30, 31, 20))
        self.cb_qui.setObjectName("cb_qui")
        self.cb_sex = QtWidgets.QCheckBox(parent=self.tab_pg)
        self.cb_sex.setGeometry(QtCore.QRect(770, 30, 31, 20))
        self.cb_sex.setObjectName("cb_sex")
        self.lbl_user = QtWidgets.QLabel(parent=self.tab_pg)
        self.lbl_user.setGeometry(QtCore.QRect(150, 10, 51, 16))
        self.lbl_user.setObjectName("lbl_user")
        self.lbl_ip = QtWidgets.QLabel(parent=self.tab_pg)
        self.lbl_ip.setGeometry(QtCore.QRect(380, 10, 16, 16))
        self.lbl_ip.setObjectName("lbl_ip")
        self.lbl_pass = QtWidgets.QLabel(parent=self.tab_pg)
        self.lbl_pass.setGeometry(QtCore.QRect(280, 10, 41, 16))
        self.lbl_pass.setObjectName("lbl_pass")
        self.cb_ter = QtWidgets.QCheckBox(parent=self.tab_pg)
        self.cb_ter.setGeometry(QtCore.QRect(650, 30, 31, 20))
        self.cb_ter.setObjectName("cb_ter")
        self.lbl_port = QtWidgets.QLabel(parent=self.tab_pg)
        self.lbl_port.setGeometry(QtCore.QRect(500, 10, 31, 16))
        self.lbl_port.setObjectName("lbl_port")
        self.edt_port = QtWidgets.QLineEdit(parent=self.tab_pg)
        self.edt_port.setGeometry(QtCore.QRect(500, 30, 51, 22))
        self.edt_port.setObjectName("edt_port")
        self.edt_port.setText("5432")
        self.cb_sab = QtWidgets.QCheckBox(parent=self.tab_pg)
        self.cb_sab.setGeometry(QtCore.QRect(810, 30, 31, 20))
        self.cb_sab.setObjectName("cb_sab")
        self.edt_id = QtWidgets.QLineEdit(parent=self.tab_pg)
        self.edt_id.setGeometry(QtCore.QRect(20, 90, 113, 22))
        self.edt_id.setObjectName("edt_id")
        self.edt_bd = QtWidgets.QLineEdit(parent=self.tab_pg)
        self.edt_bd.setGeometry(QtCore.QRect(20, 30, 101, 22))
        self.edt_bd.setObjectName("edt_bd")
        self.edt_bd.setText("ecodados")
        self.btn_save = QtWidgets.QPushButton(parent=self.tab_pg)
        self.btn_save.setGeometry(QtCore.QRect(890, 380, 75, 24))
        self.btn_save.setObjectName("btn_save")
        self.edt_pass = QtWidgets.QLineEdit(parent=self.tab_pg)
        self.edt_pass.setGeometry(QtCore.QRect(280, 30, 81, 22))
        self.edt_pass.setObjectName("edt_pass")
        self.edt_pass.setText("postgres")
        self.edt_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.cb_seg = QtWidgets.QCheckBox(parent=self.tab_pg)
        self.cb_seg.setGeometry(QtCore.QRect(610, 30, 31, 20))
        self.cb_seg.setObjectName("cb_seg")
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.tab_pg)
        self.timeEdit.setGeometry(QtCore.QRect(860, 30, 51, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.lbl_bd = QtWidgets.QLabel(parent=self.tab_pg)
        self.lbl_bd.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.lbl_bd.setObjectName("lbl_bd")
        self.edt_user = QtWidgets.QLineEdit(parent=self.tab_pg)
        self.edt_user.setGeometry(QtCore.QRect(150, 30, 91, 22))
        self.edt_user.setObjectName("edt_user")
        self.edt_user.setText("postgres")
        self.savedata = QtWidgets.QPushButton(parent=self.tab_pg)
        self.savedata.setGeometry(QtCore.QRect(870, 90, 91, 24))
        self.savedata.setObjectName("savedata")
        self.lbl_id = QtWidgets.QLabel(parent=self.tab_pg)
        self.lbl_id.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.lbl_id.setObjectName("lbl_id")
        self.cb_qua = QtWidgets.QCheckBox(parent=self.tab_pg)
        self.cb_qua.setGeometry(QtCore.QRect(690, 30, 31, 20))
        self.cb_qua.setObjectName("cb_qua")
        self.cb_dom = QtWidgets.QCheckBox(parent=self.tab_pg)
        self.cb_dom.setGeometry(QtCore.QRect(570, 30, 31, 20))
        self.cb_dom.setObjectName("cb_dom")
        self.lbl_time = QtWidgets.QLabel(parent=self.tab_pg)
        self.lbl_time.setGeometry(QtCore.QRect(860, 10, 41, 16))
        self.lbl_time.setObjectName("lbl_time")
        self.edt_ip = QtWidgets.QLineEdit(parent=self.tab_pg)
        self.edt_ip.setGeometry(QtCore.QRect(380, 30, 101, 22))
        self.edt_ip.setObjectName("edt_ip")
        self.edt_ip.setText("127.0.0.1")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.tab_pg)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 120, 961, 251))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(11)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(87)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_pg, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.tableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loadfields()
        # self.getData()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Backup Banco de Dados"))
        self.btn_destino_fb.setText(_translate("MainWindow", "Destino"))
        self.cb_qui_fb.setText(_translate("MainWindow", "Q"))
        self.cb_sex_fb.setText(_translate("MainWindow", "S"))
        self.lbl_user_fb.setText(_translate("MainWindow", "Usuário"))
        self.lbl_ip_fb.setText(_translate("MainWindow", "IP"))
        self.lbl_pass_fb.setText(_translate("MainWindow", "Senha"))
        self.cb_ter_fb.setText(_translate("MainWindow", "T"))
        self.lbl_port_fb.setText(_translate("MainWindow", "Porta"))
        self.cb_sab_fb.setText(_translate("MainWindow", "S"))
        self.btn_save_fb.setText(_translate("MainWindow", "Salvar"))
        self.cb_seg_fb.setText(_translate("MainWindow", "S"))
        self.lbl_bd_fb.setText(_translate("MainWindow", "Caminho do banco de dados"))
        self.savedata_fb.setText(_translate("MainWindow", "Inserir dados"))
        self.lbl_id_fb.setText(_translate("MainWindow", "Identificação"))
        self.cb_qua_fb.setText(_translate("MainWindow", "Q"))
        self.cb_dom_fb.setText(_translate("MainWindow", "D"))
        self.lbl_time_fb.setText(_translate("MainWindow", "Horário"))
        self.search_dtb.setText(_translate("MainWindow", "..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Banco"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Destino"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Identificação"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "S"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "T"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Q"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Q"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "S"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "S"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Hora"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_fb), _translate("MainWindow", "Firebird")
        )
        self.cb_qui.setText(_translate("MainWindow", "Q"))
        self.cb_sex.setText(_translate("MainWindow", "S"))
        self.lbl_user.setText(_translate("MainWindow", "Usuário"))
        self.lbl_ip.setText(_translate("MainWindow", "IP"))
        self.lbl_pass.setText(_translate("MainWindow", "Senha"))
        self.cb_ter.setText(_translate("MainWindow", "T"))
        self.lbl_port.setText(_translate("MainWindow", "Porta"))
        self.cb_sab.setText(_translate("MainWindow", "S"))
        self.btn_save.setText(_translate("MainWindow", "Salvar"))
        self.cb_seg.setText(_translate("MainWindow", "S"))
        self.lbl_bd.setText(_translate("MainWindow", "Banco de dados"))
        self.savedata.setText(_translate("MainWindow", "Inserir dados"))
        self.lbl_id.setText(_translate("MainWindow", "Identificação"))
        self.cb_qua.setText(_translate("MainWindow", "Q"))
        self.cb_dom.setText(_translate("MainWindow", "D"))
        self.lbl_time.setText(_translate("MainWindow", "Horário"))
        self.btn_testebkp_fb.setText(_translate("MainWindow", "Teste"))
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Banco"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Destino"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Identificação"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "S"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "T"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Q"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Q"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "S"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "S"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Hora"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_pg), _translate("MainWindow", "PostgreSQL")
        )

    def loadfields(self):
        query = "select * from tbases"
        self.getcon.cursor.execute(query)
        self.fetch = self.getcon.cursor.fetchall()
        print(self.fetch)
        for x in self.fetch:
            self.edt_bd_fb.setText(x[1])
            self.edt_id_fb.setText(x[6])
            self.edt_ip_fb.setText(x[2])
            self.edt_pass_fb.setText(x[5])
            self.edt_port_fb.setText(x[3])
            self.edt_user_fb.setText(x[4])
            self.timeEdit_fb.setTime(x[15])
            if x[8] == "S":
                self.cb_dom_fb.checkStateSet()
            if x[9] == "S":
                self.cb_sex_fb.checkStateSet()
            if x[10] == "S":
                self.cb_ter_fb.checkStateSet()
            if x[11] == "S":
                self.cb_qua_fb.checkStateSet()
            if x[12] == "S":
                self.cb_qui_fb.checkStateSet()
            if x[13] == "S":
                self.cb_sex_fb.checkStateSet()
            if x[14] == "S":
                self.cb_sab_fb.checkStateSet()
        self.getcon.cursor.close()
        self.scheduler()

    def find_database(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(
            parent=MainWindow,
            caption="selecione um arquivo",
            directory=os.getcwd(),
            filter="Banco de dados(*.eco)",
        )
        self.edt_bd_fb.setText(str(self.fname[0]))
        print(self.fname[0])

    def destino(self):
        self.folder = QtWidgets.QFileDialog.getExistingDirectory(
            parent=MainWindow, caption="Selecione uma pasta", directory=os.getcwd()
        )

    def checkfields_fb(self):
        if (
            self.cb_dom_fb.isChecked()
            or self.cb_seg_fb.isChecked()
            or self.cb_ter_fb.isChecked()
            or self.cb_qua_fb.isChecked()
            or self.cb_qui_fb.isChecked()
            or self.cb_sex_fb.isChecked()
            or self.cb_sab_fb.isChecked()
        ):
            if not self.edt_bd_fb.text() == "":
                if not self.edt_id_fb.text() == "":
                    if not self.edt_ip_fb.text() == "":
                        if not self.edt_port_fb.text() == "":
                            if not self.edt_user_fb.text() == "":
                                if not self.edt_pass_fb.text() == "":
                                    print("todos os campos estão setados")
                                    self.fillTablefb()
                                else:
                                    print("senha nao setada")
                            else:
                                print("usuario nao setado")
                        else:
                            print("porta nao setada")
                    else:
                        print("ip nao setado")
                else:
                    print("id nao setado")
            else:
                print("banco de dados nao setado")
        else:
            print("dia da semana não setado")

    def checkfields_pg(self):
        pass

    def loadfields(self):
        query = "select * from tbases"
        count = "select count(*) from tbases"
        self.getcon.cursor.execute(query)
        self.fetch = self.getcon.cursor.fetchall()
        self.getcon.cursor.execute(count)
        self.getcount = self.getcon.cursor.fetchone()
        print(self.fetch)
        row = self.getcount[0]
        print(row)
        rowPosition = self.tableWidget.rowCount()
        print(rowPosition)
        # self.tableWidget.setRowCount(row)
        for x in self.fetch:
            self.tableWidget.setItem(row - 1, 0, QtWidgets.QTableWidgetItem(x[1]))
            self.tableWidget.setItem(row - 1, 1, QtWidgets.QTableWidgetItem(x[7]))
            self.tableWidget.setItem(row - 1, 2, QtWidgets.QTableWidgetItem(x[6]))
            self.tableWidget.setItem(row - 1, 3, QtWidgets.QTableWidgetItem(x[8]))
            self.tableWidget.setItem(row - 1, 4, QtWidgets.QTableWidgetItem(x[9]))
            self.tableWidget.setItem(row - 1, 5, QtWidgets.QTableWidgetItem(x[10]))
            self.tableWidget.setItem(row - 1, 6, QtWidgets.QTableWidgetItem(x[11]))
            self.tableWidget.setItem(row - 1, 7, QtWidgets.QTableWidgetItem(x[12]))
            self.tableWidget.setItem(row - 1, 8, QtWidgets.QTableWidgetItem(x[13]))
            self.tableWidget.setItem(row - 1, 9, QtWidgets.QTableWidgetItem(x[14]))
            self.tableWidget.setItem(row - 1, 10, QtWidgets.QTableWidgetItem(x[15]))

    def fillTablefb(self):
        self.filename = os.path.basename(self.edt_bd_fb.text())
        row = 0
        remsubstr = self.filename[:-3]
        self.result = remsubstr + "GBK"
        print(f"Database: {self.filename}")
        print(f"Gbak target: {self.result}")

        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(self.filename))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(self.folder))
        self.tableWidget.setItem(
            row, 2, QtWidgets.QTableWidgetItem(self.edt_id_fb.text())
        )

        self.tableWidget.setItem(
            row,
            3,
            QtWidgets.QTableWidgetItem(
                "S" if self.cb_dom_fb.isChecked() == True else "N"
            ),
        )
        self.tableWidget.setItem(
            row,
            4,
            QtWidgets.QTableWidgetItem(
                "S" if self.cb_seg_fb.isChecked() == True else "N"
            ),
        )
        self.tableWidget.setItem(
            row,
            5,
            QtWidgets.QTableWidgetItem(
                "S" if self.cb_ter_fb.isChecked() == True else "N"
            ),
        )
        self.tableWidget.setItem(
            row,
            6,
            QtWidgets.QTableWidgetItem(
                "S" if self.cb_qua_fb.isChecked() == True else "N"
            ),
        )
        self.tableWidget.setItem(
            row,
            7,
            QtWidgets.QTableWidgetItem(
                "S" if self.cb_qui_fb.isChecked() == True else "N"
            ),
        )
        self.tableWidget.setItem(
            row,
            8,
            QtWidgets.QTableWidgetItem(
                "S" if self.cb_sex_fb.isChecked() == True else "N"
            ),
        )
        self.tableWidget.setItem(
            row,
            9,
            QtWidgets.QTableWidgetItem(
                "S" if self.cb_sab_fb.isChecked() == True else "N"
            ),
        )
        self.tableWidget.setItem(
            row, 10, QtWidgets.QTableWidgetItem(self.timeEdit_fb.text())
        )

    def insertData_FB(self):
        dom = "S" if self.cb_dom_fb.isChecked() == True else "N"
        seg = "S" if self.cb_seg_fb.isChecked() == True else "N"
        ter = "S" if self.cb_ter_fb.isChecked() == True else "N"
        qua = "S" if self.cb_qua_fb.isChecked() == True else "N"
        qui = "S" if self.cb_qui_fb.isChecked() == True else "N"
        sex = "S" if self.cb_sex_fb.isChecked() == True else "N"
        sab = "S" if self.cb_sab_fb.isChecked() == True else "N"
        try:
            self.getcon.cursor.execute(
                f"""INSERT INTO TBASES (BANCO,
                                        IP,
                                        PORTA,
                                        USUARIO,
                                        SENHA,
                                        IDENTIFICACAO,
                                        DESTINO,
                                        DOMINGO,
                                        SEGUNDA,
                                        TERCA,
                                        QUARTA,
                                        QUINTA,
                                        SEXTA,
                                        SABADO,
                                        HORA)
                                VALUES ('{self.fname[0]}',
                                        '{self.edt_ip_fb.text()}',
                                        '{self.edt_port_fb.text()}',
                                        '{self.edt_user_fb.text()}',
                                        '{self.edt_pass_fb.text()}',
                                        '{self.edt_id_fb.text()}',
                                        '{self.folder}',
                                        '{dom}',
                                        '{seg}',
                                        '{ter}',
                                        '{qua}',
                                        '{qui}',
                                        '{sex}',
                                        '{sab}',
                                        '{self.timeEdit_fb.text()}')
                                """
            )
            self.getcon.connection.commit()
            QMessageBox.information(MainWindow, "Aviso", "Backup agendado com sucesso!")
            self.scheduler()
        except Exception as e:
            QMessageBox.warning(MainWindow, "Erro", e)

    def deleteBkp(self):
        query = "delete from tbases where "

    def getData(self):
        query = "select * from tbases"
        self.getcon.cursor.execute(query)
        show = self.getcon.cursor.fetchall()
        print(show)
        self.getcon.cursor.close()

    def scheduler(self):
        query = "select * from tbases"
        self.getcon.cursor.execute(query)
        self.fetch = self.getcon.cursor.fetchall()
        for x in self.fetch:
            if x[8] == "S":
                schedule.every().sunday.at(x[15]).do(self.backup_eco)
            if x[9] == "S":
                schedule.every().monday.at(x[15]).do(self.backup_eco)
            if x[10] == "S":
                schedule.every().tuesday.at(x[15]).do(self.backup_eco)
            if x[11] == "S":
                schedule.every().wednesday.at(x[15]).do(self.backup_eco)
            if x[12] == "S":
                schedule.every().thursday.at(x[15]).do(self.backup_eco)
            if x[13] == "S":
                schedule.every().friday.at(x[15]).do(self.backup_eco)
            if x[14] == "S":
                schedule.every().saturday.at(x[15]).do(self.backup_eco)
            while True:
                schedule.run_pending()
                time.sleep(1)

    def backup_eco(self):
        self.inst = SubWindow()
        self.inst.show()
        query = "select * from tbases"
        self.getcon.cursor.execute(query)
        self.fetch = self.getcon.cursor.fetchall()
        for x in self.fetch:
            self.filename = os.path.basename(x[1])
        remsubstr = self.filename[:-3]
        self.result = remsubstr + "GBK"
        now = datetime.datetime.now()
        date_time = now.strftime("%d%m%y%H%M")
        path = "C:/TemporaryBackup/"
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            print("Creating directory..")
        filecopy = shutil.copy(x[1], path)
        getfile = os.path.basename(x[1])
        getEco = path + getfile  # Temporary folder directory with file added .eco
        getGbk = path + self.result  # Temporary folder directory with file added .gbk
        svc = fdb.services.connect(password=x[5])
        print("Fetch materialized")
        print("==================")
        print("Start backup")
        svc.backup(getEco, getGbk)
        print("svc.fetching is"), svc.fetching
        print("svc.running is"), svc.isrunning()
        report = svc.readlines()
        print("All lines of backup:")
        for i in report:
            self.inst.label.setText(i)
            print(i)
        print("Backup done...")
        svc.close()
        print("Removing database.."), os.remove(getEco)
        os.rename(getGbk, path + date_time + "_" + self.result)
        print(path + date_time + self.result)
        getPath = path + date_time + "_" + self.result
        print(f"Renamed to filedate")
        print("Calling zip..")
        removeGbk = getPath[:-3]  # Removing .gbk on string
        getzipFile = removeGbk + "zip"  # Adding .zip extension
        zip = ZipFile(getzipFile, "w")
        zip.write(getPath)
        print("Compressed file: ")
        print(getzipFile)
        print("Closing zip..")
        zip.close()
        print("Moving the .zip file on destination folder")
        shutil.move(getzipFile, x[7])
        print("Removing .Gbk file")
        os.remove(getPath)
        print("Done!")
        svc.close()
        self.getcon.connection.close()


class SubWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SubWindow, self).__init__()
        self.resize(400, 300)
        self.setWindowTitle("Backup Log")

        # Label
        self.label = QtWidgets.QTextEdit(self)
        self.label.setGeometry(0, 0, 400, 300)
        self.label.setText("ok")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec())
