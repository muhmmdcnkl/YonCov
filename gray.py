import numpy as np
from PIL import Image

def get_gray_binary(image_path_gray):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray)+ "_gray_binary.dat"
    bitarray = np.empty((arr.shape), dtype=bytearray)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    with open(path_img, 'w') as outfile:

        for data_slice in bitarray:
            for d in data_slice:
                outfile.write(str(d))
                outfile.write("\n")
        outfile.close()

def get_gray_binary_coe(image_path_gray):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray)+ "_gray_binary.coe"
    bitarray = np.empty((arr.shape), dtype=bytearray)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    with open(path_img, 'w') as outfile:
        outfile.write(
            "; Sample memory initialization file for Dual Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies the contents for a block memory\n; of depth=, and width=24.  In this case, values are specified\n; in hexadecimal format.\nmemory_initialization_radix=2;\nmemory_initialization_vector=\n")
        for data_slice in bitarray:
            for d in data_slice:
                outfile.write(str(d))
                outfile.write(",\n")
        outfile.close()

def get_gray_binary_mif(image_path_gray):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray)+ "_gray_binary.mif"
    bitarray = np.empty((arr.shape), dtype=bytearray)


    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    c = len(arr) * len(arr[i])

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
                outfile.write(d)
                temp = temp + 1
                outfile.write(";\n")
        outfile.write("END;\n")
        outfile.close()




def get_gray_hex(image_path_gray):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray) + "_gray_hexa.dat"
    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    with open(path_img, 'w') as outfile_hex:
        for data_slice in bitarray:
            for d in data_slice:
                h = hex(int(d, 2))
                w_h = h[2:]
                if len(w_h) == 1:
                    w_h = "0" + w_h

                outfile_hex.write(str(w_h))

                outfile_hex.write("\n")
        outfile_hex.close()

def get_gray_hex_coe(image_path_gray):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray) + "_gray_hexa.coe"


    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "; Sample memory initialization file for Single Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies initialization values for a block\n; memory of depth=, and width=8. In this case, values are\n; specified in hexadecimal format.\nmemory_initialization_radix=16;\nmemory_initialization_vector=\n")
        for data_slice in bitarray:
            for d in data_slice:
                h = hex(int(d, 2))
                w_h = h[2:]
                if len(w_h) == 1:
                    w_h = "0" + w_h
                outfile_hex.write(str(w_h))
                outfile_hex.write(",\n")
        outfile_hex.close()
def get_gray_hex_mif(image_path_gray):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray) + "_gray_hexa.mif"

    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)
    c= len(arr) * len(arr[i])

    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile_hex.write("WIDTH =" + str(8) + ";\n")
        outfile_hex.write("DEPTH =" + str(c) + ";\n")
        outfile_hex.write("ADDRESS_RADIX = UNS;\n")
        outfile_hex.write("DATA_RADIX=HEX;\n")
        outfile_hex.write("CONTENT BEGIN\n")
        temp = 0
        for data_slice in bitarray:
            for d in data_slice:
                h = hex(int(d, 2))
                w_h = h[2:]
                if len(w_h) == 1:
                    w_h = "0" + w_h
                outfile_hex.write(str(temp) + " : " + w_h + ";")
                temp = temp + 1
                outfile_hex.write("\n")
        outfile_hex.write("END;\n")
        outfile_hex.close()


def get_zero_bin_gray(image_path_gray, rw_value):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray) + "_gray_binary_zero.dat"
    bitarray = np.empty((arr.shape), dtype=bytearray)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    with open(path_img, 'w') as outfile:

        for data_slice in bitarray:
            for d in data_slice:
                outfile.write(str(d))
                outfile.write("\n")
        outfile.close()


    with open(path_img, 'a') as outfile_zero:

        for i in range(rw_value):
            for j in range(8):
                outfile_zero.write("0")
            outfile_zero.write("\n")
        outfile_zero.close()
