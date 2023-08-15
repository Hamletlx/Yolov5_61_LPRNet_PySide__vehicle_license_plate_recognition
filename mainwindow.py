import os
import glob
import sys
import datetime
import cv2
import csv
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QCoreApplication
from mainwindow_ui import Ui_MainWindow
from qt_material import apply_stylesheet

from detect_yolov5 import *
from detect_lprnet import *


def check_license_plate_numberWithClassS(plate_numberWithClassS):
    for plate_numberWithClass in plate_numberWithClassS:
        plate_number = plate_numberWithClass[0]
        if not check_license_plate(plate_number):
            plate_numberWithClassS.remove(plate_numberWithClass)
    return plate_numberWithClassS


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.yolov5model = attempt_load('weights/yolov5_best.pt', map_location=self.device)
        self.lprnetmodel = build_lprnet(lpr_max_len=8, phase=False, class_num=len(CHARS), dropout_rate=0.0)
        self.lprnetmodel.to(self.device)
        self.lprnetmodel.load_state_dict(torch.load("weights/Final_LPRNet_model.pth"))
        img = np.zeros((640, 640, 3), dtype=np.uint8)
        detect_yolov5(img, self.yolov5model, self.device)

        self.filePath = ''
        self.source_img = None
        self.location_img = None
        self.number_imgs = []
        self.class_numbers_imgs = []
        self.number_strs = []
        self.table_widget_items = []

        self.camera_flag = False

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        apply_stylesheet(self.ui.menubar, theme='light_cyan.xml')

        self.ui.tableWidget.setColumnWidth(0, 845)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 120)
        self.ui.tableWidget.setColumnWidth(3, 80)

        self.ui.select.triggered.connect(self.select_triggered)
        self.ui.location.triggered.connect(self.location_triggered)
        self.ui.number.triggered.connect(self.number_triggered)

        self.ui.selects.triggered.connect(self.selects_triggered)

        self.ui.select_video.triggered.connect(self.select_video_triggered)

        self.ui.select_camera.triggered.connect(self.select_camera_triggered)
        self.ui.close_camera.triggered.connect(self.close_camera_triggered)

        self.ui.repetition.triggered.connect(self.repetition_triggered)
        self.ui.output.triggered.connect(self.output_triggered)
        self.ui.clear.triggered.connect(self.clear_triggered)

        self.ui.information.triggered.connect(self.information_triggered)


    def select_triggered(self):
        self.filePath, _ = QFileDialog.getOpenFileName(self, '请选择一个图片','', '图片 (*.jpg *.jpeg *.png)')
        if self.filePath == '':
            return
        image = cv2.imdecode(np.fromfile(self.filePath, dtype=np.uint8), 1)

        image_height, image_width, _ = image.shape
        side_length = min(image_height, image_width)
        if side_length < 160:
            QMessageBox.information(self, '提示', '图片分辨率太小, 不足以进行预测')
        else:
            x1, y1 = (image_width - side_length) // 2, (image_height - side_length) // 2
            x2, y2 = x1 + side_length, y1 + side_length
            self.source_img = image[y1:y2, x1:x2]
            self.show_source()


    def location_triggered(self):
        if self.source_img is None:
            QMessageBox.information(self, '提示', '请先选择图片')
        else:
            self.location_img, self.number_imgs, self.class_numbers_imgs = detect_yolov5(self.source_img, self.yolov5model, self.device)
            self.show_division()


    def number_triggered(self):
        if self.source_img is None:
            QMessageBox.information(self, '提示', '请先选择图片')
        elif self.location_img is None:
            QMessageBox.information(self, '提示', '请先定位车牌')
        elif self.number_imgs == []:
            QMessageBox.information(self, '提示', '未检测到车牌')
        else:
            self.number_strs = detect_lprnet(self.number_imgs, self.lprnetmodel, self.device)
            datas = [[self.number_strs[i], self.class_numbers_imgs[i]] for i in range(len(self.number_strs))]
            datas = check_license_plate_numberWithClassS(datas)
            if self.number_strs == []:
                QMessageBox.information(self, '提示', '车牌识别失败')
            else:
                now_time=datetime.datetime.now()
                now_time=now_time.strftime('%Y-%m-%d %H:%M:%S')
                for data in datas:                
                    table_widget_item = [self.filePath, now_time, data[0], data[1]]
                    self.table_widget_items.append(table_widget_item)
                self.show_number()
    

    def selects_triggered(self):
        filedir = QFileDialog.getExistingDirectory(self, '请选择一个文件夹')
        if filedir == '':
            return
        filePaths = glob.glob(os.path.join(filedir, '*.jpg'))+glob.glob(os.path.join(filedir, '*.jpeg'))+glob.glob(os.path.join(filedir, '*.png'))
        for filePath in filePaths:
            self.filePath = filePath.replace('\\', '/')
            image = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), 1)
            image_height, image_width, _ = image.shape
            side_length = min(image_height, image_width)
            if side_length < 160:
                self.ui.source.setStyleSheet("color: #FF0000;")
                self.ui.source.setText('图片分辨率太小, 不足以进行预测')
            else:
                x1, y1 = (image_width - side_length) // 2, (image_height - side_length) // 2
                x2, y2 = x1 + side_length, y1 + side_length
                self.source_img = image[y1:y2, x1:x2]
                self.show_source()
                QCoreApplication.processEvents()

                self.location_img, self.number_imgs, self.class_numbers_imgs = detect_yolov5(self.source_img, self.yolov5model, self.device)
                self.show_division()
                QCoreApplication.processEvents()

                if self.number_imgs is not []:
                    self.number_strs = detect_lprnet(self.number_imgs, self.lprnetmodel, self.device)
                    datas = [[self.number_strs[i], self.class_numbers_imgs[i]] for i in range(len(self.number_strs))]
                    datas = check_license_plate_numberWithClassS(datas)
                    now_time=datetime.datetime.now()
                    now_time=now_time.strftime('%Y-%m-%d %H:%M:%S')
                    for data in datas:                
                        table_widget_item = [self.filePath, now_time, data[0], data[1]]
                        self.table_widget_items.append(table_widget_item)
                    self.show_number()
                    QCoreApplication.processEvents()


    def select_video_triggered(self):
        videoFilePath, _ = QFileDialog.getOpenFileName(self, '请选择一个视频','', '*.mp4')
        if videoFilePath == '':
            return
        cap = cv2.VideoCapture(videoFilePath)

        image_width, image_height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        side_length = min(image_height, image_width)
        if side_length < 160:
            self.ui.source.setStyleSheet("color: #FF0000;")
            self.ui.source.setText('视频分辨率太小, 不足以进行预测')
        else:
            x1, y1 = (image_width - side_length) // 2, (image_height - side_length) // 2
            x2, y2 = x1 + side_length, y1 + side_length
            frame_index = 1
            while True:
                ret, frame = cap.read()
                if ret:
                    self.filePath = 'video: ' + videoFilePath + ' ' + str(frame_index)
                    frame_index += 1
                    self.source_img = frame[y1:y2, x1:x2]
                    self.show_source()
                    QCoreApplication.processEvents()

                    self.location_img, self.number_imgs, self.class_numbers_imgs = detect_yolov5(self.source_img, self.yolov5model, self.device)
                    self.show_division()
                    QCoreApplication.processEvents()

                    if self.number_imgs is not []:
                        self.number_strs = detect_lprnet(self.number_imgs, self.lprnetmodel, self.device)
                        datas = [[self.number_strs[i], self.class_numbers_imgs[i]] for i in range(len(self.number_strs))]
                        datas = check_license_plate_numberWithClassS(datas)
                        now_time=datetime.datetime.now()
                        now_time=now_time.strftime('%Y-%m-%d %H:%M:%S')
                        for data in datas:                
                            table_widget_item = [self.filePath, now_time, data[0], data[1]]
                            self.table_widget_items.append(table_widget_item)
                        self.show_number()
                        QCoreApplication.processEvents()
                else:
                    break

    def select_camera_triggered(self):
        self.camera_flag = True
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                now_time=datetime.datetime.now()
                now_time=now_time.strftime('%Y-%m-%d %H:%M:%S')
                self.filePath = 'camera: ' + now_time
                image_height, image_width, _ = frame.shape
                side_length = min(image_height, image_width)
                x1, y1 = (image_width - side_length) // 2, (image_height - side_length) // 2
                x2, y2 = x1 + side_length, y1 + side_length
                self.source_img = frame[y1:y2, x1:x2]
                self.show_source()
                QCoreApplication.processEvents()

                self.location_img, self.number_imgs, self.class_numbers_imgs = detect_yolov5(self.source_img, self.yolov5model, self.device)
                self.show_division()
                QCoreApplication.processEvents()

                if self.number_imgs is not []:
                    self.number_strs = detect_lprnet(self.number_imgs, self.lprnetmodel, self.device)
                    datas = [[self.number_strs[i], self.class_numbers_imgs[i]] for i in range(len(self.number_strs))]
                    datas = check_license_plate_numberWithClassS(datas)
                    now_time=datetime.datetime.now()
                    now_time=now_time.strftime('%Y-%m-%d %H:%M:%S')
                    for data in datas:                
                        table_widget_item = [self.filePath, now_time, data[0], data[1]]
                        self.table_widget_items.append(table_widget_item)
                    self.show_number()
                    QCoreApplication.processEvents()
            else:
                break
            if self.camera_flag == False:
                break
        cap.release()


    def close_camera_triggered(self):
        self.camera_flag = False


    def repetition_triggered(self):
        items_str = [(row[0],row[2]) for row in self.table_widget_items]
        diff_items_str = []
        for i in range(len(items_str)-1,-1,-1):
            if items_str[i] in diff_items_str:
                self.table_widget_items.pop(i)
            else:
                diff_items_str.append(items_str[i])
        self.show_number()


    def output_triggered(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '请选择一个csv文件','', '*.csv')
        with open(filePath, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in range(self.ui.tableWidget.rowCount()):
                row_data = []
                for column in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")
                writer.writerow(row_data)
        file.close()
        QMessageBox.information(self, '提示', '保存成功')
    

    def clear_triggered(self):
        self.filePath = ''
        self.source_img = None
        self.location_img = None
        self.number_imgs = []
        self.class_numbers_imgs = []
        self.number_strs = []
        self.table_widget_items = []
        self.show_source(clear=True)
        self.show_division(clear=True)
        self.show_number()

    
    def information_triggered(self):
        QMessageBox.information(self, '信息', '作者: hamlet\n联系方式: hamletlx07@gmail.com\n版本: 3.0')            


    def show_source(self, clear = False):
        self.ui.source.clear()
        if self.source_img is None:
            if clear:
                self.ui.source.setStyleSheet("color: #CBCBCB;")
                self.ui.source.setText('SOURCE_IMAGE')
            else:
                self.ui.source.setStyleSheet("color: #FF0000;")
                self.ui.source.setText('图片显示失败')
        else:
            img = self.source_img.copy()
            img = cv2.resize(img, (self.ui.source.width(), self.ui.source.height()))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            qimg = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
            self.ui.source.setPixmap(QPixmap.fromImage(qimg))


    def show_division(self, clear = False):
        self.ui.division.clear()
        if(self.location_img is None):
            if clear:
                self.ui.division.setStyleSheet("color: #CBCBCB;")
                self.ui.division.setText('DIVISION_IMAGE')
            else:
                self.ui.division.setStyleSheet("color: #FF0000;")
                self.ui.division.setText('图片显示失败')
        else:
            img = self.location_img.copy()
            img = cv2.resize(img, (self.ui.division.width(), self.ui.division.height()))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            qimg = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
            self.ui.division.setPixmap(QPixmap.fromImage(qimg))


    def show_number(self):
        while self.ui.tableWidget.rowCount() > 0:
            self.ui.tableWidget.removeRow(0)
        for idex, item in enumerate(self.table_widget_items):
            self.ui.tableWidget.insertRow(idex)
            for i in range(len(item)):
                self.ui.tableWidget.setItem(idex, i, QTableWidgetItem(item[i]))
        self.ui.tableWidget.scrollToBottom()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QMessageBox QPushButton[text = 'OK']{qproperty-text: '好的';}")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
