import os

# 扫描 manual 目录下的所有 .md 文件
manual_dir = './manual'
md_files = [f for f in os.listdir(manual_dir) if f.endswith('.md')]

# 按错误代码排序
md_files.sort()

# 生成 README.md 内容
readme_content = f"""# PostgreSQL Error & Performance Surgery Manual (Open Source Edition)

## 简介
提供一份 Postgres Surgeon 官方维护的错误代码深度解析手册，涵盖 130+ 常见报错。

## 快速工具

| 工具 | 链接 |
|------|------|
| 在线诊断 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/) |
| 一键修复 | [Postgres Surgeon](https://postgressurgeon.wangdadi.xyz) |

## 错误代码索引

"""

# 添加错误代码索引
for md_file in md_files:
    # 提取错误代码
    error_code = md_file.replace('ERR_', '').replace('.md', '')
    # 生成链接
    readme_content += f"- [{error_code}](manual/{md_file})\n"

# 添加 SEO 标签
readme_content += "\n#PostgreSQL #DBA #Database #Optimization #ErrorCodes"

# 写入 README.md 文件
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print(f"已生成 README.md 文件，包含 {len(md_files)} 个错误代码的索引。")
