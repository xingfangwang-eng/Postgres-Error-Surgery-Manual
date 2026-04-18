import subprocess
import time

# 执行 git 命令的函数
def run_git_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

# 推送所有文件
def push_all():
    # 添加所有文件
    add_cmd = 'git add .'
    print(f"Running: {add_cmd}")
    add_code, add_out, add_err = run_git_command(add_cmd)
    if add_code != 0:
        print(f"Git add failed: {add_err}")
        return False
    else:
        print("Git add succeeded")
    
    # 提交所有文件
    commit_cmd = 'git commit -m "Add all error code files and README"'
    print(f"Running: {commit_cmd}")
    commit_code, commit_out, commit_err = run_git_command(commit_cmd)
    if commit_code != 0:
        print(f"Git commit failed: {commit_err}")
        return False
    else:
        print(f"Git commit succeeded: {commit_out}")
    
    # 推送所有文件
    for attempt in range(3):
        push_cmd = 'git push origin main'
        print(f"Running: {push_cmd} (Attempt {attempt + 1})")
        push_code, push_out, push_err = run_git_command(push_cmd)
        if push_code == 0:
            print(f"Git push succeeded on attempt {attempt + 1}")
            return True
        else:
            print(f"Git push failed on attempt {attempt + 1}: {push_err}")
            if attempt < 2:
                print("Retrying in 5 seconds...")
                time.sleep(5)
    
    print("Git push failed after 3 attempts")
    return False

# 执行推送
if push_all():
    print("All files pushed successfully")
else:
    print("Failed to push files")
