import os
import glob
import random
import setting

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

if __name__ == '__main__':
    print(get_two_candy())
