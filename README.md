# 北京青年大学习

> 注意：本项目仅供学习交流使用，请勿用于商业用途，否则后果自负。

## 简介
本项目是北京青年大学习的速刷程序，可以迅速完成学习任务。

## 特性
- 自动识别学习任务是否完成，完成后自动退出。
- 自动识别验证码，无需人工干预。
- 支持多用户
- 支持部署到各种定时任务平台，如：Windows计划任务、Linux Crontab、青龙等。

## 使用方法

1. 安装Python3，建议使用Python3.7-3.10版本，下载地址：[Python3.10](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)，版本过高可能会出现兼容性问题。
2. 安装依赖库，打开命令行，输入以下命令：
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
3. 配置账户信息，打开`account.csv.example`文件，按照格式填写账户信息，保存为`account.csv`。
4. 运行程序，打开命令行，输入以下命令：
```
python Beijng_Daxuexi.py
```
5. 程序会自动完成学习任务，完成后会自动退出。

## 注意事项
1. 程序会自动识别当前学习任务是否完成，如果学习任务完成，程序会自动跳过学习任务。
2. 本程序只会完成最新的学习任务，不会完成题目，也不会完成旧的学习任务。

## 目录结构
- `account.csv`：账户信息文件（示例），用于配置账户信息。
- `Beijng_Daxuexi.py`：主程序文件，用于完成学习任务。
- `requirements.txt`：依赖库文件，用于安装依赖库。
- `README.md`：说明文件。
- `LICENSE`：许可证文件。
- `utility.py`：工具文件，用于提供工具函数。

## 致谢
本项目参考了以下项目：
- [startkkkkkk/Beijing_Daxuexi_Simple](https://github.com/startkkkkkk/Beijing_Daxuexi_Simple)
- [sml2h3/ddddocr](https://github.com/sml2h3/ddddocr)