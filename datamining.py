# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:59:19 2018

@author: aditya royal
"""
import dicom
plan=dicom.read_file('D:/lung cancer/sample_images/00cba091fa4ad62cc3200a657aeb957e/0af07f64d14d6b0451036cc742a96fbf.dcm')
print(plan)
(0020, 000d) Study Instance UID                  UI: 2.25.86208730140539712382771890501772734277950692397709007305473
(0020, 000e) Series Instance UID                 UI: 2.25.11575877329635228925808596800269974740893519451784626046614