def get_zero_hexa_gray(image_path_gray, rw_value):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray) + "_gray_hexa_zero.dat"

    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    with open(path_img, 'w') as outfile_hex:
        for data_slice in bitarray:
            for d in data_slice:
                h = hex(int(d, 2))
                w_h = h[2:]
                if len(w_h) == 1:
                    w_h = "0" + w_h

                outfile_hex.write(str(w_h))

                outfile_hex.write("\n")
        outfile_hex.close()

    tbit =2
    with open(path_img, 'a') as outfile_zero:

        for i in range(rw_value):
            for j in range(tbit):
                outfile_zero.write("0")
            outfile_zero.write("\n")
        outfile_zero.close()
def get_zero_bin_coe_gray(image_path_gray, rw_value):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray) + "_gray_binary_zero.coe"
    bitarray = np.empty((arr.shape), dtype=bytearray)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    with open(path_img, 'w') as outfile:
        outfile.write(
            "; Sample memory initialization file for Dual Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies the contents for a block memory\n; of depth=, and width=24.  In this case, values are specified\n; in hexadecimal format.\nmemory_initialization_radix=2;\nmemory_initialization_vector=\n")
        for data_slice in bitarray:
            for d in data_slice:
                outfile.write(str(d))
                outfile.write(",\n")
        outfile.close()


    with open(path_img, 'a') as outfile_zero:

        for i in range(rw_value):
            for j in range(8):
                outfile_zero.write("0")
            outfile_zero.write(",\n")
        outfile_zero.close()
def get_zero_hexa_coe_gray(image_path_gray, rw_value):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray) + "_gray_hexa_zero.coe"

    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "; Sample memory initialization file for Single Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies initialization values for a block\n; memory of depth=, and width=8. In this case, values are\n; specified in hexadecimal format.\nmemory_initialization_radix=16;\nmemory_initialization_vector=\n")
        for data_slice in bitarray:
            for d in data_slice:
                h = hex(int(d, 2))
                w_h = h[2:]
                if len(w_h) == 1:
                    w_h = "0" + w_h
                outfile_hex.write(str(w_h))
                outfile_hex.write(",\n")
        outfile_hex.close()
    tbit =2
    with open(path_img, 'a') as outfile_zero:

        for i in range(rw_value):
            for j in range(tbit):
                outfile_zero.write("0")
            outfile_zero.write(",\n")
        outfile_zero.close()

def get_zero_bin_mif_gray(image_path_gray, rw_value):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray) + "_gray_binary.mif"
    bitarray = np.empty((arr.shape), dtype=bytearray)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    c= (len(arr) * len(arr[i]))+rw_value

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
                outfile.write(d)
                temp = temp + 1
                outfile.write(";\n")
        outfile.close()
    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            outfile_zero.write(str(temp) + " : ")
            for j in range(8):

                outfile_zero.write("0")
            temp = temp + 1
            outfile_zero.write(";\n")
        outfile_zero.write("END;\n")
        outfile_zero.close()
def get_zero_hexa_mif_gray(image_path_gray, rw_value):
    img = Image.open(image_path_gray)
    arr = np.array(img)
    path_img = str(image_path_gray) + "_gray_hexa_zero.mif"
    bitarray = np.empty((arr.shape), dtype=bytearray)
    tbit = 2
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            bitarray[i][j] = np.binary_repr(arr[i][j], width=8)

    c =(len(arr)*len(arr[i]))+rw_value
    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile_hex.write("WIDTH =" + str(8) + ";\n")
        outfile_hex.write("DEPTH =" + str(c) + ";\n")
        outfile_hex.write("ADDRESS_RADIX = UNS;\n")
        outfile_hex.write("DATA_RADIX=HEX;\n")
        outfile_hex.write("CONTENT BEGIN\n")
        temp = 0
        for data_slice in bitarray:
            for d in data_slice:
                h = hex(int(d, 2))
                w_h = h[2:]
                if len(w_h) == 1:
                    w_h = "0" + w_h
                outfile_hex.write(str(temp) + " : " + w_h + ";")
                temp = temp + 1
                outfile_hex.write("\n")
        outfile_hex.close()

    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            outfile_zero.write(str(temp) + " : ")
            for j in range(tbit):

                outfile_zero.write("0")
            temp = temp + 1
            outfile_zero.write(";\n")
        outfile_zero.write("END;\n")
        outfile_zero.close()

