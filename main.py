from __future__ import division
import string
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtGui import QPixmap, QIntValidator, QIcon
import sys
from PyQt5.QtWidgets import QFileDialog
import rgb
import gray
import ycbcr
import ycbcr422
from gui import Ui_YONGATEK

fileName = ""
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        #uic.loadUi("gui.ui", self)
        self.ui = Ui_YONGATEK()
        self.ui.setupUi(self)
        self.ui.open_image.clicked.connect(self.open_file_image)
        self.ui.open_image_2.clicked.connect(self.open_file_image_g)
        self.ui.open_image_ycbcr.clicked.connect(self.open_file_image_y)
        self.image_path = ""
        self.image_path_gray = ""
        self.image_path_ycbcr= ""
        self.ui.cvt_bn.clicked.connect(self.rgb_bin)
        self.ui.cvt_bn_2.clicked.connect(self.gray_bin)
        self.ui.cvt_hexa.clicked.connect(self.rgb_hexa)
        self.ui.cvt_hexa_2.clicked.connect(self.gray_hexa)
        self.ui.cvt_bn_coe.clicked.connect(self.rgb_bin_coe)
        self.ui.cvt_bn_coe_2.clicked.connect(self.gray_bin_coe)
        self.ui.cvt_hexa_coe.clicked.connect(self.rgb_hexa_coe)
        self.ui.cvt_hexa_coe_2.clicked.connect(self.gray_hexa_coe)
        self.ui.cvt_bn_mif.clicked.connect(self.rgb_bin_mif)
        self.ui.cvt_bn_mif_2.clicked.connect(self.gray_bin_mif)
        self.ui.cvt_hex_mif.clicked.connect(self.rgb_hexa_mif)
        self.ui.cvt_hex_mif_2.clicked.connect(self.gray_hexa_mif)
        self.ui.bin_zero_btn.clicked.connect(self.fill_zero_bin)
        self.ui.bin_zero_btn_2.clicked.connect(self.fill_zero_bin_gray)
        self.ui.bin_zero_btn_coe.clicked.connect(self.fill_zero_bin_coe)
        self.ui.bin_zero_btn_coe_2.clicked.connect(self.fill_zero_bin_gray_coe)
        self.ui.hex_zero_btn_coe.clicked.connect(self.fill_zero_hex_coe)
        self.ui.hex_zero_btn_coe_2.clicked.connect(self.fill_zero_hex_gray_coe)
        self.ui.hex_zero_btn.clicked.connect(self.fill_zero_hex)
        self.ui.hex_zero_btn_2.clicked.connect(self.fill_zero_hex_gray)
        self.ui.bin_zero_btn_mif.clicked.connect(self.fill_zero_bin_mif)
        self.ui.bin_zero_btn_mif_2.clicked.connect(self.fill_zero_bin_gray_mif)
        self.ui.hex_zero_btn_mif.clicked.connect(self.fill_zero_hex_mif)
        self.ui.hex_zero_btn_mif_2.clicked.connect(self.fill_zero_hex_gray_mif)
        self.ui.set_row.setValidator(QIntValidator(self))
        self.ui.set_row_2.setValidator(QIntValidator(self))
        self.ui.shw_btn.clicked.connect(self.shift_)
        self.ui.clr_btn.clicked.connect(self.clear)
        self.ui.shft_input.textChanged[str].connect(lambda: self.ui.shw_btn.setEnabled(self.ui.shft_input.text() != ""))
        self.ui.rgb_btn.clicked.connect(self.rgb_show)
        self.ui.shift_btn.clicked.connect(self.shift_show)
        self.ui.gray_btn.clicked.connect(self.gray_show)
        self.ui.YCbCr_btn.clicked.connect(self.ycbcr_show)
        self.ui.BIN2HEX_btn.clicked.connect(self.BIN2HEX_show)
        self.ui.DEC2BIN_btn.clicked.connect(self.DEC2BIN_show)
        self.ui.DEC2HEX_btn.clicked.connect(self.DEC2HEX_show)
        self.ui.BTN_BN2HEX.clicked.connect(self.bin2hex)
        self.ui.BTN_HEX2BN.clicked.connect(self.hex2bin)
        self.ui.BTN_DEC2BN.clicked.connect(self.dec2bin)
        self.ui.BTN_BN2DEC.clicked.connect(self.bin2dec)
        self.ui.BTN_DEC2HEX.clicked.connect(self.dec2hex)
        self.ui.BTN_HEX2DEC.clicked.connect(self.hex2dec)
        self.ui.cvt_bn_3.clicked.connect(self.ycbcr_bin)
        self.ui.cvt_bn_coe_3.clicked.connect(self.ycbcr_bin_coe)
        self.ui.cvt_bn_mif_3.clicked.connect(self.ycbcr_bin_mif)
        self.ui.cvt_hexa_3.clicked.connect(self.ycbcr_hex)
        self.ui.cvt_hexa_coe_3.clicked.connect(self.ycbcr_hex_coe)
        self.ui.cvt_hex_mif_3.clicked.connect(self.ycbcr_hex_mif)
        self.ui.bin_zero_btn_3.clicked.connect(self.fill_zero_bin_ycbcr)
        self.ui.hex_zero_btn_3.clicked.connect(self.fill_zero_hex_ycbcr)
        self.ui.bin_zero_btn_coe_3.clicked.connect(self.fill_zero_bin_ycbcr_coe)
        self.ui.hex_zero_btn_coe_3.clicked.connect(self.fill_zero_hex_ycbcr_coe)
        self.ui.bin_zero_btn_mif_3.clicked.connect(self.fill_zero_bin_ycbcr_mif)
        self.ui.hex_zero_btn_mif_3.clicked.connect(self.fill_zero_hex_ycbcr_mif)
        self.ui.cvt_bn_4.clicked.connect(self.ycbcr422_bin)
        self.ui.cvt_bn_coe_4.clicked.connect(self.ycbcr422_bin_coe)
        self.ui.cvt_bn_mif_4.clicked.connect(self.ycbcr422_bin_mif)
        self.ui.cvt_hexa_4.clicked.connect(self.ycbcr422_hex)
        self.ui.cvt_hexa_coe_4.clicked.connect(self.ycbcr422_hex_coe)
        self.ui.cvt_hex_mif_4.clicked.connect(self.ycbcr422_hex_mif)
        self.ui.bin_zero_btn_4.clicked.connect(self.fill_zero_bin_ycbcr422)
        self.ui.bin_zero_btn_coe_4.clicked.connect(self.fill_zero_bin_coe_ycbcr422)
        self.ui.bin_zero_btn_mif_4.clicked.connect(self.fill_zero_bin_mif422)
        self.ui.hex_zero_btn_4.clicked.connect(self.fill_zero_hex_ycbcr422)
        self.ui.hex_zero_btn_coe_4.clicked.connect(self.fill_zero_hexa_coe422)
        self.ui.hex_zero_btn_mif_4.clicked.connect(self.fill_zero_hexa_mif422)

    def bin2hex(self):
        bin_num = self.ui.lineEdit_BN_INPUT.text()
        p = set(bin_num)
        s = {'0', '1'}

        if s == p or p == {'0'} or p == {'1'} :
            bin_num = int(self.ui.lineEdit_BN_INPUT.text(), 2)
            hex_num = format(bin_num, 'x')
            self.ui.RES_HEX.setText(hex_num)
        else:
            QMessageBox.about(self, "ERROR", "Please enter the correct number!")

    def hex2bin(self):
        hex_num = self.ui.lineEdit_HEX_INPUT.text()

        if all(c in string.hexdigits for c in hex_num) == True :
            hex_num = int(self.ui.lineEdit_HEX_INPUT.text(), 16)
            bin_num = format(hex_num, 'b')
            self.ui.RES_BN.setText(bin_num)
        else:
            QMessageBox.about(self, "ERROR", "Please enter the correct number!")

    def dec2bin(self):
        num = self.ui.lineEdit_DEC_INPUT.text()

        if num.isdigit()== True:
            num = int(self.ui.lineEdit_DEC_INPUT.text())
            bin_num = format(num, 'b')
            self.ui.RES_BN_2.setText(bin_num)
        else:
            QMessageBox.about(self, "ERROR", "Please enter the correct number!")

    def bin2dec(self):
        bin_num = self.ui.lineEdit_BN_INPUT_2.text()
        p = set(bin_num)
        s = {'0', '1'}
        if s == p or p == {'0'} or p == {'1'}:
            bin_num = int(self.ui.lineEdit_BN_INPUT_2.text(), 2)
            dec_num = format(bin_num, 'd')
            self.ui.RES_DEC.setText(dec_num)
        else:
            QMessageBox.about(self, "ERROR", "Please enter the correct number!")


    def dec2hex(self):
        num = self.ui.lineEdit_DEC_INPUT_3.text()

        if num.isdigit()== True:
            num = int(self.ui.lineEdit_DEC_INPUT_3.text())
            hex_num = format(num, 'x')
            self.ui.RES_HEX_2.setText(hex_num)
        else:
            QMessageBox.about(self, "ERROR", "Please enter the correct number!")

    def hex2dec(self):
        hex_num = self.ui.lineEdit_HEX_INPUT_3.text()

        if all(c in string.hexdigits for c in hex_num) == True :
            hex_num = int(self.ui.lineEdit_HEX_INPUT_3.text(), 16)
            num = format(hex_num, 'd')
            self.ui.RES_DEC_2.setText(num)
        else:
            QMessageBox.about(self, "ERROR", "Please enter the correct number!")


    def rgb_show(self):
        self.ui.function.setCurrentWidget(self.ui.tab1)

    def shift_show(self):
        self.ui.function.setCurrentWidget(self.ui.tab2)
    def gray_show(self):
        self.ui.function.setCurrentWidget(self.ui.tab3)

    def ycbcr_show(self):
        self.ui.function.setCurrentWidget(self.ui.tab4)
    def BIN2HEX_show(self):
        self.ui.function.setCurrentWidget(self.ui.tab5)
    def DEC2BIN_show(self):
        self.ui.function.setCurrentWidget(self.ui.tab6)
    def DEC2HEX_show(self):
        self.ui.function.setCurrentWidget(self.ui.tab7)

    def open_file_image_y(self):
        self.openFileNameDialog_y()
        self.show()

    def openFileNameDialog_y(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Image Files (*.png);;Image Files (*.jpg)",
                                                  options=options)
        self.image_path_ycbcr = fileName
        img = QtGui.QImage(QtGui.QImageReader(fileName).read())

        resizeimg = img.scaled(661, 531)
        self.ui.lbl_img_8.setPixmap(QtGui.QPixmap(resizeimg))

    def open_file_image_g(self):
        self.openFileNameDialog_g()
        self.show()

    def openFileNameDialog_g(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Image Files (*.png);;Image Files (*.jpg)",
                                                  options=options)
        self.image_path_gray = fileName
        img = QtGui.QImage(QtGui.QImageReader(fileName).read())

        resizeimg = img.scaled(661, 531)
        self.ui.lbl_img_3.setPixmap(QtGui.QPixmap(resizeimg))


    def clear(self):
        self.ui.textedit.clear()

    def open_file_image(self):
        self.openFileNameDialog()
        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Image Files (*.png);;Image Files (*.jpg)",
                                                  options=options)
        self.image_path = fileName
        img = QtGui.QImage(QtGui.QImageReader(fileName).read())

        resizeimg = img.scaled(661, 531)
        self.ui.lbl_img.setPixmap(QtGui.QPixmap(resizeimg))



    def rgb_bin(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        else:
            rbitVal= int(self.ui.r_line.text())
            gbitVal= int(self.ui.g_line.text())
            bbitVal= int(self.ui.b_line.text())
            rgb.get_rgb_binary(self.image_path, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Converted Binary.dat")

    def rgb_bin_coe(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        else:
            rbitVal= int(self.ui.r_line.text())
            gbitVal= int(self.ui.g_line.text())
            bbitVal= int(self.ui.b_line.text())
            rgb.get_rgb_binary_coe(self.image_path, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Converted Binary.coe")
    def rgb_bin_mif(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        else:
            rbitVal= int(self.ui.r_line.text())
            gbitVal= int(self.ui.g_line.text())
            bbitVal= int(self.ui.b_line.text())
            rgb.get_rgb_binary_mif(self.image_path, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Converted Binary.mif")

    def rgb_hexa(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        else:
            rbitVal = int(self.ui.r_line.text())
            gbitVal = int(self.ui.g_line.text())
            bbitVal = int(self.ui.b_line.text())
            rgb.get_rgb_hex(self.image_path, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Converted Hexadecimal.dat")

    def rgb_hexa_coe(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        else:
            rbitVal = int(self.ui.r_line.text())
            gbitVal = int(self.ui.g_line.text())
            bbitVal = int(self.ui.b_line.text())
            rgb.get_rgb_hex_coe(self.image_path, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Converted Hexadecimal.coe")

    def rgb_hexa_mif(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        else:
            rbitVal = int(self.ui.r_line.text())
            gbitVal = int(self.ui.g_line.text())
            bbitVal = int(self.ui.b_line.text())
            rgb.get_rgb_hex_mif(self.image_path, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Converted Hexadecimal.mif")

    def fill_zero_bin(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        elif self.ui.set_row.text() == "":
            self.ui.lbl_res.setText("Please enter the row values!")
        else:
            rbitVal= int(self.ui.r_line.text())
            gbitVal= int(self.ui.g_line.text())
            bbitVal= int(self.ui.b_line.text())
            rw_value= int(self.ui.set_row.text())
            rgb.get_zero_bin(self.image_path, rw_value, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Filled With Zero bin.dat")

    def fill_zero_bin_coe(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        elif self.ui.set_row.text() == "":
            self.ui.lbl_res.setText("Please enter the row values!")
        else:
            rbitVal= int(self.ui.r_line.text())
            gbitVal= int(self.ui.g_line.text())
            bbitVal= int(self.ui.b_line.text())
            rw_value= int(self.ui.set_row.text())
            rgb.get_zero_bin_coe(self.image_path, rw_value, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Filled With Zero bin.coe")

    def fill_zero_bin_mif(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        elif self.ui.set_row.text() == "":
            self.ui.lbl_res.setText("Please enter the row values!")
        else:
            rbitVal= int(self.ui.r_line.text())
            gbitVal= int(self.ui.g_line.text())
            bbitVal= int(self.ui.b_line.text())
            rw_value= int(self.ui.set_row.text())
            rgb.get_zero_bin_mif(self.image_path, rw_value, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Filled With Zero bin.mif")
    def fill_zero_hex(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        elif self.ui.set_row.text() == "":
            self.ui.lbl_res.setText("Please enter the row values!")
        else:
            rbitVal = int(self.ui.r_line.text())
            gbitVal = int(self.ui.g_line.text())
            bbitVal = int(self.ui.b_line.text())
            rw_value= int(self.ui.set_row.text())
            rgb.get_zero_hexa(self.image_path, rw_value,rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Filled With Zero hex.dat")

    def fill_zero_hex_coe(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        elif self.ui.set_row.text() == "":
            self.ui.lbl_res.setText("Please enter the row values!")
        else:
            rbitVal = int(self.ui.r_line.text())
            gbitVal = int(self.ui.g_line.text())
            bbitVal = int(self.ui.b_line.text())
            rw_value= int(self.ui.set_row.text())
            rgb.get_zero_hexa_coe(self.image_path, rw_value, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Filled With Zero hex.coe")

    def fill_zero_hex_mif(self):
        if self.image_path == "":
            self.ui.lbl_res.setText("!!!!!Image is not loading!!!!")
        elif self.ui.r_line.text()=="" or self.ui.g_line.text()=="" or self.ui.b_line.text()=="" :
            self.ui.lbl_res.setText("Please enter the bits values!")
        elif self.ui.set_row.text() == "":
            self.ui.lbl_res.setText("Please enter the row values!")
        else:
            rbitVal = int(self.ui.r_line.text())
            gbitVal = int(self.ui.g_line.text())
            bbitVal = int(self.ui.b_line.text())
            rw_value= int(self.ui.set_row.text())
            rgb.get_zero_hexa_mif(self.image_path, rw_value, rbitVal, gbitVal, bbitVal)
            self.ui.lbl_res.setText("Filled With Zero hex.mif")

    def shift_(self):
        mul = float(self.ui.shft_input.text())
        i = 1
        sum = 0
        if mul >= 1 or mul <= 0:
            QMessageBox.about(self, "ERROR", "Please enter the number in the correct range!")
        else:
            while True:
                shifted = 0.5 ** i
                if mul > sum + shifted:
                    sum = sum + shifted
                    self.ui.textedit.append("float" + str(i) + "  used: " + str(shifted))
                elif mul < sum + shifted:
                    pass
                else:
                    sum = sum + shifted
                    self.ui.textedit.append("float" + str(i) + "  used: " + str(shifted))
                    break
                i = i + 1
                if i == 20:
                    break
            self.ui.textedit.append("iteration: " + str(i) + "\n" + str(sum))
    def gray_bin(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        else:
            gray.get_gray_binary(self.image_path_gray)
            self.ui.lbl_res_2.setText("Converted Binary.dat")
    def gray_bin_coe(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        else:
            gray.get_gray_binary_coe(self.image_path_gray)
            self.ui.lbl_res_2.setText("Converted Binary.coe")
    def gray_bin_mif(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        else:
            gray.get_gray_binary_mif(self.image_path_gray)
            self.ui.lbl_res_2.setText("Converted Binary.mif")
    def gray_hexa(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        else:
            gray.get_gray_hex(self.image_path_gray)
            self.ui.lbl_res_2.setText("Converted hex.dat")
    def gray_hexa_coe(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        else:
            gray.get_gray_hex_coe(self.image_path_gray)
            self.ui.lbl_res_2.setText("Converted hex.coe")
    def gray_hexa_mif(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        else:
            gray.get_gray_hex_mif(self.image_path_gray)
            self.ui.lbl_res_2.setText("Converted hex.mif")
    def fill_zero_bin_gray(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_2.text() == "":
            self.ui.lbl_res_2.setText("Please enter the row values!")
        else:
            rw_value = int(self.ui.set_row_2.text())
            gray.get_zero_bin_gray(self.image_path_gray, rw_value)
            self.ui.lbl_res_2.setText("Filled With Zero bin.dat")

    def fill_zero_hex_gray(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_2.text() == "":
            self.ui.lbl_res_2.setText("Please enter the row values!")
        else:
            rw_value = int(self.ui.set_row_2.text())
            gray.get_zero_hexa_gray(self.image_path_gray, rw_value)
            self.ui.lbl_res_2.setText("Filled With Zero hex.dat")

    def fill_zero_bin_gray_coe(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_2.text() == "":
            self.ui.lbl_res_2.setText("Please enter the row values!")
        else:
            rw_value = int(self.ui.set_row_2.text())
            gray.get_zero_bin_coe_gray(self.image_path_gray, rw_value)
            self.ui.lbl_res_2.setText("Filled With Zero bin.coe")

    def fill_zero_hex_gray_coe(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_2.text() == "":
            self.ui.lbl_res_2.setText("Please enter the row values!")
        else:
            rw_value = int(self.ui.set_row_2.text())
            gray.get_zero_hexa_coe_gray(self.image_path_gray, rw_value)
            self.ui.lbl_res_2.setText("Filled With Zero hex.coe")

    def fill_zero_bin_gray_mif(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_2.text() == "":
            self.ui.lbl_res_2.setText("Please enter the row values!")
        else:
            rw_value = int(self.ui.set_row_2.text())
            gray.get_zero_bin_mif_gray(self.image_path_gray, rw_value)
            self.ui.lbl_res_2.setText("Filled With Zero bin.mif")

    def fill_zero_hex_gray_mif(self):
        if self.image_path_gray == "":
            self.ui.lbl_res_2.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_2.text() == "":
            self.ui.lbl_res_2.setText("Please enter the row values!")
        else:
            rw_value = int(self.ui.set_row_2.text())
            gray.get_zero_hexa_mif_gray(self.image_path_gray, rw_value)
            self.ui.lbl_res_2.setText("Filled With Zero hex.mif")

#######################
    def ycbcr_bin(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr.get_ycbcr_binary(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr Converted Binary.dat")
    def ycbcr_bin_coe(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr.get_ycbcr_binary_coe(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr Converted Binary.coe")

    def ycbcr_bin_mif(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr.get_ycrcb_binary_mif(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr Converted Binary.mif")

    def ycbcr_hex(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr.get_ycrcb_hex(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr Converted hexadecimal.dat")

    def ycbcr_hex_coe(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr.get_ycbcr_hex_coe(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr Converted hexadecimal.coe")

    def ycbcr_hex_mif(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr.get_ycbcr_hex_mif(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr Converted hexadecimal.coe")

    def fill_zero_bin_ycbcr(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_3.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_3.text())
            ycbcr.get_zero_bin_ycbcr(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr Filled With Zero bin.dat")
    def fill_zero_hex_ycbcr(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_3.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_3.text())
            ycbcr.get_zero_hexa_ycbcr(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr Filled With Zero hexa.dat")

    def fill_zero_bin_ycbcr_coe(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_3.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_3.text())
            ycbcr.get_zero_bin_coe_ycbcr(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr Filled With Zero bin.coe")
    def fill_zero_hex_ycbcr_coe(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_3.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_3.text())
            ycbcr.get_zero_hexa_coe(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr Filled With Zero hexa.coe")

    def fill_zero_bin_ycbcr_mif(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_3.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_3.text())
            ycbcr.get_zero_bin_mif(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr Filled With Zero bin.mif")
    def fill_zero_hex_ycbcr_mif(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_3.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_3.text())
            ycbcr.get_zero_hexa_mif(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr Filled With Zero hexa.mif")
######################################
    def ycbcr422_bin(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr422.get_ycbcr422_binary(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr422 Converted Binary.dat")

    def ycbcr422_bin_coe(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr422.get_ycbcr422_binary_coe(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr422 Converted Binary.coe")
    def ycbcr422_bin_mif(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr422.get_ycrcb422_binary_mif(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr422 Converted Binary.mif")

    def ycbcr422_hex(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr422.get_ycrcb422_hex(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr422 Converted hexa.dat")
    def ycbcr422_hex_coe(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr422.get_ycrcb422_hex_coe(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr422 Converted hexa.coe")
    def ycbcr422_hex_mif(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        else:
            ycbcr422.get_ycrcb422_hex_mif(self.image_path_ycbcr)
            self.ui.lbl_res_3.setText("Ycbcr422 Converted hexa.mif")

    def fill_zero_bin_ycbcr422(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_4.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_4.text())
            ycbcr422.get_zero_bin_ycbcr422(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr422 Filled With Zero bin.dat")
    def fill_zero_hex_ycbcr422(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_4.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_4.text())
            ycbcr422.get_zero_hexa_ycbcr422(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr422 Filled With Zero hexa.dat")
    def fill_zero_bin_coe_ycbcr422(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_4.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_4.text())
            ycbcr422.get_zero_bin_coe_ycbcr422(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr422 Filled With Zero bin.coe")

    def fill_zero_hexa_coe422(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_4.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_4.text())
            ycbcr422.get_zero_hexa_coe422(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr422 Filled With Zero hexa.coe")
    def fill_zero_bin_mif422(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_4.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value= int(self.ui.set_row_4.text())
            ycbcr422.get_zero_bin_mif422(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr422 Filled With Zero bin.mif")

    def fill_zero_hexa_mif422(self):
        if self.image_path_ycbcr == "":
            self.ui.lbl_res_3.setText("!!!!!Image is not loading!!!!")
        elif self.ui.set_row_4.text() == "":
            self.ui.lbl_res_3.setText("Please enter the row values!")
        else:
            rw_value = int(self.ui.set_row_4.text())
            ycbcr422.get_zero_hexa_mif422(self.image_path_ycbcr, rw_value)
            self.ui.lbl_res_3.setText("Ycbcr422 Filled With Zero hexa.mif")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
