# 文件结构

project_root/          # 项目根目录

├── backend/           # 后端主模块（组长 A 负责的核心后端）

│   ├── `__init__`.py    # 标记为 Python 包

│   ├── main.py        # 后端主程序（如 Flask/Django 的启动入口）

│   ├── database/      # 数据库相关代码（A 的任务：设计数据库）

│   ├── api/           # 接口设计代码（A 的任务：设计接口）

│   └── deployment/    # 部署环境相关代码（A 的任务：部署环境）

├── vision_module/     # 成员 B：计算机视觉模块

│   ├── `__init__`.py    # 标记为 Python 包

│   ├── detection/     # 顾客检测代码

│   ├── recognition/   # 商品识别代码

│   └── behavior/      # 行为识别代码

├── frontend_module/   # 成员 C：前端模块（注：若前端是前端技术栈，此为“前端资源的后端管理”或“前后端交互层”）

│   ├── `__init__`.py

│   ├── web_ui/        # 前端界面相关的后端配置（如模板、静态文件管理）

│   └── admin_panel/   # 管理后台的后端交互逻辑

└── llm_voice_module/  # 成员 D：LLM + 语音交互模块

​    ├── `__init__`.py

​    ├── speech_recog/  # 语音识别代码

​    ├── llm_integration/ # 大语言模型接入代码

​    └── chat_recommend/  # 智能客服与推荐代码



# 创建文件脚本

```python
import os

def create_project_structure():
    """创建指定的项目文件结构"""
    # 项目根目录
    root_dir = "SmartStore_01"
    os.makedirs(root_dir, exist_ok=True)
    print(f"创建项目根目录: {root_dir}")

    # 定义项目结构
    structure = {
        # 后端主模块（组长A负责）
        f"{root_dir}/backend": [
            "__init__.py",
            "main.py",
            {
                "database/": [],  # 数据库相关代码
                "api/": [],       # 接口设计代码
                "deployment/": [] # 部署环境相关代码
            }
        ],
        
        # 计算机视觉模块（成员B负责）
        f"{root_dir}/vision_module": [
            "__init__.py",
            {
                "detection/": [],    # 顾客检测代码
                "recognition/": [],  # 商品识别代码
                "behavior/": []      # 行为识别代码
            }
        ],
        
        # 前端模块（成员C负责）
        f"{root_dir}/frontend_module": [
            "__init__.py",
            {
                "web_ui/": [],        # 前端界面相关的后端配置
                "admin_panel/": []    # 管理后台的后端交互逻辑
            }
        ],
        
        # LLM + 语音交互模块（成员D负责）
        f"{root_dir}/llm_voice_module": [
            "__init__.py",
            {
                "speech_recog/": [],      # 语音识别代码
                "llm_integration/": [],   # 大语言模型接入代码
                "chat_recommend/": []     # 智能客服与推荐代码
            }
        ]
    }

    def create_structure(base_path, items):
        """递归创建目录和文件"""
        for item in items:
            if isinstance(item, dict):
                # 处理子目录
                for dir_name, sub_items in item.items():
                    dir_path = os.path.join(base_path, dir_name)
                    os.makedirs(dir_path, exist_ok=True)
                    print(f"创建目录: {dir_path}")
                    # 在每个子目录中添加__init__.py文件
                    init_file = os.path.join(dir_path, "__init__.py")
                    if not os.path.exists(init_file):
                        with open(init_file, 'w', encoding='utf-8') as f:
                            f.write(f"# {dir_name[:-1]} 模块初始化\n")
                        print(f"创建文件: {init_file}")
                    # 递归处理子项目
                    if sub_items:
                        create_structure(dir_path, sub_items)
            else:
                # 处理文件
                file_path = os.path.join(base_path, item)
                if not os.path.exists(file_path):
                    with open(file_path, 'w', encoding='utf-8') as f:
                        if item == "main.py":
                            # 添加Flask启动代码模板
                            f.write("""from flask import Flask
from backend.api import bp as api_bp
import os

app = Flask(
    __name__,
    static_folder="../../frontend_module/web_ui/static",
    template_folder="../../frontend_module/web_ui/templates"
)

# 注册蓝图
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    return "Smart Store Backend is running!"

if __name__ == '__main__':
    app.run(debug=True)
""")
                        elif item == "__init__.py":
                            # 添加模块初始化注释
                            module_name = os.path.basename(base_path)
                            f.write(f"# {module_name} 模块初始化\n")
                print(f"创建文件: {file_path}")

    # 遍历结构并创建
    for base_path, items in structure.items():
        os.makedirs(base_path, exist_ok=True)
        print(f"创建目录: {base_path}")
        create_structure(base_path, items)

    # 创建项目根目录下的必要文件
    root_files = [
        "requirements.txt",
        "README.md",
        ".gitignore"
    ]
    for file in root_files:
        file_path = os.path.join(root_dir, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                if file == "requirements.txt":
                    f.write("flask==2.3.3\n")
                    f.write("opencv-python==4.9.0.80\n")
                    f.write("transformers==4.35.2\n")
                    f.write("pymysql==1.1.1\n")
                elif file == "README.md":
                    f.write("# 智能商店系统\n\n")
                    f.write("## 项目结构\n")
                    f.write("- backend: 后端主模块（组长A负责）\n")
                    f.write("- vision_module: 计算机视觉模块（成员B负责）\n")
                    f.write("- frontend_module: 前端模块（成员C负责）\n")
                    f.write("- llm_voice_module: LLM+语音交互模块（成员D负责）\n")
                elif file == ".gitignore":
                    f.write("__pycache__/\n")
                    f.write("venv/\n")
                    f.write(".env\n")
                    f.write("*.pyc\n")
            print(f"创建文件: {file_path}")

    print(f"\n项目结构创建完成！根目录: {os.path.abspath(root_dir)}")

if __name__ == "__main__":
    create_project_structure()
    
```

