import numpy as np
import cv2
def get_ycbcr_binary(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr_binary.dat"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)
    with open(path_img, 'w') as outfile:
        for data_slice in bitarray:
            for d in data_slice:
                for i in d:
                    outfile.write(str(i))
                outfile.write("\n")
        outfile.close()



def get_ycbcr_binary_coe(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr_binary.coe"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    with open(path_img, 'w') as outfile:
        outfile.write(
            "; Sample memory initialization file for Dual Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies the contents for a block memory\n; of depth=, and width=24.  In this case, values are specified\n; in hexadecimal format.\nmemory_initialization_radix=2;\nmemory_initialization_vector=\n")
        for data_slice in bitarray:
            for d in data_slice:
                outfile.write(str(d).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', ''))
                outfile.write(",\n")
        outfile.close()

def get_ycrcb_binary_mif(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycrcb_binary.mif"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    c = len(im_ycrcb) * len(im_ycrcb[i])

    with open(path_img, 'w') as outfile:
        outfile.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile.write("WIDTH =" + str(8) + ";\n")
        outfile.write("DEPTH =" + str(c) + ";\n")
        outfile.write("ADDRESS_RADIX = UNS;\n")
        outfile.write("DATA_RADIX=BIN;\n")
        outfile.write("CONTENT BEGIN\n")
        temp = 0
        for data_slice in bitarray:

            for d in data_slice:
                outfile.write(str(temp) + " : ")
                outfile.write(str(d).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', ''))
                temp = temp + 1
                outfile.write(";\n")
        outfile.write("END;\n")
        outfile.close()

def get_ycrcb_hex(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr_hexa.dat"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)
    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    with open(path_img, 'w') as outfile_hex:
        for data_slice in bitarray:
            for d in data_slice:
                con = []
                for i in d:
                    h = hex(int(i, 2))
                    w_h = h[2:]
                    con.append(w_h)

                conv_h = con[0] + con[1] + con[2]
                if len(conv_h) == 3:
                    conv_h = "000" + conv_h
                elif len(conv_h) == 4:
                    conv_h = "00" + conv_h
                elif len(conv_h) == 5:
                    conv_h = "0" + conv_h

                outfile_hex.write(conv_h)
                outfile_hex.write("\n")
        outfile_hex.close()

def get_ycbcr_hex_coe(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr_hexa.coe"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)
    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "; Sample memory initialization file for Single Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies initialization values for a block\n; memory of depth=, and width=8. In this case, values are\n; specified in hexadecimal format.\nmemory_initialization_radix=16;\nmemory_initialization_vector=\n")
        for data_slice in bitarray:
            for d in data_slice:
                for i in d:
                    h = hex(int(i, 2))
                    w_h = h[2:]
                    if len(w_h) == 1:
                        w_h = "0" + w_h
                    outfile_hex.write(str(w_h))
                outfile_hex.write(",\n")
        outfile_hex.close()
def get_ycbcr_hex_mif(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr_hexa.mif"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)
    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)
    c= len(im_ycrcb) * len(im_ycrcb[i])

    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile_hex.write("WIDTH =" + str(24) + ";\n")
        outfile_hex.write("DEPTH =" + str(c) + ";\n")
        outfile_hex.write("ADDRESS_RADIX = UNS;\n")
        outfile_hex.write("DATA_RADIX=HEX;\n")
        outfile_hex.write("CONTENT BEGIN\n")
        temp = 0
        for data_slice in bitarray:
            for d in data_slice:
                con = []
                for i in d:
                    h = hex(int(i, 2))
                    w_h = h[2:]
                    con.append(w_h)

                conv_h = con[0] + con[1] + con[2]
                if len(conv_h) == 3:
                    conv_h = "000" + conv_h
                elif len(conv_h) == 4:
                    conv_h = "00" + conv_h
                elif len(conv_h) == 5:
                    conv_h = "0" + conv_h
                outfile_hex.write(str(temp) + " : " + conv_h + ";")
                temp = temp + 1
                outfile_hex.write("\n")
        outfile_hex.write("END;\n")
        outfile_hex.close()
def get_zero_bin_ycbcr(image_path_ycbcr,rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr_binary_zero.dat"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)
    with open(path_img, 'w') as outfile:
        for data_slice in bitarray:
            for d in data_slice:
                for i in d:
                    outfile.write(str(i))
                outfile.write("\n")
        outfile.close()
    with open(path_img, 'a') as outfile_zero:

        for i in range(rw_value):
            for j in range(24):
                outfile_zero.write("0")
            outfile_zero.write("\n")
        outfile_zero.close()
def get_zero_hexa_ycbcr(image_path_ycbcr, rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr_hexa_zero.dat"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)
    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    with open(path_img, 'w') as outfile_hex:
        for data_slice in bitarray:
            for d in data_slice:
                con = []
                for i in d:
                    h = hex(int(i, 2))
                    w_h = h[2:]
                    con.append(w_h)

                conv_h = con[0] + con[1] + con[2]
                if len(conv_h) == 3:
                    conv_h = "000" + conv_h
                elif len(conv_h) == 4:
                    conv_h = "00" + conv_h
                elif len(conv_h) == 5:
                    conv_h = "0" + conv_h

                outfile_hex.write(conv_h)
                outfile_hex.write("\n")
        outfile_hex.close()
    with open(path_img, 'a') as outfile_zero:

        for i in range(rw_value):
            for j in range(6):
                outfile_zero.write("0")
            outfile_zero.write("\n")
        outfile_zero.close()
def get_zero_bin_coe_ycbcr(image_path_ycbcr, rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr_binary_zero.coe"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    with open(path_img, 'w') as outfile:
        outfile.write(
            "; Sample memory initialization file for Dual Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies the contents for a block memory\n; of depth=, and width=24.  In this case, values are specified\n; in hexadecimal format.\nmemory_initialization_radix=2;\nmemory_initialization_vector=\n")
        for data_slice in bitarray:
            for d in data_slice:
                outfile.write(
                    str(d).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', ''))
                outfile.write(",\n")
        outfile.close()
    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            for j in range(24):
                outfile_zero.write("0")
            outfile_zero.write(",\n")
        outfile_zero.close()
def get_zero_hexa_coe(image_path_ycbcr, rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr_hexa_zero.coe"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)
    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "; Sample memory initialization file for Single Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies initialization values for a block\n; memory of depth=, and width=8. In this case, values are\n; specified in hexadecimal format.\nmemory_initialization_radix=16;\nmemory_initialization_vector=\n")
        for data_slice in bitarray:
            for d in data_slice:
                for i in d:
                    h = hex(int(i, 2))
                    w_h = h[2:]
                    if len(w_h) == 1:
                        w_h = "0" + w_h
                    outfile_hex.write(str(w_h))
                outfile_hex.write(",\n")
        outfile_hex.close()
    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            for j in range(6):
                outfile_zero.write("0")
            outfile_zero.write(",\n")
        outfile_zero.close()

def get_zero_bin_mif(image_path_ycbcr, rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycrcb_binary_zero.mif"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    c = len(im_ycrcb) * len(im_ycrcb[i])

    with open(path_img, 'w') as outfile:
        outfile.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile.write("WIDTH =" + str(24) + ";\n")
        outfile.write("DEPTH =" + str(c) + ";\n")
        outfile.write("ADDRESS_RADIX = UNS;\n")
        outfile.write("DATA_RADIX=BIN;\n")
        outfile.write("CONTENT BEGIN\n")
        temp = 0
        for data_slice in bitarray:

            for d in data_slice:
                outfile.write(str(temp) + " : ")
                outfile.write(
                    str(d).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', ''))
                temp = temp + 1
                outfile.write(";\n")
        outfile.close()
    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            outfile_zero.write(str(temp) + " : ")
            for j in range(24):
                outfile_zero.write("0")
            temp = temp + 1
            outfile_zero.write(";\n")
        outfile_zero.write("END;\n")
        outfile_zero.close()
def get_zero_hexa_mif(image_path_ycbcr, rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr_hexa_zore.mif"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)
    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)
    c = len(im_ycrcb) * len(im_ycrcb[i])

    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile_hex.write("WIDTH =" + str(24) + ";\n")
        outfile_hex.write("DEPTH =" + str(c) + ";\n")
        outfile_hex.write("ADDRESS_RADIX = UNS;\n")
        outfile_hex.write("DATA_RADIX=HEX;\n")
        outfile_hex.write("CONTENT BEGIN\n")
        temp = 0
        for data_slice in bitarray:
            for d in data_slice:
                con = []
                for i in d:
                    h = hex(int(i, 2))
                    w_h = h[2:]
                    con.append(w_h)

                conv_h = con[0] + con[1] + con[2]
                if len(conv_h) == 3:
                    conv_h = "000" + conv_h
                elif len(conv_h) == 4:
                    conv_h = "00" + conv_h
                elif len(conv_h) == 5:
                    conv_h = "0" + conv_h
                outfile_hex.write(str(temp) + " : " + conv_h + ";")
                temp = temp + 1
                outfile_hex.write("\n")
        outfile_hex.close()

    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            outfile_zero.write(str(temp) + " : ")
            for j in range(6):
                outfile_zero.write("0")
            temp = temp + 1
            outfile_zero.write(";\n")
        outfile_zero.write("END;\n")
        outfile_zero.close()


