import os
import glob
import random
import pathlib
import sys
import torch
DIR = pathlib.Path(__file__)
sys.path.append(DIR.parents[2])
from test_webapp import setting
from test_webapp.modules.ego.stimulation import shape


# キャンディの画像のパスのリストを返す関数
# 引数は個数、返り値はリスト型
# 引数のデフォルトは2
def get_two_candy(number=2) -> list:
    images: list = glob.glob(os.path.join(setting.CANDY_DIR, "*.jpg"))
    choice_images: list = random.sample(images, number)
    fix_images: list = []
    for choice_image in choice_images:
        fix_images.append(os.path.join(setting.CANDY_RELATIVE_PREFIX,
                                       os.path.basename(choice_image)))
    return fix_images


def sum_number(number):
    return number + 1


def shiroshita_system():
    count_num:int = 1
    LOOP_NUM = 100
    RANDOM_NUM = 80
    bounds = torch.Tensor([[-1, -0.5, -0.25, -0.125, -1, -0.5, -0.25, -0.125], [1, 0.5, 0.25, 0.125, 1, 0.5, 0.25, 0.125]])
    path1 = "001.jpg"
    path2 = "002.jpg"
    result = []
    response = []

    #76
    if count_num >= RANDOM_NUM:
       gallary = random_gallery(bounds)
    else: 
        gallery = acquisition_gallery(result, response, bounds)
        image_create_ellipse_fourier(path1, gallery[0], result)
        image_create_ellipse_fourier(path2, gallery[1], result)
    valType = "extendedCode"
    #80
    result = torch.Tensor(result).reshape(-1, len(bounds[0]))
    response = torch.Tensor(response).reshape(-1, 2)
    result_save_name = filename + '_result.pt'
    response_save_name = filename + '_response.pt'
    torch.save(result, result_save_name)
    torch.save(response, response_save_name)
    valType = "extendedCode"
    #83
    '''
    if count_num >= LOOP_NUM && key_resp_1.keys == None && mouse.clicked_name == image_1:
       response.append(len(result)-2)
       response.append(len(result)-1)
    else:
        response.append(len(result)-1)
        response.append(len(result)-2)
    else:
    if key_resp_1.keys == '1':
        response.append(len(result)-2)
        response.append(len(result)-1)
    else: 
        response.append(len(result)-1)
        response.append(len(result)-2)
        count_num += 1
    valType = "extendedCode"
    '''


def s_system(input_array: list):
    count_num: int = 1
    loop_num: int = 100
    random_num: int = 80
    bounds: torch.Tensor = torch.Tensor([
        [-1, -0.5, -0.25, -0.125, -1, -0.5, -0.25, -0.125],
        [1, 0.5, 0.25, 0.125, 1, 0.5, 0.25, 0.125]])
    path1: str = "001.jpg"
    path2: str = "002.jpg"

    result: list = []
    response: list = []

    if count_num >= random_num:
        gallary: list = shape.random_gallery(bounds)
    else:
        gallery = shape.acquisition_gallery(result, response, bounds)
        shape.image_create_ellipse_fourier(path1, gallery[0], result)
        shape.image_create_ellipse_fourier(path2, gallery[1], result)
    result: torch.Tensor = torch.Tensor(result).reshape(-1, len(bounds[0]))
    response: torch.Tensor = torch.Tensor(response).reshape(-1, 2)
    print(result)
    print(response)


if __name__ == '__main__':
    # s_system([1, 1])
    for i in sys.path:
        print(i)