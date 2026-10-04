###############################  read me  #####################################

#用于 labelme生成的数据格式 转 coco格式

#运行代码后将会提示输入  输入路径  输出路径

###############################################################################
import json
import os
import glob
from tqdm import tqdm

inputpath=input("输入读取的json文件路径： ")
outputpath=input("输入 输出的文件路径： ")
def labelme2coco(labelme_json_dir, save_json_path, img_suffix='.jpg'):
    # 1. 初始化 COCO 结构
    coco = {
        "images": [],
        "annotations": [],
        "categories": []
    }

    # 2. 读取所有 Labelme JSON
    json_files = glob.glob(os.path.join(labelme_json_dir, '*.json'))
    if not json_files:
        raise Exception(f"未找到 JSON 文件：{labelme_json_dir}")

    # 3. 类别映射（自动收集）
    categories = {}
    ann_id = 1

    for json_file in tqdm(json_files, desc="转换中"):
        # 读取 Labelme JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 图片信息
        img_name = data['imagePath']
        img_id = len(coco['images']) + 1
        img_info = {
            "id": img_id,
            "file_name": img_name,
            "height": data['imageHeight'],
            "width": data['imageWidth']
        }
        coco['images'].append(img_info)

        # 标注信息
        for shape in data['shapes']:
            label = shape['label']
            points = shape['points']

            # 收集类别
            if label not in categories:
                categories[label] = len(categories) + 1
                coco['categories'].append({
                    "id": categories[label],
                    "name": label,
                    "supercategory": "none"
                })

            # 计算 bbox
            x = [p[0] for p in points]
            y = [p[1] for p in points]
            bbox = [min(x), min(y), max(x)-min(x), max(y)-min(y)]

            # 计算 area
            area = bbox[2] * bbox[3]

            # 标注
            ann = {
                "id": ann_id,
                "image_id": img_id,
                "category_id": categories[label],
                "bbox": bbox,
                "area": area,
                "iscrowd": 0
            }
            coco['annotations'].append(ann)
            ann_id += 1

    # 4. 保存 COCO JSON
    with open(save_json_path, 'w', encoding='utf-8') as f:
        json.dump(coco, f, ensure_ascii=False, indent=4)

    print(f"转换完成！保存到：{save_json_path}")
    print(f"类别：{list(categories.keys())}")

# ====================== 你只需要改这里 ======================
if __name__ == '__main__':
    # Labelme JSON 所在文件夹
    LABELME_JSON_DIR = inputpath
    # 输出 COCO JSON 路径
    SAVE_JSON_PATH = outputpath

    labelme2coco(LABELME_JSON_DIR, SAVE_JSON_PATH)