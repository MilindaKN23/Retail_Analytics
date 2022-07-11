import os
import shutil


def place_images_in_folders(images_path):

    if not os.path.exists(images_path + '/train'):
        os.makedirs(images_path + '/train')
    if not os.path.exists(images_path + '/test'):
        os.makedirs(images_path + '/test')
    if not os.path.exists(images_path + '/val'):
        os.makedirs(images_path + '/val')

    for image in os.listdir(images_path):
        if image.startswith('test'):
            shutil.move(images_path + '/' + image, images_path + '/test')
        elif image.startswith('train'):
            shutil.move(images_path + '/' + image, images_path + '/train')
        elif image.startswith('val'):
            shutil.move(images_path + '/' + image, images_path + '/val')
        else:
            print('Image not in test, train or val folder')
            print(image)
            exit()


images_path = "..\Dataset\images"

place_images_in_folders(images_path)
