import os
import re

# 真实的 Colab 链接
REAL_COLAB_LINK = "https://colab.research.google.com/drive/1InhuP66xl3VIRYOpRlvQXBCsvig0i3x4"

# 要处理的文件路径
FILES_TO_PROCESS = ["./README.md"]

# 添加 manual 目录下的所有 .md 文件
manual_dir = "./manual"
if os.path.exists(manual_dir):
    for filename in os.listdir(manual_dir):
        if filename.endswith(".md"):
            FILES_TO_PROCESS.append(os.path.join(manual_dir, filename))

def replace_colab_links(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换 [你的Colab链接] 占位符
        content = re.sub(r'\[你的Colab链接\]', REAL_COLAB_LINK, content)
        
        # 替换类似的占位符
        content = re.sub(r'\[Colab链接\]', REAL_COLAB_LINK, content)
        
        # 确保 Colab 徽章链接正确
        # 匹配 [![Open In Colab]... 格式
        content = re.sub(
            r'\[!\[Open In Colab\]\([^)]*\)\]\([^)]*\)',
            f'[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({REAL_COLAB_LINK})',
            content
        )
        
        # 匹配 ![Colab Badge]... 格式
        content = re.sub(
            r'!\[Colab Badge\]\([^)]*\)',
            f'[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({REAL_COLAB_LINK})',
            content
        )
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"已处理文件: {file_path}")
        return True
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return False

def main():
    print("开始替换 Colab 链接...")
    
    success_count = 0
    total_count = len(FILES_TO_PROCESS)
    
    for file_path in FILES_TO_PROCESS:
        if os.path.exists(file_path):
            if replace_colab_links(file_path):
                success_count += 1
        else:
            print(f"文件不存在: {file_path}")
    
    print(f"\n替换完成！")
    print(f"处理文件数: {total_count}")
    print(f"成功替换: {success_count}")

if __name__ == "__main__":
    main()