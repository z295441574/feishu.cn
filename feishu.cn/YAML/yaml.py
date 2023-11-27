import yaml
import os

def get_yaml_load_all(yaml_name):
    #打开文件
    current_work_dir = os.path.dirname(__file__)  # 当前文件所在的目录
    yaml.warnings({'YAML': False})
    with open(current_work_dir+'\\'+yaml_name, mode="r", encoding="utf-8") as f:# 打开yaml文件
        data = f.read()
    file = yaml.load_all(data, Loader=yaml.FullLoader)
    data=yaml.safe_load(data)
    return data
