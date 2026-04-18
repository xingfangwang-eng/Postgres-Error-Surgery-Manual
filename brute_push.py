import os
import subprocess
import time

# 遍历 manual 文件夹下的所有文件
manual_dir = './manual'
files = [os.path.join(manual_dir, f) for f in os.listdir(manual_dir) if os.path.isfile(os.path.join(manual_dir, f))]

# 每 10 个文件一批次
batch_size = 10

# 执行 git 命令的函数
def run_git_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

# 推送函数
def push_batch(batch_files, batch_num):
    # 打印当前批次的文件
    print(f"Files in batch {batch_num}: {batch_files}")
    
    # 检查 Git 状态
    status_code, status_out, status_err = run_git_command('git status')
    print(f"Git status: {status_out}")
    
    # 尝试提交
    commit_cmd = f'git commit -m "Add batch {batch_num} of error code files"'
    print(f"Running: {commit_cmd}")
    commit_code, commit_out, commit_err = run_git_command(commit_cmd)
    if commit_code != 0:
        print(f"Batch {batch_num} Git commit failed: {commit_err}")
        # 如果是因为没有新文件，跳过
        if "nothing to commit" in commit_err:
            print("No new files to commit, skipping...")
            return True
        return False
    else:
        print(f"Batch {batch_num} Git commit succeeded: {commit_out}")
    
    # Git push with retry
    for attempt in range(3):
        push_cmd = 'git push origin main'
        print(f"Running: {push_cmd} (Attempt {attempt + 1})")
        push_code, push_out, push_err = run_git_command(push_cmd)
        if push_code == 0:
            print(f"Batch {batch_num} Git push succeeded on attempt {attempt + 1}")
            return True
        else:
            print(f"Batch {batch_num} Git push failed on attempt {attempt + 1}: {push_err}")
            if attempt < 2:
                print("Retrying in 5 seconds...")
                time.sleep(5)
    
    print(f"Batch {batch_num} Git push failed after 3 attempts")
    return False

# 分批处理
for i in range(0, len(files), batch_size):
    batch_files = files[i:i+batch_size]
    batch_num = i // batch_size + 1
    print(f"\n=== Processing batch {batch_num} with {len(batch_files)} files ===")
    success = push_batch(batch_files, batch_num)
    if success:
        print(f"Batch {batch_num} processed successfully")
    else:
        print(f"Batch {batch_num} processing failed")
    print("\n")

print("All batches processed")
