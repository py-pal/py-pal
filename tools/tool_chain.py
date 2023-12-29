# -*- coding: utf-8 -*-
"""
这个脚本用于解包和转换MKF文件中的资源。
MKF文件是某些老旧游戏（如《仙剑奇侠传》）中用于存储游戏资源的一种格式。
通常，这些资源需要被解包并转换成标准格式以便查看或编辑。

此脚本只是使用一般规则对mkf进行解压，不适用于所有mkf。
后续将对不同类型mkf针对性开发脚本。
"""


# 导入必要的库
import os
import subprocess
import glob


# 定义创建文件夹的函数
def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)


# 定义运行 demkf 工具的函数
def run_demkf(python_executable, demkf_tool, mkf_file, output_dir):
    subprocess.run(
        [python_executable, demkf_tool, "-p", "yj1", mkf_file], cwd=output_dir
    )


# 定义运行 deyj1 工具的函数
def run_deyj1(python_executable, deyj1_tool, yj1_file, output_dir):
    subprocess.run([python_executable, deyj1_tool, yj1_file, "-o", output_dir])


# 定义运行 desmkf 工具的函数
def run_desmkf(python_executable, desmkf_tool, smkf_file, output_dir):
    subprocess.run(
        [python_executable, desmkf_tool, "-p", "rle", smkf_file], cwd=output_dir
    )


# 定义运行 derle 工具的函数
def run_derle(python_executable, derle_tool, rle_file, pat_file, output_dir):
    # 构建输出 BMP 文件的路径
    output_file = os.path.relpath(rle_file, start=output_dir).replace(".rle", ".bmp")
    bmp_output_path = os.path.join(output_dir, output_file)

    # 确保输出文件夹存在
    os.makedirs(os.path.dirname(bmp_output_path), exist_ok=True)

    # 运行 derle 工具
    subprocess.run(
        [python_executable, derle_tool, rle_file, "-o", output_dir, "-p", pat_file]
    )


# 配置是否执行每个步骤
execute_step_1 = True
execute_step_2 = True
execute_step_3 = True
execute_step_4 = True

# 控制是否只处理第一个文件(方便调试)
single_file_debug_mode = True

# 获取当前脚本的绝对路径
current_path = os.path.abspath(__file__)
# 获取当前脚本所在的目录
current_dir = os.path.dirname(current_path)

# 每步骤的输出目录
step_1_folder = "yj1"
step_2_folder = "smkf"
step_3_folder = "rle"
step_4_folder = "bmp"

# 配置 Python 可执行文件路径
python_executable = "python"  # 或 "python3"

# 配置工具路径
tool_path = current_dir + "/palresearch_tools/PackageUtils/"
demkf_tool = tool_path + "demkf.py"
deyj1_tool = tool_path + "deyj1.py"
desmkf_tool = tool_path + "desmkf.py"
derle_tool = tool_path + "derle.py"

# 指定 MKF 文件的源路径
mkf_dir = "D:/Users/couger/Downloads/Entertainment/project/sdlpal_HD/归档_research"
output_base_dir = "D:/Users/couger/Downloads/Entertainment/project/sdlpal_HD/MKF"

# 指定 BMP 需要的 PAT 调色板文件的目录
PAT_dir = output_base_dir

# 获取所有 MKF 文件
mkf_files = glob.glob(os.path.join(mkf_dir, "*.mkf"))
print(f"发现 {len(mkf_files)} 个 MKF 文件。")

# 统计解包数量、成功数量、失败数量
total_files = len(mkf_files)
processed_files = 0
successful_files = 0
failed_files = 0

# 取第一个文件进行处理
mkf_file = mkf_files[0] if single_file_debug_mode else None

