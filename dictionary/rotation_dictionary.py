import numpy as np
from pyquaternion import Quaternion as Q

cam_rot = {'kitti': {'waymo': Q(axis=[0, 1, 0], angle=np.pi / 2).rotation_matrix @
                              Q(axis=[0, 0, 1], angle=-np.pi / 2).rotation_matrix,
                     'nuscenes': np.eye(3, dtype=np.float32),
                     'udacity': np.eye(3, dtype=np.float32)},
           'waymo': {'kitti': Q(axis=[1, 0, 0], angle=np.pi / 2).rotation_matrix @
                              Q(axis=[0, 0, 1], angle=np.pi / 2).rotation_matrix,
                     'nuscenes': Q(axis=[1, 0, 0], angle=np.pi / 2).rotation_matrix @
                                 Q(axis=[0, 0, 1], angle=np.pi / 2).rotation_matrix,
                     'udacity': np.eye(3, dtype=np.float32)},
           'nuscenes': {'kitti': np.eye(3, dtype=np.float32),
                        'waymo': Q(axis=[0, 1, 0], angle=np.pi / 2).rotation_matrix @
                                 Q(axis=[0, 0, 1], angle=-np.pi / 2).rotation_matrix,
                        'udacity': np.eye(3, dtype=np.float32)}}

lid_rot = {'kitti': {'waymo': np.eye(3, dtype=np.float32),
                     'nuscenes': Q(axis=[0, 0, 1], angle=np.pi / 2).rotation_matrix,
                     'udacity': np.eye(3, dtype=np.float32)},
           'waymo': {'kitti': np.eye(3, dtype=np.float32),
                     'nuscenes': Q(axis=[0, 0, 1], angle=np.pi / 2).rotation_matrix,
                     'udacity': np.eye(3, dtype=np.float32)},
           'nuscenes': {'kitti': Q(axis=[0, 0, 1], angle=-np.pi / 2).rotation_matrix,
                        'waymo': Q(axis=[0, 0, 1], angle=-np.pi / 2).rotation_matrix,
                        'udacity': Q(axis=[0, 0, 1], angle=-np.pi / 2).rotation_matrix}
           }
