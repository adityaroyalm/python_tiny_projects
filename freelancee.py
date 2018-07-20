# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 18:48:43 2017

@author: aditya royal
"""
all_url=list()
links=list()
i=0
emails=dict()
emails=dict()
from bs4 import BeautifulSoup
r=BeautifulSoup(open('C:/Users/aditya royal/Downloads/NHVTMA.html'),'html.parser')
import email_extrctor
def main():
    email_extrctor.extract_links(r)
    email_extrctor.extract_emails(extract_links(r))
main()
#email_extrctor.unique_emails(extract_emails(links))
if __name__=='__main__':
    import timeit
    print timeit.timeit('extract_links(r,links)', setup='from __main__ import extract_links')