if mkf_file:
    # 获取文件名和不带扩展名的文件名
    file_name = os.path.basename(mkf_file)
    name_without_ext = os.path.splitext(file_name)[0]

    # 构建输出目录路径
    output_dir_MKF_File = os.path.join(output_base_dir, name_without_ext)

    # 创建每个 MKF 文件的输出目录
    create_folder(output_dir_MKF_File)

    # 创建步骤2、3、4的输出目录
    output_dir_step_2 = os.path.join(output_dir_MKF_File, step_2_folder)
    output_dir_step_3 = os.path.join(output_dir_MKF_File, step_3_folder)
    output_dir_step_4 = os.path.join(output_dir_MKF_File, step_4_folder)

    create_folder(output_dir_step_2)
    create_folder(output_dir_step_3)
    create_folder(output_dir_step_4)

    # 第一步：运行 demkf 解包工具
    if execute_step_1:
        try:
            print(f"开始解包 {file_name}...")
            run_demkf(python_executable, demkf_tool, mkf_file, output_dir_MKF_File)
            # 检查解包后的文件
            yj1_files_check = glob.glob(
                os.path.join(output_dir_MKF_File, step_1_folder, "*.yj1")
            )
            print(f"第一步完成，生成 {len(yj1_files_check)} 个 YJ1 文件。")
            if len(yj1_files_check) == 0:
                print(
                    f"警告：在 {output_dir_MKF_File + '/' + step_1_folder} 中没有找到 YJ1 文件，请检查 demkf 工具是否正常工作。"
                )
                failed_files += 1
            else:
                successful_files += 1
        except Exception as e:
            print(f"异常：在解包 {file_name} 时发生错误：{e}")
            failed_files += 1

    # 第二步：运行 deyj1 解压工具
    if execute_step_2:
        yj1_files = glob.glob(os.path.join(output_dir_MKF_File, step_1_folder, "*.yj1"))
        print(f"找到 {len(yj1_files)} 个 YJ1 文件待处理.")
        for yj1_file in yj1_files:
            # 检查输入文件大小
            if os.path.getsize(yj1_file) == 0:
                print(f"跳过处理空文件: {os.path.basename(yj1_file)}")
                continue

            try:
                run_deyj1(python_executable, deyj1_tool, yj1_file, output_dir_step_2)
                processed_files += 1
                successful_files += 1
            except Exception as e:
                print(f"异常：在解压 {os.path.basename(yj1_file)} 时发生错误：{e}")
                failed_files += 1

    # 第三步：运行 desmkf 解包工具
    if execute_step_3:
        smkf_files = glob.glob(os.path.join(output_dir_step_2, "*.smkf"))
        print(f"找到 {len(smkf_files)} 个 SMKF 文件待处理.")
        for smkf_file in smkf_files:
            # 检查输入文件大小
            if os.path.getsize(smkf_file) == 0:
                print(f"跳过处理空文件: {os.path.basename(smkf_file)}")
                continue

            try:
                run_desmkf(python_executable, desmkf_tool, smkf_file, output_dir_step_3)
                processed_files += 1
                successful_files += 1
            except Exception as e:
                print(f"异常：在解包 {os.path.basename(smkf_file)} 时发生错误：{e}")
                failed_files += 1

    # 第四步：运行 derle 解压带调色板的 BMP/PNG 工具
    if execute_step_4:
        os.chdir(output_dir_step_3)  # 修改工作目录为第三步的输出目录

        for root, _, files in os.walk("."):  # 遍历目录及子目录下的文件
            rle_files = [
                os.path.join(root, file) for file in files if file.endswith(".rle")
            ]
            print(f"找到 {len(rle_files)} 个 RLE 文件待处理.")
            for rle_file in rle_files:
                # 检查输入文件大小
                if os.path.getsize(rle_file) == 0:
                    print(f"跳过处理空文件: {rle_file}")
                    continue

                try:
                    run_derle(
                        python_executable,
                        derle_tool,
                        rle_file,
                        PAT_dir + "/PAT.MKF",
                        output_dir_step_4,
                    )
                    processed_files += 1
                    successful_files += 1
                except Exception as e:
                    print(f"异常：在处理 {os.path.basename(rle_file)} 时发生错误：{e}")
                    failed_files += 1

            # 实时显示总体解包情况
            print(
                f"总体解包情况：共处理 {processed_files} 个文件，成功 {successful_files} 个，失败 {failed_files} 个。",
                end="\r",
            )

# 打印最终统计信息
print("\n解包过程完成。")  # 添加换行符，以便在最后显示总体解包情况
