#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import struct
import os


def deSMKF(f, postfix, output_path):
    mkf_name = os.path.basename(f.name)
    prefix = os.path.splitext(mkf_name)[0]
    output_dir = os.path.join(output_path, prefix)  # 创建以 smkf 文件名为名的新目录
    os.makedirs(output_dir, exist_ok=True)  # 确保新目录存在

    f.seek(0, os.SEEK_END)
    total_length = f.tell()
    f.seek(0, os.SEEK_SET)
    use_unsigned_short = total_length > 64 * 1024
    packarg = "<H" if use_unsigned_short else "<h"
    (first_index,) = struct.unpack(packarg, f.read(2))
    subfiles = first_index - 1

    for i in range(subfiles):
        f.seek(i * 2, os.SEEK_SET)
        (begin,) = struct.unpack(packarg, f.read(2))
        if i < subfiles - 1:
            (next_begin,) = struct.unpack(packarg, f.read(2))
            f.seek(-2, os.SEEK_CUR)
        else:
            next_begin = total_length // 2
        begin = begin if begin > 0 else 32768 + begin
        end = next_begin if next_begin > 0 else 32768 + next_begin
        end = end if end >= begin else total_length // 2
        f.seek(begin * 2, os.SEEK_SET)
        subfile_content = f.read((end - begin) * 2)
        with open(os.path.join(output_dir, f"{prefix}_{i}.{postfix}"), "wb") as subfile:
            subfile.write(subfile_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sMKF unpack util")
    parser.add_argument(
        "sMKF", type=argparse.FileType("rb"), help="sMKF file to unpack"
    )
    parser.add_argument(
        "-p", "--postfix", required=True, help="postfix for unpacked files"
    )
    parser.add_argument(
        "-o", "--output", default=".", help="output directory for unpacked files"
    )
    args = parser.parse_args()

    deSMKF(args.sMKF, args.postfix, args.output)
