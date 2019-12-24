from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys
import sqlite3
import time
import os


class InsertDialog(QDialog):  # personel ekleme diaglogu
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Kayıt")

        self.setWindowTitle("Kişi Ekle")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle("Kişi Bilgisi Ekle")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.QBtn.clicked.connect(self.addpersonal)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("İsim")
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("Bilgi İşlem")
        self.branchinput.addItem("İnsan Kaynakları")
        self.branchinput.addItem("Muhasebe")
        self.branchinput.addItem("Finansman")
        self.branchinput.addItem("Pazarlama")
        self.branchinput.addItem("İş Güvenliği")
        layout.addWidget(self.branchinput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Telefon No :")
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Adres :")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addpersonal(self):  # personel eklme fonksiyonu

        isim = ""
        dep = ""
        telefon = ""
        adres = ""

        isim = self.nameinput.text()
        dep = self.branchinput.itemText(self.branchinput.currentIndex())
        telefon = self.mobileinput.text()
        adres = self.addressinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO personal (isim,dep,telefon,adres) VALUES (?,?,?,?)",
                           (isim, dep, telefon, adres))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Başarılı', 'Kişi database eklendi.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Hata', 'Kişi database eklenemedi.')


class Updatepersonal(QDialog):
    def __init__(self, *args, **kwargs):
        super(Updatepersonal, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText("Kayıt")

        self.setWindowTitle("Kişi Ekle")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle("Kişi Bilgisi Ekle")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.QBtn.clicked.connect(self.updatepersonal2)

        layout = QVBoxLayout()

        self.idinput = QLineEdit()
        self.idinput.setPlaceholderText("id")
        layout.addWidget(self.idinput)

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("İsim")
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("Bilgi İşlem")
        self.branchinput.addItem("İnsan Kaynakları")
        self.branchinput.addItem("Muhasebe")
        self.branchinput.addItem("Finansman")
        self.branchinput.addItem("Pazarlama")
        self.branchinput.addItem("İş Güvenliği")
        layout.addWidget(self.branchinput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Telefon No :")
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Adres :")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)


    def updatepersonal2(self):  # personel eklme fonksiyonu

        updaterol = self.idinput.text()
        isim = self.nameinput.text()
        dep = self.branchinput.itemText(self.branchinput.currentIndex())
        telefon = self.mobileinput.text()
        adres = self.addressinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE personal SET isim='%s',dep='%s',telefon='%s',adres='%s' WHERE roll='%s'"%(isim,dep,telefon,adres,updaterol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Başarılı', 'Kişi database eklendi.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Hata', 'Kişi database eklenemedi.')


class SearchDialog(QDialog):  # arama diaglogu arama fonk cagırılıyor.
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Ara")

        self.setWindowTitle("Kişi Ara")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchpersonal)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("ID")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchpersonal(self):  # arama fonksiyonu

        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from personal WHERE roll=" + str(searchrol))
            row = result.fetchone()
            serachresult = "ID : " + str(row[0]) + '\n' + "isim: " + str(row[1]) + '\n' + "Dep : " + str(
                row[2]) + '\n' + "Telefon : " + str(row[3]) + '\n' + "Adres  : " + str(row[4])
            QMessageBox.information(QMessageBox(), 'Başarılı', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Hata', 'Kullanıcı databasede değil !')


class DeleteDialog(QDialog):  # personel silme diaglogu personel silme fonk cagırıyoruz.
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Sil")

        self.setWindowTitle("Kişi Sil")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deletepersonal)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("ID")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletepersonal(self):  # personel silme fonksiyonu

        delrol = ""
        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from personal WHERE roll=" + str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Başarılı', 'Tablo silme başarılı')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Hata', 'Kişi tablodan silinemedi')


class AboutDialog(QDialog):  # Hakkımızda diaglogu
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(500)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        self.setWindowTitle("Hakkımızda")
        title = QLabel("KYÇUBYO OTOMASYON SİSTEMİ")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        layout.addWidget(QLabel("2019 Tüm Hakları Saklıdır. Murat Çiçek"))

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/g2.png'))  # pencere ikon

        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS personal(roll INTEGER PRIMARY KEY AUTOINCREMENT ,isim TEXT,dep TEXT,telefon INTEGER,adres TEXT)")
        self.c.close()

        file_menu = self.menuBar().addMenu("&Dosya")

        help_menu = self.menuBar().addMenu("&Hakkımızda")

        self.setWindowTitle("Kyçubyo Personal Otomasyon Sistemi")
        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("ID", "İSİM", "DEPARTMAN", "TELEFON", "ADRES"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("icon/add1.jpg"), "Kişi Ekle", self)  # kişi ekleme ikonu
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add Student")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon("icon/r3.png"), "Refresh", self)  # yenileme ikonu
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/s1.png"), "ARA", self)  # arama ikonu
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Kişi Ara")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("icon/d1.png"), "Sil", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Kişi Sil")
        toolbar.addAction(btn_ac_delete)

        btn_ac_update = QAction(QIcon("icon/p1.png"), "Update", self)
        btn_ac_update.triggered.connect(self.update)
        btn_ac_update.setStatusTip("Kişi Güncelle")
        toolbar.addAction(btn_ac_update)

        adduser_action = QAction(QIcon("icon/add1.jpg"), "Kişi Ekle", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)

        searchuser_action = QAction(QIcon("icon/s1.png"), "Kişi Ara", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)

        deluser_action = QAction(QIcon("icon/d1.png"), "Sil", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)

        about_action = QAction(QIcon("icon/i1.png"), "Gelitirici", self)  # info icon
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)


    def loaddata(self):
        self.connection = sqlite3.connect("database.db")  # sayfa yenileme fonksiyonu
        query = "SELECT * FROM personal"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def insert(self):  # ekle fonksiyonunda ınsert diaglogu cagırıyoruz
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):  # sil fonksiyonunda delete diaglogu cagırıyoruz
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):  # arama fonksiyonunda search diaglogu cagırıyoruz
        dlg = SearchDialog()
        dlg.exec_()

    def update(self):  # update fonksiyonunda hakkımda diaglogu cagırıyoruz
        dlg = Updatepersonal()
        dlg.exec_()

    def about(self):  # hakkımda fonksiyonunda hakkımda diaglogu cagırıyoruz
        dlg = AboutDialog()
        dlg.exec_()




app = QApplication(sys.argv)
if (QDialog.Accepted == True):  # ekrana form nesnesi olusturup döngüye sokuyoruz.
    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())
