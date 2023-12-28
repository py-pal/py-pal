# tool-chain_PackageUtils

本工具链py脚本基于palresearch项目中的的PackageUtils工具包制作

**注意**
**已经对palresearch中的工具脚本进行了修改，因此不适用于原始脚本。**

## 开发计划

- 基于palresearch项目的PackageUtils工具包进行开发
- pal全部资源的自动化解包、封包(针对MKF格式开发中)
- GUI界面操作(未实现)
- pal中全部资源树形目录清单，包括解包后的原始资源(未实现)
- 自由选择需要解包、封包的资源(未实现)
- pal中各种资源的自由替换(未实现)

## 文件说明

- palresearch_tools(修改过的palresearch项目中工具)
- tool_chain.py(按照一般规则解开所有mkf，单线程，对有些mkf不适用)
<!-- - tool_chain_concu.py(多线程并发，未实现) -->
- deSSS_html.py(将事件文件SSS.mkf解开，将16进制的代码使用表格呈现，且保存为HTML)
- deSSS_table_descriptions.json(表格字段描述)
- deSSS_table_module.html(html模板)

## 开发环境

### Python

- 保持使用最新稳定版本
- 当前为: Python3.12
- 使用 pyupgrade 保持对代码的自动更新

### PackageUtils工具包

请参照palresearch项目中的内容进行研究

- [palresearch](https://github.com/palxex/palresearch)
