#MIC IMPORTS
import matplotlib.pyplot as plt
from datetime import datetime, timezone
from typing import Optional
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#PYQT5 IMPORTS
from PyQt5.QtWidgets import  QVBoxLayout, QWidget
from PyQt5.QtCore import QSize, QCoreApplication, Qt, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSplitter, QLabel, QFrame, QTableWidget, QTableWidgetItem
#HANDLER IMPORTS
from Handlers.dbHandle import importPastAlertsCount, getPacketCounter


class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if Dashboard.objectName():
            Dashboard.setObjectName(u"Intruwatch Dashboard")
        Dashboard.resize(1600, 900)
        Dashboard.setFixedSize(QSize(1600, 900))
        Dashboard.setAutoFillBackground(False)
        Dashboard.setStyleSheet(u"color:rgb(0,0,0);")
        Dashboard.setAnimated(True)
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1450, 810, 131, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border: 2px outset black;\n"
"background:blue;\n"
"color: white;\n"
"font: bold 14pt;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px outset black;\n"
"background:white;\n"
"color: black;\n"
"font: bold 14pt;\n"
"}")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(1420, 10, 171, 181))
        self.splitter.setOrientation(Qt.Vertical)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"border: 2px outset black;\n"
"background:blue;\n"
"color: white;\n"
"font: bold 8pt;\n"
"border-radius: 20px;\n"
"}\n"
"")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_2)
        self.label_4 = QLabel(self.splitter)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(12)
        self.label_4.setFont(font2)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setFrameShadow(QFrame.Sunken)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_4)
        self.label_3 = QLabel(self.splitter)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel{\n"
"border: 2px outset black;\n"
"background:blue;\n"
"color: white;\n"
"font: bold 8pt;\n"
"border-radius: 20px;\n"
"}\n"
"")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_3)
        self.label_5 = QLabel(self.splitter)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setFont(font2)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setFrameShadow(QFrame.Sunken)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_5)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 570, 1391, 311))
        self.tableWidget.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: rgb(0, 0, 0)")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(347)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(10, 21, 1391, 62))
        font3 = QFont()
        font3.setPointSize(36)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel{\n"
"border: 2px outset black;\n"
"background:blue;\n"
"color: white;\n"
"font: bold 36pt;\n"
"border-radius: 20px;\n"
"}\n"
"")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setAlignment(Qt.AlignCenter)
        Dashboard.setCentralWidget(self.centralwidget)
        self.retranslateUi(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"Intruwatch Dash", None))
        self.pushButton.setText(QCoreApplication.translate("Dashboard", u"Advanced", None))
        self.label_2.setText(QCoreApplication.translate("Dashboard", u"Past Threats", None))
        self.label_4.setText(QCoreApplication.translate("Dashboard", str(importPastAlertsCount()), None))
        self.label_3.setText(QCoreApplication.translate("Dashboard", u"Current Threats Detected", None))
        self.label_5.setText(QCoreApplication.translate("Dashboard", u"TDCounter", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dashboard", u"Time", None)); # 
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dashboard", u"Source IP", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dashboard", u"Source Port", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dashboard", u"Packet Type", None));
        self.label.setText(QCoreApplication.translate("Dashboard", u"Intruwatch Dashboard", None))
        
        
    def update_past_alerts_count(self, count):
        self.label_4.setText(QCoreApplication.translate("Dashboard", str(count), None))
    def update_current_alerts_count(self, count):
        self.label_5.setText(QCoreApplication.translate("Dashboard", str(count), None))
    # retranslateUi
###################################################################################################################################

class RealTimeGraph(QWidget):
    def __init__(self, packet_graph: Optional[str] = None, histo_tick_size: int = 200):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.fig, self.ax = plt.subplots()
        self.ax.set_title(packet_graph)
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Amount of Packets")
        self.ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: datetime.fromtimestamp(x, timezone.utc).strftime('%H:%M:%S')))
        self.TCP_dataset, = self.ax.plot([], [], label="TCP")
        self.UDP_dataset, = self.ax.plot([], [], label="UDP")
        self.ICMP_dataset, = self.ax.plot([], [], label="ICMP")
        self.ax.legend()
        self.TCP_data = []
        self.UDP_data = []
        self.ICMP_data = []
        self.dates = []
        self.animation = FuncAnimation(self.fig, self.update, interval=1000, cache_frame_data=False)

        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        
    def update(self, frame):
        current_time = datetime.now().timestamp()
        two_seconds_ago = current_time - 10
        
        # Filter out data points older than two seconds
        filtered_indices = [i for i, date in enumerate(self.dates) if date >= two_seconds_ago]
        self.dates = [self.dates[i] for i in filtered_indices]
        self.TCP_data = [self.TCP_data[i] for i in filtered_indices]
        self.UDP_data = [self.UDP_data[i] for i in filtered_indices]
        self.ICMP_data = [self.ICMP_data[i] for i in filtered_indices]
        
        top=0
        
        # Fetch packet counts for TCP, UDP, and ICMP
        tcp_count = int(getPacketCounter("TCP") or 0)
        udp_count = int(getPacketCounter("UDP") or 0)
        icmp_count = int(getPacketCounter("ICMP") or 0)
        
        if tcp_count > top:
            top = .5 * tcp_count
        elif udp_count > top:
            top = .5 * udp_count
        elif icmp_count > top:
            top = .5 * icmp_count
        else:
            top = top
        
        # Append counts to data lists
        self.TCP_data.append(tcp_count)
        self.UDP_data.append(udp_count)
        self.ICMP_data.append(icmp_count)
        
        # Append current time
        self.dates.append(current_time)

        # Update dataset with new data
        self.TCP_dataset.set_data(self.dates, self.TCP_data)
        self.UDP_dataset.set_data(self.dates, self.UDP_data)
        self.ICMP_dataset.set_data(self.dates, self.ICMP_data)
        
        # Set Y-axis limits dynamically based on the maximum values of the data
        max_tcp = max(self.TCP_data, default=0)
        max_udp = max(self.UDP_data, default=0)
        max_icmp = max(self.ICMP_data, default=0)
        max_value = max(max_tcp, max_udp, max_icmp)
        
        # Add buffer space (0.5) to the top and bottom
        buffer_space = top
        min_y = min(0, max_value - buffer_space)
        max_y = max_value + buffer_space
        
        # Set y-axis limits with buffer space
        self.ax.set_ylim(min_y, max_y)

        # Redraw the graph
        self.ax.relim()
        self.ax.autoscale_view(True, True, True)