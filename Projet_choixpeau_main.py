# coding: utf-8
'''
        ...
'''

from math import sqrt



def k_ppv_algo(profile, profile_data, k=5):
    '''
    '''
    assert profile == dict; profile_data == list; k == int
    distance_dict = {}
    for i in range(len(profile_data)):
        for compared in profile_data:
                distance = ((compared['Courage'] - profile['Courage']) ** 2 + (compared['Ambition'] - profile['Ambition']) ** 2 + (compared['Intelligence'] - profile['Intelligence']) ** 2 + (compared['Good'] - profile['Good']) ** 2) ** 1/2
                distance_dict.update(compared['Name'], distance)

    distance_dict['Name'].sort()
    for j in range(k + 1):
        distance_dict[k] 

    
