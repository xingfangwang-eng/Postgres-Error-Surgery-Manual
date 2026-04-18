import json
import os

# 读取错误代码数据
with open('../01_Crawler_Engine/pg_errors.json', 'r', encoding='utf-8') as f:
    errors = json.load(f)

# 确保输出目录存在
output_dir = './manual'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 生成 Markdown 文件
for error in errors:
    error_code = error['error_code']
    error_name = error['condition']
    
    # 生成文件名
    filename = f'ERR_{error_code}.md'
    filepath = os.path.join(output_dir, filename)
    
    # 生成文件内容
    content = f"""# [错误代码] : {error_code} [错误名称] : {error_name} 深度解析与排查方案

## 现象描述

当你在使用 PostgreSQL 时遇到这个错误，通常意味着 {error_name}。

## 基础排查步骤

- 检查 SQL 语句语法。
- 确认表或字段是否存在。

## 进阶诊断（免费工具推荐）

这种错误往往涉及到复杂的数据库配置或模式问题。你可以使用我们的免费在线手术室进行快速诊断：

![Colab Badge](https://colab.research.google.com/assets/colab-badge.svg)

## 自动化修复建议

想要一键扫描并修复 Postgres 性能与配置问题？

👉 访问 Postgres Surgeon (PostgreSQL 自动化修复专家)
"""
    
    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"已生成 {len(errors)} 个错误代码的 Markdown 文件到 {output_dir} 目录。")
