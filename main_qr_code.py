# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 18:11:22 2019

@author: PeerapongE
"""


import qrcode

# Test#1
link_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdwRhT8BRvdbnw4CYPncbAf3Q1MmnzoQoFp5xq3zqFoCufKAg/viewform'
file_output = 'qr_code.jpg'

# Test#2
# =============================================================================
# link_url    = 'https://drive.google.com/drive/folders/18wBM3CiXzbJCZ3wgBb5DlX2_KpCbgD_D'
# file_output = 'qr_code_sql_training.jpg'
# =============================================================================



img = qrcode.make(link_url)
img.save(file_output)
