# -*- coding: utf-8 -*-
""" BriarIDS menu loader: Creates a python desktop application.

Desktop application allows you to install Suricata, Bro, Critical Stack Agent 
and Virus Total Scanner via selectable button options.  

Follow wiki at https://github.com/musicmancorley/BriarIDS/wiki for latest docs.

"""

from PyQt4 import QtCore, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class UiForm:

    """Primary class that creates the BriarIDS desktop application
    
    Creates the desktop application, as well as runs bash script's depending on which button is 
    pressed.
    
    """

    def setup_ui(self, Form):
        """Sets up the outline of the UI.
        
        Instantiates all the classes from the pyQt4 program and then defines the size,shape, layout of
        all the UI elements.
        
        param Form: pyQt4 form object
        """

        Form.setObjectName(_fromUtf8("Form"))
        Form.setFixedSize(QtCore.QSize(454, 703))
        
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tempus Sans ITC"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)
        self.label = QtGui.QLabel(Form)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/bateman-in-the-brier-patch-crop.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(True)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 8, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 7, 0, 1, 2)
        self.pushButton_5 = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoFillBackground(True)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 6, 0, 1, 2)
        self.pushButton_8 = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setAutoFillBackground(True)
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 12, 0, 1, 2)

        self.retranslate_ui(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslate_ui(self, Form):
        """Adds text to created UI elements"""

        Form.setWindowTitle(_translate("Form", "BriarIDS", None))
        self.pushButton.setToolTip(_translate("Form", "This installs Suricata and also checks if Suricata is already installed", None))
        self.pushButton.setText(_translate("Form", "Install Suricata", None))
        self.pushButton.clicked.connect(self.install)
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; color:#0055ff;\">Welcome to BriarIDS -  designed for the Raspberry Pi</span></p></body></html>", None))
        self.pushButton_2.setToolTip(_translate("Form", "This starts the Suricata IDS engine and displays log alerts in the terminal", None))
        self.pushButton_2.setText(_translate("Form", "Run Suricata", None))
        self.pushButton_2.clicked.connect(self.runtheprog)
        self.pushButton_4.setToolTip(_translate("Form", "Add in your public/WAN IP", None))
        self.pushButton_4.setText(_translate("Form", "Add WAN IP to config for monitoring", None))
        self.pushButton_5.setToolTip(_translate("Form", "This installs Bro and the Critical Stack Intel Feed client", None))
        self.pushButton_5.setText(_translate("Form", "Install/Configure/Run Bro AND Intel Agent!", None))
        self.pushButton_5.clicked.connect(self.brointelinstall)
        self.pushButton_4.clicked.connect(self.configcheck)
        self.pushButton_8.setToolTip(_translate("Form", "Runs the VirusTotal Scanner against your extracted files!", None))
        self.pushButton_8.setText(_translate("Form", "Virus Total File Scanner (new!)", None))
        self.pushButton_8.clicked.connect(self.vtotalscanner)
        self.comboBox.setItemText(0, _translate("Form", "eth0", None))
        self.comboBox.setItemText(1, _translate("Form", "eth1", None))
        self.comboBox.setItemText(2, _translate("Form", "eth2", None))
        self.comboBox.setItemText(3, _translate("Form", "eth3", None))
        self.comboBox.setItemText(4, _translate("Form", "eth4", None))
        self.comboBox.setItemText(5, _translate("Form", "wlan0", None))
        self.comboBox.setItemText(6, _translate("Form", "wlan1", None))
        self.label_3.setText(_translate("Form", "<span style='font-size:8pt'>CHOOSE SURICATA MONITOR INTERFACE:</span>", None))

    def install(self):
        """Runs the suricata install bash shell script when 'Install Suricata' button pressed"""

        print("Installation routine initializing...")
        os.system("x-terminal-emulator -e './suricata-install-script.sh'")

    def runtheprog(self):
        """Start's suricata when 'Run Suricata' button pressed"""

        monint = str(self.comboBox.currentText())
        print("Configuring interface using Ethtool...")
        os.system("ethtool -K " + monint + " tx off rx off sg off gso off gro off" + " 2>/dev/null")
        print("Note: You can view your alert logs by issuing the following command: tail -f /var/log/suricata/http.log /var/log/suricata/fast.log")
        print("Even better, you are encouraged to use the new WEB GUI log management interface, TheBriarPatch, specifically for BriarIDS!")
        print("Go here to clone it: https://github.com/musicmancorley/TheBriarPatch")
        os.system("sleep 5")
        print("Starting Suricata!!!")
        os.system("./rulecleanup.sh")
        mycommand = '/opt/suricata/bin/suricata -c /opt/suricata/etc/suricata/suricata.yaml --af-packet=' + monint + " -D"
        print("Suricata has been started and has been minimized/daemonized")
        print("please allow 30-60 seconds for it to complete the initialization process")
        os.system("x-terminal-emulator -e " + mycommand)

    def configcheck(self):
        """Python system call that runs script that makes sure BriarIDS is installed and that a WAN IP entered"""

        os.system("./configcheck.sh")

    def brointelinstall(self):
        """Python system call that runs script that installs/configures Bro."""
        os.system("./bromenu.sh")

    def vtotalscanner(self):
        """Python system call that runs script that runs vtotalscanner scripts"""

        os.system("./filetypescan.sh")

import main_rc
