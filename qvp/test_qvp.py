""" Unit Tests for Py-ART's retrieve/qvp.py module. """

import numpy as np
from numpy.testing import assert_almost_equal

import pyart


def test_quasi_vertical_profile():
    test_radar = pyart.testing.maske_targer_radar()
    height = np.arange(0, 1000, 200)
    speed = np.ones_like(height) * 5
    direction = np.array([0, 90, 180, 270, 45])
    profile = pyart.core.HorizontalWindProfile(height, speed, direction)
    sim_vel = pyart.util.simulated_vel_from_profile(test_radar, profile)
    test_radar.add_field('velocity', sim_vel, replace_existing=True)

    qvp = pyart.retrieve.quasi_vertical_profile(test_radar)

    qvp_height = [0., 0., 0., 1., 1., 1., 1., 2., 2., 2., 2., 3.,
                  3., 3., 3., 3., 4., 4., 4., 4., 5., 5., 5., 5.,
                  6., 6., 6., 7., 7., 7., 7., 8., 8., 8., 8., 9.,
                  9., 9., 10., 10., 10., 10., 11., 11., 11., 11., 
                  12., 12., 12., 13.]
    
    qvp_range = [ 0., 20.408163, 40.816326, 61.22449, 81.63265, 102.04082, 
                 122.44898, 142.85715, 163.2653, 183.67346, 204.08163, 224.48979, 
                 244.89796, 265.30612, 285.7143, 306.12244, 326.5306, 346.93878, 
                 367.34692, 387.7551, 408.16327, 428.57144, 448.97958, 469.38776, 
                 489.79593, 510.20407, 530.61224, 551.0204, 571.4286, 591.83673,
                 612.2449, 632.6531, 653.0612, 673.46936, 693.87756, 714.2857,
                 734.69385, 755.10205, 775.5102, 795.9184, 816.32654, 836.7347,
                 857.1429, 877.551, 897.95917, 918.3674, 938.7755, 959.18365, 
                 979.59186, 1000]
    
    qvp_reflectivity = [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 10., 10., 10., 
                        10., 10., 10., 10., 10., 10., 10., 20., 20., 20., 20., 20., 20., 
                        20., 20., 20., 20., 30., 30., 30., 30., 30., 30., 30., 30., 30., 
                        30., 40., 40., 40., 40., 40., 40., 40., 40., 40., 40.]
    
    qvp_velocity = [7.448253646563035e-09, 7.448253646563035e-09, 7.448253646563035e-09,
                    7.212727631475402e-09, 7.212727631475402e-09, 7.212727631475402e-09,
                    7.212727631475402e-09, 6.977201207147226e-09, 6.977201207147226e-09,
                    6.977201207147226e-09, 6.977201207147226e-09, 6.741673554133687e-09,
                    6.741673554133687e-09, 6.741673554133687e-09, 6.741673554133687e-09,
                    6.741673554133687e-09, 6.5061473227453115e-09, 6.5061473227453115e-09,
                    6.5061473227453115e-09, 6.5061473227453115e-09, 6.270622495326468e-09,
                    6.270622495326468e-09, 6.270622495326468e-09, 6.270622495326468e-09,
                    6.0350943047028496e-09, 6.0350943047028496e-09, 6.0350943047028496e-09,
                    5.799567182514694e-09, 5.799567182514694e-09, 5.799567182514694e-09,
                    5.799567182514694e-09, 5.5640389605889535e-09, 5.5640389605889535e-09,
                    5.5640389605889535e-09, 5.5640389605889535e-09, 5.328510501969833e-09,
                    5.328510501969833e-09, 5.328510501969833e-09, 5.092988902216039e-09,
                    5.092988902216039e-09, 5.092988902216039e-09, 5.092988902216039e-09,
                    4.857459394590356e-09, 4.857459394590356e-09, 4.857459394590356e-09,
                    4.857459394590356e-09, 4.621931789300988e-09, 4.621931789300988e-09,
                    4.621931789300988e-09, 4.386406373001349e-09]
    
    assert_almost_equal(qvp['height'], qvp_height, 3)
    assert_almost_equal(qvp['range'], qvp_range, 3)
    assert_almost_equal(qvp['reflectivity'], qvp_reflectivity, 3)
    assert_almost_equal(qvp['velocity'], qvp_velocity, 3)