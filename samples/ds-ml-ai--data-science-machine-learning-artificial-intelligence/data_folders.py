import os

from glob import glob, iglob

folder_root='../../../../../data/images/'

folders_with_images = [
                        f"{folder_root}/",
                        f"/Volumes/pics-imgs-5/pics/Pixel 6/20260313/pictures/Screenshots/ai/",
                        f"/Volumes/pics-imgs-5/pics/Pixel 6/20260313/pictures/Screenshots/personal/",
                    ]


# https://www.geeksforgeeks.org/python/python-list-all-files-in-directory-and-subdirectories/
# https://www.geeksforgeeks.org/python/how-to-use-glob-function-to-find-files-recursively-in-python/
# https://stackoverflow.com/questions/18394147/how-to-do-a-recursive-sub-folder-search-and-return-files-in-a-list

files_images = []

for folder in folders_with_images:

    if not os.path.exists(folder):
        print(f"Folder does not exist: {folder}")
        continue

    files_images_png = \
        [ iglob(os.path.join(folder_root, '**', '*.[pP][nN][gG]'), recursive=True) ]

    files_images_jpg = \
        [ iglob(os.path.join(folder_root, '**', '*.[jJ][pP][gG]'), recursive=True) ]

    files_images_jpeg = \
        [ iglob(os.path.join(folder_root, '**', '*.[jJ][pP][eE][gG]'), recursive=True) ]

    files_images_loop = \
                        files_images_jpeg \
                        + \
                        files_images_jpg \
                        + \
                        files_images_png
    files_images += files_images_loop

import os
result_1 = [os.path.join(folder_path, file) \
                for folder_path, folder_name, filenames in os.walk(folder_root) \
                for file in filenames if os.path.splitext(file)[1] == '.png' \
            ]


from glob import glob, iglob

result_2 = [y \
            for x in os.walk(folder_root) \
            for y in glob(os.path.join(x[0], '*.png')) \
            ]

from itertools import chain
result_3 = (chain.from_iterable(glob(os.path.join(x[0], '*.png')) for x in os.walk(folder_root)))


result_4 = iglob(os.path.join(folder_root, '**', '*.[pP][nN][gG]'), recursive=True)

result_5 = glob(folder_root + '/**/*.png', recursive=True)

# print("result_1")
# print(result_1)
# print("result_2")
# print(result_2)
# print("result_3")
# print(list(result_3))
# print("result_4")
# print(list(result_4))
# print("result_5")
# print(result_5)