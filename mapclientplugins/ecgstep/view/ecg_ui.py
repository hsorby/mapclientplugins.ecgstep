# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ecgwidget.ui'
#
# Created: Wed Sep 19 17:00:37 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MeshGeneratorWidget(object):
    def setupUi(self, MeshGeneratorWidget):
        MeshGeneratorWidget.setObjectName("MeshGeneratorWidget")
        MeshGeneratorWidget.resize(927, 829)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MeshGeneratorWidget.sizePolicy().hasHeightForWidth())
        MeshGeneratorWidget.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QtGui.QGridLayout(MeshGeneratorWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dockWidget = QtGui.QDockWidget(MeshGeneratorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(390, 436))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 366, 456))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.time_groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.time_groupBox.setObjectName("time_groupBox")
        self.gridLayout_4 = QtGui.QGridLayout(self.time_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.timeValue_doubleSpinBox = QtGui.QDoubleSpinBox(self.time_groupBox)
        self.timeValue_doubleSpinBox.setMaximum(12000.0)
        self.timeValue_doubleSpinBox.setObjectName("timeValue_doubleSpinBox")
        self.gridLayout_4.addWidget(self.timeValue_doubleSpinBox, 0, 1, 1, 1)
        self.timeLoop_checkBox = QtGui.QCheckBox(self.time_groupBox)
        self.timeLoop_checkBox.setObjectName("timeLoop_checkBox")
        self.gridLayout_4.addWidget(self.timeLoop_checkBox, 1, 2, 1, 1)
        self.timeValue_label = QtGui.QLabel(self.time_groupBox)
        self.timeValue_label.setObjectName("timeValue_label")
        self.gridLayout_4.addWidget(self.timeValue_label, 0, 0, 1, 1)
        self.timePlayStop_pushButton = QtGui.QPushButton(self.time_groupBox)
        self.timePlayStop_pushButton.setObjectName("timePlayStop_pushButton")
        self.gridLayout_4.addWidget(self.timePlayStop_pushButton, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.time_groupBox)
        self.video_groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.video_groupBox.setObjectName("video_groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.video_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frameIndex_label = QtGui.QLabel(self.video_groupBox)
        self.frameIndex_label.setObjectName("frameIndex_label")
        self.gridLayout_2.addWidget(self.frameIndex_label, 0, 0, 1, 1)
        self.framesPerSecond_spinBox = QtGui.QSpinBox(self.video_groupBox)
        self.framesPerSecond_spinBox.setMinimum(1)
        self.framesPerSecond_spinBox.setProperty("value", 25)
        self.framesPerSecond_spinBox.setObjectName("framesPerSecond_spinBox")
        self.gridLayout_2.addWidget(self.framesPerSecond_spinBox, 1, 1, 1, 1)
        self.framesPerSecond_label = QtGui.QLabel(self.video_groupBox)
        self.framesPerSecond_label.setObjectName("framesPerSecond_label")
        self.gridLayout_2.addWidget(self.framesPerSecond_label, 1, 0, 1, 1)
        self.frameIndex_spinBox = QtGui.QSpinBox(self.video_groupBox)
        self.frameIndex_spinBox.setMinimum(1)
        self.frameIndex_spinBox.setMaximum(10000)
        self.frameIndex_spinBox.setObjectName("frameIndex_spinBox")
        self.gridLayout_2.addWidget(self.frameIndex_spinBox, 0, 1, 1, 1)
        self.numFrames_frame = QtGui.QFrame(self.video_groupBox)
        self.numFrames_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.numFrames_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.numFrames_frame.setObjectName("numFrames_frame")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.numFrames_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.numFrames_label = QtGui.QLabel(self.numFrames_frame)
        self.numFrames_label.setObjectName("numFrames_label")
        self.horizontalLayout_4.addWidget(self.numFrames_label)
        self.numFramesValue_label = QtGui.QLabel(self.numFrames_frame)
        self.numFramesValue_label.setObjectName("numFramesValue_label")
        self.horizontalLayout_4.addWidget(self.numFramesValue_label)
        self.gridLayout_2.addWidget(self.numFrames_frame, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.video_groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.blackfynn_groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.blackfynn_groupBox.setObjectName("blackfynn_groupBox")
        self.gridLayout_5 = QtGui.QGridLayout(self.blackfynn_groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.blackfynnProfiles_groupBox = QtGui.QGroupBox(self.blackfynn_groupBox)
        self.blackfynnProfiles_groupBox.setObjectName("blackfynnProfiles_groupBox")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.blackfynnProfiles_groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.profiles_comboBox = QtGui.QComboBox(self.blackfynnProfiles_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profiles_comboBox.sizePolicy().hasHeightForWidth())
        self.profiles_comboBox.setSizePolicy(sizePolicy)
        self.profiles_comboBox.setObjectName("profiles_comboBox")
        self.horizontalLayout_5.addWidget(self.profiles_comboBox)
        self.addProfile_pushButton = QtGui.QPushButton(self.blackfynnProfiles_groupBox)
        self.addProfile_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/meshgeneratorstep/images/plus-icon-green-th.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addProfile_pushButton.setIcon(icon)
        self.addProfile_pushButton.setObjectName("addProfile_pushButton")
        self.horizontalLayout_5.addWidget(self.addProfile_pushButton)
        self.gridLayout_5.addWidget(self.blackfynnProfiles_groupBox, 0, 0, 1, 3)
        self.blackfynnDatasets_pushButton = QtGui.QPushButton(self.blackfynn_groupBox)
        self.blackfynnDatasets_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/meshgeneratorstep/images/download-icon-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blackfynnDatasets_pushButton.setIcon(icon1)
        self.blackfynnDatasets_pushButton.setObjectName("blackfynnDatasets_pushButton")
        self.gridLayout_5.addWidget(self.blackfynnDatasets_pushButton, 1, 2, 1, 1)
        self.blackfynnDatasets_label = QtGui.QLabel(self.blackfynn_groupBox)
        self.blackfynnDatasets_label.setObjectName("blackfynnDatasets_label")
        self.gridLayout_5.addWidget(self.blackfynnDatasets_label, 1, 0, 1, 1)
        self.displayEEGAnimation_checkBox = QtGui.QCheckBox(self.blackfynn_groupBox)
        self.displayEEGAnimation_checkBox.setObjectName("displayEEGAnimation_checkBox")
        self.gridLayout_5.addWidget(self.displayEEGAnimation_checkBox, 6, 0, 1, 1)
        self.blackfynnTimeSeries_comboBox = QtGui.QComboBox(self.blackfynn_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blackfynnTimeSeries_comboBox.sizePolicy().hasHeightForWidth())
        self.blackfynnTimeSeries_comboBox.setSizePolicy(sizePolicy)
        self.blackfynnTimeSeries_comboBox.setObjectName("blackfynnTimeSeries_comboBox")
        self.gridLayout_5.addWidget(self.blackfynnTimeSeries_comboBox, 4, 1, 1, 1)
        self.blackfynnDatasets_comboBox = QtGui.QComboBox(self.blackfynn_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blackfynnDatasets_comboBox.sizePolicy().hasHeightForWidth())
        self.blackfynnDatasets_comboBox.setSizePolicy(sizePolicy)
        self.blackfynnDatasets_comboBox.setObjectName("blackfynnDatasets_comboBox")
        self.gridLayout_5.addWidget(self.blackfynnDatasets_comboBox, 1, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.blackfynn_groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 6, 1, 1, 1)
        self.blackfynnTimeSeries_pushButton = QtGui.QPushButton(self.blackfynn_groupBox)
        self.blackfynnTimeSeries_pushButton.setText("")
        self.blackfynnTimeSeries_pushButton.setIcon(icon1)
        self.blackfynnTimeSeries_pushButton.setObjectName("blackfynnTimeSeries_pushButton")
        self.gridLayout_5.addWidget(self.blackfynnTimeSeries_pushButton, 4, 2, 1, 1)
        self.blackfynnTimeSeries_label = QtGui.QLabel(self.blackfynn_groupBox)
        self.blackfynnTimeSeries_label.setObjectName("blackfynnTimeSeries_label")
        self.gridLayout_5.addWidget(self.blackfynnTimeSeries_label, 4, 0, 1, 1)
        self.downloadData_button = QtGui.QPushButton(self.blackfynn_groupBox)
        self.downloadData_button.setObjectName("downloadData_button")
        self.gridLayout_5.addWidget(self.downloadData_button, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.blackfynn_groupBox)
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.viewAll_button = QtGui.QPushButton(self.frame)
        self.viewAll_button.setObjectName("viewAll_button")
        self.horizontalLayout_2.addWidget(self.viewAll_button)
        self.done_button = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.done_button.sizePolicy().hasHeightForWidth())
        self.done_button.setSizePolicy(sizePolicy)
        self.done_button.setObjectName("done_button")
        self.horizontalLayout_2.addWidget(self.done_button)
        self.verticalLayout.addWidget(self.frame)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.gridLayout_3.addWidget(self.dockWidget, 0, 0, 1, 1)
        self.sceneviewer_widget = AlignmentSceneviewerWidget(MeshGeneratorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewer_widget.sizePolicy().hasHeightForWidth())
        self.sceneviewer_widget.setSizePolicy(sizePolicy)
        self.sceneviewer_widget.setObjectName("sceneviewer_widget")
        self.gridLayout_3.addWidget(self.sceneviewer_widget, 0, 1, 1, 1)

        self.retranslateUi(MeshGeneratorWidget)
        QtCore.QMetaObject.connectSlotsByName(MeshGeneratorWidget)

    def retranslateUi(self, MeshGeneratorWidget):
        MeshGeneratorWidget.setWindowTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Mesh Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Control Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.time_groupBox.setTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLoop_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Loop", None, QtGui.QApplication.UnicodeUTF8))
        self.timeValue_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Time value:", None, QtGui.QApplication.UnicodeUTF8))
        self.timePlayStop_pushButton.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.video_groupBox.setTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Video:", None, QtGui.QApplication.UnicodeUTF8))
        self.frameIndex_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Frame index:", None, QtGui.QApplication.UnicodeUTF8))
        self.framesPerSecond_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Frames per second:", None, QtGui.QApplication.UnicodeUTF8))
        self.numFrames_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "# frames:", None, QtGui.QApplication.UnicodeUTF8))
        self.numFramesValue_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.blackfynn_groupBox.setTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Blackfynn:", None, QtGui.QApplication.UnicodeUTF8))
        self.blackfynnProfiles_groupBox.setTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Profiles:", None, QtGui.QApplication.UnicodeUTF8))
        self.addProfile_pushButton.setToolTip(QtGui.QApplication.translate("MeshGeneratorWidget", "Add profile", None, QtGui.QApplication.UnicodeUTF8))
        self.blackfynnDatasets_pushButton.setToolTip(QtGui.QApplication.translate("MeshGeneratorWidget", "Retrieve datasets", None, QtGui.QApplication.UnicodeUTF8))
        self.blackfynnDatasets_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Datasets:", None, QtGui.QApplication.UnicodeUTF8))
        self.displayEEGAnimation_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Show EEG data in animation", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Export for WebGL", None, QtGui.QApplication.UnicodeUTF8))
        self.blackfynnTimeSeries_pushButton.setToolTip(QtGui.QApplication.translate("MeshGeneratorWidget", "Retrieve time series", None, QtGui.QApplication.UnicodeUTF8))
        self.blackfynnTimeSeries_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Time series:", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadData_button.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Download Data", None, QtGui.QApplication.UnicodeUTF8))
        self.viewAll_button.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "View All", None, QtGui.QApplication.UnicodeUTF8))
        self.done_button.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Done", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.zincwidgets.alignmentsceneviewerwidget import AlignmentSceneviewerWidget