import os
from glob import glob

import cv2
from easydict import EasyDict as edict
import json
import sys
sys.path.append('../../')

def get_file_name(data_path):
    fn_list = []
    addrs = glob(os.path.join(data_path + '/' + '*.jpg'))

    for addr in addrs:
        fn = os.path.basename(addr)
        fn_list.append(fn)

    return fn_list

def filename():
    configs = edict()

    configs.working_dir = '/home/ankhzaya/Desktop/extract_images_gait_events/'
    configs.datasets_dir = os.path.join(configs.working_dir, 'images/')

    subjects = ['S19']
    cameras = ['C12']
    act_names = ['WalkingAround']
    act_orders = ['1']

    for sbj in subjects:
        for cmr in cameras:
            for act_name in act_names:
                for act_order in act_orders:
                    images_dir = os.path.join(configs.datasets_dir, sbj, act_name + '{}'.format(act_order), cmr)
                    #print('images_dir: {}'.format(images_dir))

                    if not os.path.isdir(images_dir):
                        print('No dir: {} !!!'.format(os.path.basename(images_dir)))
                    else:
                        filename_list = get_file_name(images_dir)

    #print('len(finame_list): {}'.format(len(filename_list)))
    #print('example of filename: {}'.format(filename_list[4]))

    return images_dir, filename_list

if __name__ == '__main__':
    filename()