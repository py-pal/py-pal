#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import struct
import os
import utilcommon
from ctypes import *
from PIL import Image, ImageDraw

args = None


def deRLE(input):
    dll = cdll.LoadLibrary(utilcommon.getPallibPath())
    width, height = struct.unpack("<hh", input[0:4])
    length = width * height
    ArrayType = c_int16 * length
    buffer = ArrayType()
    memset(buffer, args.transparent_palette_index, length)
    dll.decoderle(input, c_void_p(addressof(buffer)), width, width, height, 0, 0)
    return width, height, string_at(buffer, width * height)


def process():
    pat = utilcommon.getPalette(args)

    width, height, buffer = deRLE(args.rle.read())

    if args.saveraw:
        input_filename = os.path.splitext(os.path.basename(args.rle.name))[0]
        output_path = args.o or os.path.dirname(args.rle.name)

        # 新建目录
        output_directory = os.path.join(output_path, input_filename)
        os.makedirs(output_directory, exist_ok=True)

        output_filename = os.path.join(output_directory, input_filename + ".raw")
        open(output_filename, "wb").write(buffer)

    im = Image.frombytes("P", (width, height), buffer)
    im.putpalette(pat)

    im.info["transparency"] = args.transparent_palette_index

    if args.show:
        im.show()

    if args.o:
        input_filename = os.path.splitext(os.path.basename(args.rle.name))[0]
        output_path = args.o or os.path.dirname(args.rle.name)

        # 新建目录
        output_directory = os.path.join(output_path, input_filename)
        os.makedirs(output_directory, exist_ok=True)

        output_filename = os.path.join(output_directory, input_filename + ".png")
        im.save(output_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="tool for converting RLE to palette BMP/PNG"
    )
    parser.add_argument("rle", type=argparse.FileType("rb"), help="rle file to decode")
    parser.add_argument("-o", type=str, help="output path for the resulting images")
    parser.add_argument(
        "-p", "--palette", type=argparse.FileType("rb"), required=True, help="PAT file"
    )
    parser.add_argument("-i", "--palette_id", type=int, default=0, help="palette id")
    parser.add_argument(
        "-n", "--night", action="store_true", default=False, help="use night palette"
    )
    parser.add_argument(
        "-d",
        "--transparent_palette_index",
        default=0xFF,
        help="transparent index for color in palette; default 255",
    )
    parser.add_argument(
        "--show", action="store_true", default=False, help="show decoded image"
    )
    parser.add_argument(
        "--saveraw", action="store_true", default=False, help="save decoded raw data"
    )

    args = parser.parse_args()
    if not args.show and not args.o:
        print("Either Show or Specify output path")
    else:
        process()
