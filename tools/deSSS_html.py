# -*- coding: utf-8 -*-
"""
这个脚本用于解包和转换事件文件SSS.mkf。

将16进制的事件代码使用html文件中的表格形式进行呈现。
"""

import os
import json

# 设置文件路径
directory_path = (
    r"C:\Users\couger\Downloads\Entertainment\project\sdlpal_HD\decode\sss\yj1"
)
# 示例文件列表
file_names = ["SSS0.yj1", "SSS1.yj1", "SSS2.yj1", "SSS3.yj1", "SSS4.yj1"]
# 输出html模板
template_name = "deSSS_Table_module.html"
# 输出表格字段描述
descriptions_json = "deSSS_table_descriptions.json"

template_path = template_name
descriptions_path = descriptions_json

# 读取描述文件
try:
    with open(descriptions_path, "r", encoding="utf-8") as json_file:
        descriptions = json.load(json_file)
except FileNotFoundError:
    print(f"Error: The file {descriptions_path} does not exist.")
    descriptions = {}

# 读取模板文件
with open(template_path, "r", encoding="utf-8") as template_file:
    html_template = template_file.read()

# 处理每个文件
for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    output_name = "de" + os.path.splitext(file_name)[0] + ".html"  # 根据原始文件名生成输出文件名
    output_path = os.path.join(directory_path, output_name)

    # 读取二进制文件并转换为16进制
    with open(file_path, "rb") as file:
        file_content = file.read()

    # 获取特定文件的描述信息
    file_descriptions = descriptions.get(file_name, {})
    header = file_descriptions.get("header", [])
    column_descriptions = file_descriptions.get("column_descriptions", [])

    # 创建HTML表格
    table_content = "<table>\n"

    # 插入首行
    first_row = ["<th>OFFSET</th><td></td>"] + [f"<th>{desc}</th>" for desc in header]
    table_content += "  <tr>" + "".join(first_row) + "</tr>\n"

    # 添加二进制数据到表格
    for i in range(0, len(file_content), 32):  # 每行读取32字节
        hex_values = " ".join(
            f"{file_content[j:j+2].hex().upper():0>4}"
            for j in range(i, min(i + 32, len(file_content)), 2)
        )

        # 访问空白列的描述，如果索引超出范围，使用空字符串
        desc = (
            column_descriptions[i // 32] if i // 32 < len(column_descriptions) else ""
        )

        row_data = [f"<th>{i//32:04X}</th><td>{desc}</td>"] + [
            f"<td>{val}</td>" for val in hex_values.split(" ")
        ]

        table_content += "  <tr>" + "".join(row_data) + "</tr>\n"
    table_content += "</table>\n"

    # 将表格插入到HTML模板中
    html_output = html_template.replace("<!-- INSERT_TABLE_HERE -->", table_content)

    # 保存新的HTML文件
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(html_output)
