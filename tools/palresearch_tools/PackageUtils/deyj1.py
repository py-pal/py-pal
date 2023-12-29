#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import utilcommon
from ctypes import *


def deYJ1(input):
    dll = cdll.LoadLibrary(utilcommon.getPallibPath())
    buffer = POINTER(c_byte)()
    length = c_int()
    dll.decodeyj1(input, byref(buffer), byref(length))
    return string_at(buffer, length)


def process(inputf, output_path):
    # 读取输入文件内容
    input_content = deYJ1(inputf.read())
    # 关闭输入文件
    inputf.close()

    # 获取输入文件的基本名称（不含路径和后缀）
    input_file_base_name = os.path.splitext(os.path.basename(inputf.name))[0]

    # 检查输出路径是否存在，如果不存在则创建
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 构造输出文件的完整路径
    output_file_path = os.path.join(output_path, input_file_base_name + ".smkf")

    # 将解码后的内容写入输出文件
    with open(output_file_path, "wb") as output_file:
        output_file.write(input_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YJ1 decompressing util")
    parser.add_argument("YJ1", type=argparse.FileType("rb"), help="YJ1 file to extract")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        help="path for unpacked file (without filename)",
    )

    args = parser.parse_args()
    if utilcommon.PallibExist():
        process(args.YJ1, args.output)
    else:
        print("PalLib not exist. Please build it first in PalLibrary folder")
