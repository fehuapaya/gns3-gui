# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jbbowen/Desktop/Toptal/github/gns3-gui/gns3/modules/vpcs/ui/vpcs_preferences_page.ui'
#
# Created: Tue May 13 13:18:58 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_vpcsPreferencesPageWidget(object):
    def setupUi(self, vpcsPreferencesPageWidget):
        vpcsPreferencesPageWidget.setObjectName(_fromUtf8("vpcsPreferencesPageWidget"))
        vpcsPreferencesPageWidget.resize(432, 508)
        self.vboxlayout = QtGui.QVBoxLayout(vpcsPreferencesPageWidget)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.uiTabWidget = QtGui.QTabWidget(vpcsPreferencesPageWidget)
        self.uiTabWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.uiTabWidget.setObjectName(_fromUtf8("uiTabWidget"))
        self.uiGeneralSettingsTabWidget = QtGui.QWidget()
        self.uiGeneralSettingsTabWidget.setObjectName(_fromUtf8("uiGeneralSettingsTabWidget"))
        self.gridLayout = QtGui.QGridLayout(self.uiGeneralSettingsTabWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.uivpcsPathLineEdit = QtGui.QLineEdit(self.uiGeneralSettingsTabWidget)
        self.uivpcsPathLineEdit.setObjectName(_fromUtf8("uivpcsPathLineEdit"))
        self.horizontalLayout_5.addWidget(self.uivpcsPathLineEdit)
        self.uivpcsPathToolButton = QtGui.QToolButton(self.uiGeneralSettingsTabWidget)
        self.uivpcsPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uivpcsPathToolButton.setObjectName(_fromUtf8("uivpcsPathToolButton"))
        self.horizontalLayout_5.addWidget(self.uivpcsPathToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(164, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.uiTestSettingsPushButton = QtGui.QPushButton(self.uiGeneralSettingsTabWidget)
        self.uiTestSettingsPushButton.setObjectName(_fromUtf8("uiTestSettingsPushButton"))
        self.horizontalLayout_2.addWidget(self.uiTestSettingsPushButton)
        self.uiRestoreDefaultsPushButton = QtGui.QPushButton(self.uiGeneralSettingsTabWidget)
        self.uiRestoreDefaultsPushButton.setObjectName(_fromUtf8("uiRestoreDefaultsPushButton"))
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.uivpcsPathLabel = QtGui.QLabel(self.uiGeneralSettingsTabWidget)
        self.uivpcsPathLabel.setObjectName(_fromUtf8("uivpcsPathLabel"))
        self.gridLayout.addWidget(self.uivpcsPathLabel, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(390, 193, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 2)
        self.uiTabWidget.addTab(self.uiGeneralSettingsTabWidget, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.uiConsolePortRangeGroupBox = QtGui.QGroupBox(self.tab)
        self.uiConsolePortRangeGroupBox.setObjectName(_fromUtf8("uiConsolePortRangeGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.uiConsolePortRangeGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.uiConsoleStartPortSpinBox = QtGui.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleStartPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiConsoleStartPortSpinBox.setMaximum(65535)
        self.uiConsoleStartPortSpinBox.setProperty("value", 4001)
        self.uiConsoleStartPortSpinBox.setObjectName(_fromUtf8("uiConsoleStartPortSpinBox"))
        self.horizontalLayout.addWidget(self.uiConsoleStartPortSpinBox)
        self.uiConsolePortRangeLabel = QtGui.QLabel(self.uiConsolePortRangeGroupBox)
        self.uiConsolePortRangeLabel.setObjectName(_fromUtf8("uiConsolePortRangeLabel"))
        self.horizontalLayout.addWidget(self.uiConsolePortRangeLabel)
        self.uiConsoleEndPortSpinBox = QtGui.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleEndPortSpinBox.setSuffix(_fromUtf8(" TCP"))
        self.uiConsoleEndPortSpinBox.setMaximum(65535)
        self.uiConsoleEndPortSpinBox.setProperty("value", 4500)
        self.uiConsoleEndPortSpinBox.setObjectName(_fromUtf8("uiConsoleEndPortSpinBox"))
        self.horizontalLayout.addWidget(self.uiConsoleEndPortSpinBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.uiConsolePortRangeGroupBox)
        self.uiUDPPortRangeGroupBox = QtGui.QGroupBox(self.tab)
        self.uiUDPPortRangeGroupBox.setObjectName(_fromUtf8("uiUDPPortRangeGroupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.uiUDPPortRangeGroupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.uiUDPStartPortSpinBox = QtGui.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPStartPortSpinBox.setSuffix(_fromUtf8(" UDP"))
        self.uiUDPStartPortSpinBox.setMaximum(65535)
        self.uiUDPStartPortSpinBox.setProperty("value", 30001)
        self.uiUDPStartPortSpinBox.setObjectName(_fromUtf8("uiUDPStartPortSpinBox"))
        self.horizontalLayout_4.addWidget(self.uiUDPStartPortSpinBox)
        self.uiUDPPortRangeLabel = QtGui.QLabel(self.uiUDPPortRangeGroupBox)
        self.uiUDPPortRangeLabel.setObjectName(_fromUtf8("uiUDPPortRangeLabel"))
        self.horizontalLayout_4.addWidget(self.uiUDPPortRangeLabel)
        self.uiUDPEndPortSpinBox = QtGui.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPEndPortSpinBox.setSuffix(_fromUtf8(" UDP"))
        self.uiUDPEndPortSpinBox.setMaximum(65535)
        self.uiUDPEndPortSpinBox.setProperty("value", 40000)
        self.uiUDPEndPortSpinBox.setObjectName(_fromUtf8("uiUDPEndPortSpinBox"))
        self.horizontalLayout_4.addWidget(self.uiUDPEndPortSpinBox)
        spacerItem3 = QtGui.QSpacerItem(147, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.uiUDPPortRangeGroupBox)
        spacerItem4 = QtGui.QSpacerItem(20, 304, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.uiTabWidget.addTab(self.tab, _fromUtf8(""))
        self.vboxlayout.addWidget(self.uiTabWidget)

        self.retranslateUi(vpcsPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(vpcsPreferencesPageWidget)

    def retranslateUi(self, vpcsPreferencesPageWidget):
        vpcsPreferencesPageWidget.setWindowTitle(_translate("vpcsPreferencesPageWidget", "vpcs", None))
        self.uivpcsPathToolButton.setText(_translate("vpcsPreferencesPageWidget", "...", None))
        self.uiTestSettingsPushButton.setText(_translate("vpcsPreferencesPageWidget", "Test settings", None))
        self.uiRestoreDefaultsPushButton.setText(_translate("vpcsPreferencesPageWidget", "Restore defaults", None))
        self.uivpcsPathLabel.setText(_translate("vpcsPreferencesPageWidget", "Path to vpcs:", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiGeneralSettingsTabWidget), _translate("vpcsPreferencesPageWidget", "General settings", None))
        self.uiConsolePortRangeGroupBox.setTitle(_translate("vpcsPreferencesPageWidget", "Console port range", None))
        self.uiConsolePortRangeLabel.setText(_translate("vpcsPreferencesPageWidget", "to", None))
        self.uiUDPPortRangeGroupBox.setTitle(_translate("vpcsPreferencesPageWidget", "UDP tunneling port range", None))
        self.uiUDPPortRangeLabel.setText(_translate("vpcsPreferencesPageWidget", "to", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab), _translate("vpcsPreferencesPageWidget", "Advanced settings", None))

