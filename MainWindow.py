from UIMainWindowForm import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from Origin import Origin


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNew_Origin.triggered.connect(self.new_origin)
        self.ui.actionOpen_Origin.triggered.connect(self.open_origin)
        self.ui.actionSave_Origin.triggered.connect(self.save_origin)
        self.ui.actionSave_As_Origin.triggered.connect(self.save_as_origin)

        self.ui.actionQuit.triggered.connect(self.quit)

        self.origin2form()
        self.ui.numberOfLines.setText('1')
        self.ui.numberOfPoints.setText('1')

        self.origin_file = None

    def origin2form(self, origin=None):
        if origin is None:
            origin = Origin()

        self.ui.lineNumber.setText(str(origin.line_number))
        self.ui.pointNumber.setText(str(origin.point_number))
        self.ui.lineInterval.setText(str(origin.line_interval))
        self.ui.pointInterval.setText(str(origin.point_interval))
        self.ui.lineDistance.setText(str(origin.line_distance))
        self.ui.pointDistance.setText(str(origin.point_distance))
        self.ui.easting.setText(str(origin.easting))
        self.ui.northing.setText(str(origin.northing))
        self.ui.lineAzimuth.setText(str(origin.line_azimuth))

    def form2origin(self):
        origin = Origin()
        origin.line_number = float(self.ui.lineNumber.text())
        origin.point_number = float(self.ui.pointNumber.text())
        origin.line_interval = float(self.ui.lineInterval.text())
        origin.point_interval = float(self.ui.pointInterval.text())
        origin.line_distance = float(self.ui.lineDistance.text())
        origin.point_distance = float(self.ui.pointDistance.text())
        origin.easting = float(self.ui.easting.text())
        origin.northing = float(self.ui.northing.text())
        origin.line_azimuth = float(self.ui.lineAzimuth.text())
        return origin

    def new_origin(self):
        self.origin_file = None
        o = Origin()
        self.origin2form(o)

    def open_origin(self):
        previous_origin_file = self.origin_file

        self.origin_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "Origin (*.origin );;All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not self.origin_file:
            self.origin_file = previous_origin_file
            return

        self.read_origin_from_file()

    def save_origin(self):
        if not self.origin_file:
            self.save_as_origin()
            return
        self.save_origin_to_file(self.origin_file)

    def save_as_origin(self):
        origin_file, _ = QFileDialog.getSaveFileName(
            self,
            "Save as file",
            "",
            "Origin (*.origin );;All files (*.*)",
            # options=QFileDialog.DontUseNativeDialog
        )

        if not origin_file:
            return

        self.origin_file = origin_file
        self.save_origin_to_file()

    def read_origin_from_file(self):
        fh = open(self.origin_file, 'r')
        od = eval(fh.read())
        o = Origin()
        o = o.deserialize(od)
        self.origin2form(o)
        fh.close()

    def save_origin_to_file(self, file=None):
        if not file:
            file = self.origin_file

        fh = open(file, 'w')
        o = self.form2origin()
        od = o.serialize()
        fh.write(str(od))
        fh.close()

    def quit(self):
        self.save_origin()
        self.close()
