#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Author : Ayden Lee
    Date   : 11/09/2020
    Desc   :
    Change LOG :

"""
class Course:
    def __init__(self,name,price,period,teacher):
        self.name=name
        self.price=price
        self.period=period
        self.teacher=teacher
class Student:
    def __init__(self,name):
        self.name=name

    def show_course(self):
        print('查看所有课程')

    def select_course(self):
        print('选择课程')

    def check_selected_cource(self):
        print('查看已选课程')

    def exit(self):
        exit()

class Manager:
    operate_1st=['create_course',
                 'create_student',
                 'show_cource',
                 'show_student',
                 'show_student_course',
                 'exit']
    def __init__(self,name):
        self.name=name

    def create_course(self):
        print('创建课程')

    def create_student(self):
        print('创建学生')

    def show_cource(self):
        print('查看所有课程')

    def show_student(self):
        print('查看所有学生')

    def show_student_course(self):
        print('查看所有学生的选课情况')

    def exit(self):
        exit()



def login():
    name=input('username:')
    pawd=input('password:')
    with open('userinfo',encoding='utf-8') as f:
        for line in f:
            usr,pwd,identify=line.strip().split('>=')
            if usr==name and pwd==pawd:
                return {'result':True,'name':name,'id':identify}
            else:
                return {'result':False,'name':name}
ret=login()
if ret['result']:
    print('登录成功')
    if ret['id'] == 'Manager':
        obj=Manager(ret['name'])
        for id,item in enumerate(obj.operate_1st,1):
            print(id,item)
else:
    print('登录失败')
