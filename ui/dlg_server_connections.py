# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_server_connections.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_DlgServerConnections(object):
    def setupUi(self, DlgServerConnections):
        DlgServerConnections.setObjectName(_fromUtf8("DlgServerConnections"))
        DlgServerConnections.resize(690, 487)
        DlgServerConnections.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(DlgServerConnections)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(DlgServerConnections)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 85))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cbxConnections = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbxConnections.sizePolicy().hasHeightForWidth())
        self.cbxConnections.setSizePolicy(sizePolicy)
        self.cbxConnections.setObjectName(_fromUtf8("cbxConnections"))
        self.gridLayout_2.addWidget(self.cbxConnections, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnConnect = QtGui.QPushButton(self.groupBox)
        self.btnConnect.setEnabled(False)
        self.btnConnect.setObjectName(_fromUtf8("btnConnect"))
        self.horizontalLayout_3.addWidget(self.btnConnect)
        self.btnCreateConnection = QtGui.QPushButton(self.groupBox)
        self.btnCreateConnection.setObjectName(_fromUtf8("btnCreateConnection"))
        self.horizontalLayout_3.addWidget(self.btnCreateConnection)
        self.btnEdit = QtGui.QPushButton(self.groupBox)
        self.btnEdit.setEnabled(False)
        self.btnEdit.setObjectName(_fromUtf8("btnEdit"))
        self.horizontalLayout_3.addWidget(self.btnEdit)
        self.btnDelete = QtGui.QPushButton(self.groupBox)
        self.btnDelete.setEnabled(False)
        self.btnDelete.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))
        self.horizontalLayout_3.addWidget(self.btnDelete)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnLoad = QtGui.QPushButton(self.groupBox)
        self.btnLoad.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.horizontalLayout_3.addWidget(self.btnLoad)
        self.btnSave = QtGui.QPushButton(self.groupBox)
        self.btnSave.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout_3.addWidget(self.btnSave)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tblLayers = QtGui.QTableView(DlgServerConnections)
        self.tblLayers.setProperty("showDropIndicator", False)
        self.tblLayers.setAlternatingRowColors(True)
        self.tblLayers.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tblLayers.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblLayers.setSortingEnabled(True)
        self.tblLayers.setCornerButtonEnabled(True)
        self.tblLayers.setObjectName(_fromUtf8("tblLayers"))
        self.tblLayers.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tblLayers, 1, 0, 1, 1)
        self.grpOptions = QtGui.QGroupBox(DlgServerConnections)
        self.grpOptions.setMinimumSize(QtCore.QSize(0, 190))
        self.grpOptions.setObjectName(_fromUtf8("grpOptions"))
        self.gridLayout.addWidget(self.grpOptions, 2, 0, 1, 1)
        self.grpCrs = QtGui.QGroupBox(DlgServerConnections)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpCrs.sizePolicy().hasHeightForWidth())
        self.grpCrs.setSizePolicy(sizePolicy)
        self.grpCrs.setMinimumSize(QtCore.QSize(0, 58))
        self.grpCrs.setObjectName(_fromUtf8("grpCrs"))
        self.gridLayout_5 = QtGui.QGridLayout(self.grpCrs)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.btnChangeCrs = QtGui.QPushButton(self.grpCrs)
        self.btnChangeCrs.setObjectName(_fromUtf8("btnChangeCrs"))
        self.gridLayout_3.addWidget(self.btnChangeCrs, 0, 1, 1, 1)
        self.lblCrs = QtGui.QLabel(self.grpCrs)
        self.lblCrs.setObjectName(_fromUtf8("lblCrs"))
        self.gridLayout_3.addWidget(self.lblCrs, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.grpCrs, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.chkKeepOpen = QtGui.QCheckBox(DlgServerConnections)
        self.chkKeepOpen.setObjectName(_fromUtf8("chkKeepOpen"))
        self.horizontalLayout.addWidget(self.chkKeepOpen, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.btnAdd = QtGui.QPushButton(DlgServerConnections)
        self.btnAdd.setEnabled(False)
        self.btnAdd.setMinimumSize(QtCore.QSize(80, 0))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnClose = QtGui.QPushButton(DlgServerConnections)
        self.btnClose.setMinimumSize(QtCore.QSize(80, 0))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.horizontalLayout.addWidget(self.btnClose)
        self.btnHelp = QtGui.QPushButton(DlgServerConnections)
        self.btnHelp.setMinimumSize(QtCore.QSize(80, 0))
        self.btnHelp.setObjectName(_fromUtf8("btnHelp"))
        self.horizontalLayout.addWidget(self.btnHelp)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(DlgServerConnections)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL(_fromUtf8("clicked()")), DlgServerConnections.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgServerConnections)

    def retranslateUi(self, DlgServerConnections):
        DlgServerConnections.setWindowTitle(_translate("DlgServerConnections", "Add Layer(s) from a Vector Tile Source", None))
        self.groupBox.setTitle(_translate("DlgServerConnections", "Connections", None))
        self.btnConnect.setText(_translate("DlgServerConnections", "Connect", None))
        self.btnCreateConnection.setText(_translate("DlgServerConnections", "New", None))
        self.btnEdit.setText(_translate("DlgServerConnections", "Edit", None))
        self.btnDelete.setText(_translate("DlgServerConnections", "Delete", None))
        self.btnLoad.setText(_translate("DlgServerConnections", "Load", None))
        self.btnSave.setText(_translate("DlgServerConnections", "Save", None))
        self.grpOptions.setTitle(_translate("DlgServerConnections", "Options", None))
        self.grpCrs.setTitle(_translate("DlgServerConnections", "Coordinate reference system", None))
        self.btnChangeCrs.setText(_translate("DlgServerConnections", "Change", None))
        self.lblCrs.setText(_translate("DlgServerConnections", "not implemented", None))
        self.chkKeepOpen.setText(_translate("DlgServerConnections", "Keep dialog open", None))
        self.btnAdd.setText(_translate("DlgServerConnections", "Add", None))
        self.btnClose.setText(_translate("DlgServerConnections", "Close", None))
        self.btnHelp.setText(_translate("DlgServerConnections", "Help", None))

