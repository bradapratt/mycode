#!/usr/bin/env python3
import shutil
import os

#change the working directory
os.chdir('/home/student/mycode/')

#move file into directory. leave the file name as is. it will replace a file of the same name if it exists already.
shutil.move('raynor.obj', 'ceph_storage/')
xname = input('What is the new name for kerrigan.obj? ')

#move file into directory with a new name
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

