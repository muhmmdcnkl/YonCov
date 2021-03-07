import numpy as np
from PIL import Image

def get_rgb_binary(img_path, rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path)+ "_binary.dat"
    bitarray = np.empty((arr.shape), dtype=bytearray)


    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]

    with open(path_img, 'w') as outfile:

        for data_slice in bitarray:
            for d in data_slice:
                for i in d:
                    outfile.write(i)
                outfile.write("\n")
        outfile.close()

def get_rgb_binary_coe(img_path, rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path)+ "_binary.coe"
    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]
    with open(path_img, 'w') as outfile:
        outfile.write(
            "; Sample memory initialization file for Dual Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies the contents for a block memory\n; of depth=, and width=24.  In this case, values are specified\n; in hexadecimal format.\nmemory_initialization_radix=2;\nmemory_initialization_vector=\n")
        for data_slice in bitarray:
            for d in data_slice:
                for i in d:
                    outfile.write(i)
                outfile.write(",\n")
        outfile.close()

def get_rgb_binary_mif(img_path, rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path)+ "_binary.mif"
    bitarray = np.empty((arr.shape), dtype=bytearray)
    sumbits = rbitVal + gbitVal + bbitVal

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]
    d = len(arr) * len(arr[i])
    with open(path_img, 'w') as outfile:
        outfile.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile.write("WIDTH =" + str(sumbits) + ";\n")
        outfile.write("DEPTH =" + str(d) + ";\n")
        outfile.write("ADDRESS_RADIX = UNS;\n")
        outfile.write("DATA_RADIX=BIN;\n")
        outfile.write("CONTENT BEGIN\n")
        temp = 0
        for data_slice in bitarray:
            for d in data_slice:
                outfile.write(str(temp) + " : ")
                for i in d:
                    outfile.write(i)

                temp = temp + 1
                outfile.write(";\n")
        outfile.write("END;\n")
        outfile.close()
def get_rgb_hex(img_path,rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path) + "_hexa.dat"
    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]

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

def get_rgb_hex_coe(img_path,rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path) + "_hexa.coe"


    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]

    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "; Sample memory initialization file for Single Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies initialization values for a block\n; memory of depth=, and width=24. In this case, values are\n; specified in hexadecimal format.\nmemory_initialization_radix=16;\nmemory_initialization_vector=\n")
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

                outfile_hex.write(conv_h + ",")
                outfile_hex.write("\n")
        outfile_hex.close()
def get_rgb_hex_mif(img_path,rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path) + "_hexa.mif"

    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]
    d = len(arr) * len(arr[i])
    hexbits = rbitVal + gbitVal + bbitVal
    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile_hex.write("WIDTH =" + str(hexbits) + ";\n")
        outfile_hex.write("DEPTH =" + str(d) + ";\n")
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


def get_zero_bin(img_path, rw_value, rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path) + "_binary_zero.dat"
    bitarray = np.empty((arr.shape), dtype=bytearray)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]

    with open(path_img, 'w') as outfile:

        for data_slice in bitarray:
            for d in data_slice:
                for i in d:
                    outfile.write(i)
                outfile.write("\n")
        outfile.close()

    sumbit = rbitVal + gbitVal + bbitVal
    with open(path_img, 'a') as outfile_zero:

        for i in range(rw_value):
            for j in range(sumbit):
                outfile_zero.write("0")
            outfile_zero.write("\n")
        outfile_zero.close()
def get_zero_hexa(img_path, rw_value, rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path) + "_hexa_zero.dat"

    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]

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

    tbit =6
    with open(path_img, 'a') as outfile_zero:

        for i in range(rw_value):
            for j in range(tbit):
                outfile_zero.write("0")
            outfile_zero.write("\n")
        outfile_zero.close()
def get_zero_bin_coe(img_path, rw_value, rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path) + "_binary_zero.coe"
    bitarray = np.empty((arr.shape), dtype=bytearray)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]

    with open(path_img, 'w') as outfile:
        outfile.write(
            "; Sample memory initialization file for Dual Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies the contents for a block memory\n; of depth=, and width=24.  In this case, values are specified\n; in hexadecimal format.\nmemory_initialization_radix=2;\nmemory_initialization_vector=\n")
        for data_slice in bitarray:
            for d in data_slice:
                for i in d:
                    outfile.write(i)
                outfile.write(",\n")
        outfile.close()
    sumbit = rbitVal + gbitVal + bbitVal
    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            for j in range(sumbit):
                outfile_zero.write("0")
            outfile_zero.write(",\n")
        outfile_zero.close()
