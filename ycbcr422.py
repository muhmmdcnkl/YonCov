import numpy as np
import cv2
def get_ycbcr422_binary(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr422_binary.dat"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    with open(path_img, 'w') as outfile:
        for i in range(0, len(bitarray)):
            for j in range(0, len(bitarray[i]), 2):
                x = bitarray[i, j, [0, 1]]
                x2 = bitarray[i, j, [2]]
                x3 = bitarray[i, j + 1, [0]]

                outfile.write(
                    str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")
                outfile.write(
                    str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")

        outfile.close()
def get_ycbcr422_binary_coe(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr422_binary.coe"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    with open(path_img, 'w') as outfile:
        outfile.write(
            "; Sample memory initialization file for Dual Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies the contents for a block memory\n; of depth=, and width=16.  In this case, values are specified\n; in hexadecimal format.\nmemory_initialization_radix=2;\nmemory_initialization_vector=\n")
        for i in range(0, len(bitarray)):
            for j in range(0, len(bitarray[i]), 2):
                x = bitarray[i, j, [0, 1]]
                x2 = bitarray[i, j, [2]]
                x3 = bitarray[i, j + 1, [0]]
                outfile.write(
                    str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")
                outfile.write(
                    str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")
        outfile.close()

def get_ycrcb422_binary_mif(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycrcb422_binary.mif"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    c = len(im_ycrcb) * len(im_ycrcb[i])

    with open(path_img, 'w') as outfile:
        outfile.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile.write("WIDTH =" + str(16) + ";\n")
        outfile.write("DEPTH =" + str(c) + ";\n")
        outfile.write("ADDRESS_RADIX = UNS;\n")
        outfile.write("DATA_RADIX=BIN;\n")
        outfile.write("CONTENT BEGIN\n")
        temp = 0
        for i in range(0, len(bitarray)):
            for j in range(0, len(bitarray[i]), 2):
                outfile.write(str(temp) + " : ")
                x = bitarray[i, j, [0, 1]]
                x2 = bitarray[i, j, [2]]
                x3 = bitarray[i, j + 1, [0]]
                outfile.write(
                    str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '')+";\n")
                temp = temp + 1
                outfile.write(str(temp) + " : ")
                outfile.write(
                    str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', ''))
                temp = temp + 1
                outfile.write(";\n")
        outfile.write("END;\n")
        outfile.close()
def get_ycrcb422_hex(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr422_hexa.dat"
    np.set_printoptions(formatter={'int': lambda im_ycrcb: hex(int(im_ycrcb))[2:].zfill(2)})

    with open(path_img, 'w') as outfile:
        for i in range(0, len(im_ycrcb)):
            for j in range(0, len(im_ycrcb[i]), 2):
                x = im_ycrcb[i, j, [0]]
                x1= im_ycrcb[i, j, [1]]
                x2 = im_ycrcb[i, j, [2]]
                x3 = im_ycrcb[i, j + 1, [0]]


                outfile.write(
                    str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(x1).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') +"\n")
                outfile.write(
                    str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")

        outfile.close()


def get_ycrcb422_hex_coe(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr422_hexa.coe"
    np.set_printoptions(formatter={'int': lambda im_ycrcb: hex(int(im_ycrcb))[2:].zfill(2)})

    with open(path_img, 'w') as outfile:
        outfile.write(
            "; Sample memory initialization file for Single Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies initialization values for a block\n; memory of depth=, and width=16. In this case, values are\n; specified in hexadecimal format.\nmemory_initialization_radix=16;\nmemory_initialization_vector=\n")
        for i in range(0, len(im_ycrcb)):
            for j in range(0, len(im_ycrcb[i]), 2):
                x = im_ycrcb[i, j, [0]]
                x1 = im_ycrcb[i, j, [1]]
                x2 = im_ycrcb[i, j, [2]]
                x3 = im_ycrcb[i, j + 1, [0]]

                outfile.write(
                    str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x1).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + ",\n")

                outfile.write(
                    str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + ",\n")

        outfile.close()

def get_ycrcb422_hex_mif(image_path_ycbcr):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr422_hexa.mif"
    np.set_printoptions(formatter={'int': lambda im_ycrcb: hex(int(im_ycrcb))[2:].zfill(2)})

    c = len(im_ycrcb) * len(im_ycrcb[1])
    with open(path_img, 'w') as outfile:
        outfile.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile.write("WIDTH =" + str(16) + ";\n")
        outfile.write("DEPTH =" + str(c) + ";\n")
        outfile.write("ADDRESS_RADIX = UNS;\n")
        outfile.write("DATA_RADIX=HEX;\n")
        outfile.write("CONTENT BEGIN\n")
        temp = 0
        for i in range(0, len(im_ycrcb)):
            for j in range(0, len(im_ycrcb[i]), 2):
                x = im_ycrcb[i, j, [0]]
                x1= im_ycrcb[i, j, [1]]
                x2 = im_ycrcb[i, j, [2]]
                x3 = im_ycrcb[i, j + 1, [0]]


                outfile.write(
                    str(temp) + " : " + str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(x1).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') +";\n")
                temp = temp + 1
                outfile.write(
                    str(temp) + " : " + str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + ";\n")

                temp = temp + 1

        outfile.write("END;\n")
        outfile.close()
######################
def get_zero_bin_ycbcr422(image_path_ycbcr,rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr422_binary.dat"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    with open(path_img, 'w') as outfile:
        for i in range(0, len(bitarray)):
            for j in range(0, len(bitarray[i]), 2):
                x = bitarray[i, j, [0, 1]]
                x2 = bitarray[i, j, [2]]
                x3 = bitarray[i, j + 1, [0]]

                outfile.write(
                    str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")
                outfile.write(
                    str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")

        outfile.close()
    with open(path_img, 'a') as outfile_zero:

        for i in range(rw_value):
            for j in range(16):
                outfile_zero.write("0")
            outfile_zero.write("\n")
        outfile_zero.close()
def get_zero_hexa_ycbcr422(image_path_ycbcr, rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr422_hexa.dat"
    np.set_printoptions(formatter={'int': lambda im_ycrcb: hex(int(im_ycrcb))[2:].zfill(2)})

    with open(path_img, 'w') as outfile:
        for i in range(0, len(im_ycrcb)):
            for j in range(0, len(im_ycrcb[i]), 2):
                x = im_ycrcb[i, j, [0]]
                x1 = im_ycrcb[i, j, [1]]
                x2 = im_ycrcb[i, j, [2]]
                x3 = im_ycrcb[i, j + 1, [0]]

                outfile.write(
                    str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x1).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")
                outfile.write(
                    str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")

        outfile.close()
    with open(path_img, 'a') as outfile_zero:

        for i in range(rw_value):
            for j in range(4):
                outfile_zero.write("0")
            outfile_zero.write("\n")
        outfile_zero.close()
def get_zero_bin_coe_ycbcr422(image_path_ycbcr, rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr422_binary.coe"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    with open(path_img, 'w') as outfile:
        outfile.write(
            "; Sample memory initialization file for Dual Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies the contents for a block memory\n; of depth=, and width=24.  In this case, values are specified\n; in hexadecimal format.\nmemory_initialization_radix=2;\nmemory_initialization_vector=\n")
        for i in range(0, len(bitarray)):
            for j in range(0, len(bitarray[i]), 2):
                x = bitarray[i, j, [0, 1]]
                x2 = bitarray[i, j, [2]]
                x3 = bitarray[i, j + 1, [0]]
                outfile.write(
                    str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")
                outfile.write(
                    str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + "\n")
        outfile.close()
    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            for j in range(16):
                outfile_zero.write("0")
            outfile_zero.write(",\n")
        outfile_zero.close()
def get_zero_hexa_coe422(image_path_ycbcr, rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr422_hexa.coe"
    np.set_printoptions(formatter={'int': lambda im_ycrcb: hex(int(im_ycrcb))[2:].zfill(2)})

    with open(path_img, 'w') as outfile:
        outfile.write(
            "; Sample memory initialization file for Single Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies initialization values for a block\n; memory of depth=, and width=8. In this case, values are\n; specified in hexadecimal format.\nmemory_initialization_radix=16;\nmemory_initialization_vector=\n")
        for i in range(0, len(im_ycrcb)):
            for j in range(0, len(im_ycrcb[i]), 2):
                x = im_ycrcb[i, j, [0]]
                x1 = im_ycrcb[i, j, [1]]
                x2 = im_ycrcb[i, j, [2]]
                x3 = im_ycrcb[i, j + 1, [0]]
                outfile.write(
                    str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x1).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']',
                                                                                                        '') + ",\n")
                outfile.write(
                    str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + ",\n")
        outfile.close()
    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            for j in range(4):
                outfile_zero.write("0")
            outfile_zero.write(",\n")
        outfile_zero.close()

def get_zero_bin_mif422(image_path_ycbcr, rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycrcb422_binary.mif"
    bitarray = np.empty((im_ycrcb.shape), dtype=bytearray)

    for i in range(len(im_ycrcb)):
        for j in range(len(im_ycrcb[i])):
            for k in range(3):
                bitarray[i][j][k] = np.binary_repr(im_ycrcb[i][j][k], width=8)

    c = len(im_ycrcb) * len(im_ycrcb[i])+rw_value

    with open(path_img, 'w') as outfile:
        outfile.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile.write("WIDTH =" + str(16) + ";\n")
        outfile.write("DEPTH =" + str(c) + ";\n")
        outfile.write("ADDRESS_RADIX = UNS;\n")
        outfile.write("DATA_RADIX=BIN;\n")
        outfile.write("CONTENT BEGIN\n")
        temp = 0
        for i in range(0, len(bitarray)):
            for j in range(0, len(bitarray[i]), 2):
                outfile.write(str(temp) + " : ")
                x = bitarray[i, j, [0, 1]]
                x2 = bitarray[i, j, [2]]
                x3 = bitarray[i, j + 1, [0]]
                outfile.write(
                    str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + ";\n")
                temp = temp + 1
                outfile.write(str(temp) + " : ")
                outfile.write(
                    str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', ''))
                temp = temp + 1
                outfile.write(";\n")
        outfile.close()
    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            outfile_zero.write(str(temp) + " : ")
            for j in range(16):
                outfile_zero.write("0")
            temp = temp + 1
            outfile_zero.write(";\n")
        outfile_zero.write("END;\n")
        outfile_zero.close()
def get_zero_hexa_mif422(image_path_ycbcr, rw_value):
    im = cv2.imread(image_path_ycbcr)
    im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    path_img = str(image_path_ycbcr) + "_ycbcr422_hexa.mif"
    np.set_printoptions(formatter={'int': lambda im_ycrcb: hex(int(im_ycrcb))[2:].zfill(2)})

    c = len(im_ycrcb) * len(im_ycrcb[1])+rw_value
    with open(path_img, 'w') as outfile:
        outfile.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile.write("WIDTH =" + str(16) + ";\n")
        outfile.write("DEPTH =" + str(c) + ";\n")
        outfile.write("ADDRESS_RADIX = UNS;\n")
        outfile.write("DATA_RADIX=HEX;\n")
        outfile.write("CONTENT BEGIN\n")
        temp = 0
        for i in range(0, len(im_ycrcb)):
            for j in range(0, len(im_ycrcb[i]), 2):
                x = im_ycrcb[i, j, [0]]
                x1 = im_ycrcb[i, j, [1]]
                x2 = im_ycrcb[i, j, [2]]
                x3 = im_ycrcb[i, j + 1, [0]]
                outfile.write(
                    str(temp) + " : " + str(x).replace("'", "").replace(' ', '').replace('.', '').replace('[',
                                                                                                          '').replace(
                        ']', '') + str(x1).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(
                        ']', '') + ";\n")
                temp = temp + 1
                outfile.write(
                    str(temp) + " : " + str(x3).replace("'", "").replace(' ', '').replace('.', '').replace('[',
                                                                                                           '').replace(
                        ']', '') + str(
                        x2).replace("'", "").replace(' ', '').replace('.', '').replace('[', '').replace(']', '') + ";\n")
                temp = temp + 1
        outfile.close()

    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            outfile_zero.write(str(temp) + " : ")
            for j in range(4):
                outfile_zero.write("0")
            temp = temp + 1
            outfile_zero.write(";\n")
        outfile_zero.write("END;\n")
        outfile_zero.close()






