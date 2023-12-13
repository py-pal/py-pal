# py-pal

基于Python的仙剑奇侠传1重制版

## 开发计划

- 基于Arcade库进行开发
- 实现原版仙剑奇侠传1 Windows95版本的所有功能
- 尝试利用AI重新绘制部分图像资源，提高清晰度和分辨率
- 跨平台编译支持
- 重新设计脚本系统，添加新的剧情分支
- 提供地图/关卡编辑器

## 开发环境

### Python

- 保持使用最新稳定版本
- 当前为: Python3.12
- 使用 pyupgrade 保持对代码的自动更新

## Git hook

### pre-commit

#### 安装

```shell
pre-commit install
```

#### 已启用插件

- pyupgrade
- black
- iosrt

## 代码格式化

- Python
  - black
  - iosrt

- 文本类
  - Prettier
