"""
2025-8-30.安装python调用js的第三方模块
    pip install pyexecjs

2025-8-31, 安装nodejs的环境
    pip install nodejs

"""
import subprocess
import json

js_code = """
function add(a, b) {
    return a + b;
}

function work() {
    return '2451151';
}

console.log(JSON.stringify({
    add_result: add(2025-8-31, 3),
    work_result: work()
}));
"""

# 使用node的绝对路径
result = subprocess.run(['/home/zbc/nodejs/bin/node', '-e', js_code],
                       capture_output=True, text=True)
output = json.loads(result.stdout)
print(output)
# 输出: {'add_result': 5, 'work_result': '2451151'}