def get_zero_hexa_coe(img_path, rw_value, rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path) + "_hexa_zero.coe"
    bitarray = np.empty((arr.shape), dtype=bytearray)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]
    with open(path_img, 'w') as outfile_hex:
        outfile_hex.write(
            "; Sample memory initialization file for Single Port Block Memory,\n; v3.0 or later.\n;\n; This .COE file specifies initialization values for a block\n; memory of depth=, and width=24. In this case, values are\n; specified in hexadecimal format.\nmemory_initialization_radix=16;\nmemory_initialization_vector=\n")
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
                outfile_hex.write(conv_h + ",")
                outfile_hex.write("\n")
        outfile_hex.close()
    tbit =6
    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            for j in range(tbit):
                outfile_zero.write("0")
            outfile_zero.write(",\n")
        outfile_zero.close()

def get_zero_bin_mif(img_path, rw_value, rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path) + "_binary.mif"
    bitarray = np.empty((arr.shape), dtype=bytearray)
    sumbits = rbitVal + gbitVal + bbitVal
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]
    d = (len(arr) * len(arr[i]))+rw_value
    with open(path_img, 'w') as outfile:
        outfile.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile.write("WIDTH =" + str(sumbits) + ";\n")
        outfile.write("DEPTH =" + str(d) + ";\n")
        outfile.write("ADDRESS_RADIX = UNS;\n")
        outfile.write("DATA_RADIX=BIN;\n")
        outfile.write("CONTENT BEGIN\n")
        temp = 0
        for data_slice in bitarray:
            for d in data_slice:
                outfile.write(str(temp) + " : ")
                for i in d:
                    outfile.write(i)
                temp = temp + 1
                outfile.write(";\n")
        outfile.close()
    with open(path_img, 'a') as outfile_zero:
        for i in range(rw_value):
            outfile_zero.write(str(temp) + " : ")
            for j in range(sumbits):
                outfile_zero.write("0")
            temp = temp + 1
            outfile_zero.write(";\n")
        outfile_zero.write("END;\n")
        outfile_zero.close()
def get_zero_hexa_mif(img_path, rw_value, rbitVal, gbitVal, bbitVal):
    img = Image.open(img_path)
    arr = np.array(img)
    path_img = str(img_path) + "_hexa_zero.mif"
    sumbit = rbitVal + gbitVal + bbitVal
    bitarray = np.empty((arr.shape), dtype=bytearray)
    tbit = 6

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(3):
                if k % 3 == 0:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:rbitVal]
                elif k % 3 == 1:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:gbitVal]
                elif k % 3 == 2:
                    bitarray[i][j][k] = np.binary_repr(arr[i][j][k], width=8)[0:bbitVal]

    d =(len(arr)*len(arr[i]))+rw_value
    with open(path_img, 'w') as outfile_hex:
        temp = 0
        outfile_hex.write(
            "-- Copyright (C) 2018  Intel Corporation. All rights reserved.\n-- Your use of Intel Corporation's design tools, logic functions\n-- and other software and tools, and its AMPP partner logic\n-- functions, and any output files from any of the foregoing\n-- (including device programming or simulation files), and any\n-- associated documentation or information are expressly subject \n-- to the terms and conditions of the Intel Program License \n-- Subscription Agreement, the Intel Quartus Prime License Agreement,\n-- the Intel FPGA IP License Agreement, or other applicable license\n-- agreement, including, without limitation, that your use is for\n-- the sole purpose of programming logic devices manufactured by\n-- Intel and sold by Intel or its authorized distributors.\n-- Please refer to the applicable agreement for further details.\n-- Quartus Prime generated Memory Initialization File (.mif)\n")
        outfile_hex.write("WIDTH =" + str(sumbit) + ";\n")
        outfile_hex.write("DEPTH =" + str(d) + ";\n")
        outfile_hex.write("ADDRESS_RADIX = UNS;\n")
        outfile_hex.write("DATA_RADIX=HEX;\n")
        outfile_hex.write("CONTENT BEGIN\n")

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
            for j in range(tbit):
                outfile_zero.write("0")
            temp = temp + 1
            outfile_zero.write(";\n")
        outfile_zero.write("END;\n")
        outfile_zero.close()

