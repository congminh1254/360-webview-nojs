import pytest
import cv2
import numpy as np
from managers.Equirec2Perspec import xyz2lonlat, lonlat2XY, Equirectangular

def test_xyz2lonlat():
    xyz = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) 
    expected_output = np.array([[np.pi/2, 0], [0, np.pi/2], [0, 0]])

    result = xyz2lonlat(xyz)
    np.testing.assert_almost_equal(result, expected_output)


def test_lonlat2XY():
    lonlat = np.array([[np.pi/2, 0], [0, np.pi/2], [0, 0]]) 

    shape = (100, 200) 
    expected_output = np.array([[150, 49], [99, 99], [99, 50]])

    result = lonlat2XY(lonlat, shape)
    np.testing.assert_almost_equal(result, expected_output, 0)
    