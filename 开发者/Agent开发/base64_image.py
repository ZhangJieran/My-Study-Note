#将图片转换成 Base64 编码的 Data URI 字符串



def encode_image(img_path,img_type='jpg'):
    #适配content
    with open(img_path,"rb") as img_file:
        return f"data:image/{img_type};base64,{base64.b64encode(img_file.read()).decode("utf-8")}"



def encode_image(img_path,img_type='jpg'):
    #适配content_blocks
    with open(img_path,"rb") as img_file:
        return f"{base64.b64encode(img_file.read()).decode("utf-8")}"