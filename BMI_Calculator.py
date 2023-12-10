#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:29:58 2023

Title: BMI Calculator

@author: nicosidari

BMI = (weight in pounds x 703) / (height in inches x height in inches)
"""
#%%
def BMI_Calc():
    Name = input("Enter Your Name: ")

    Weight = int(input("Enter Your Weight in Pounds: "))

    Height = int(input("Enter Your Height in Inches: "))

    BMI = (Weight * 703) / (Height * Height)

    print("BMI =", BMI)

    if BMI > 0:
        if (BMI < 18.5):
            print(Name + ", You Are Underweight")
        elif (BMI <= 24.9):
            print(Name + ", You Are at a Normal Weight")
        elif (BMI <= 29.9):
            print(Name + ", You Are Overweight")
        elif (BMI <= 34.9):
            print(Name + ", You Are Obese")
        elif (BMI <= 39.9):
            print(Name + ", You Are Severely Obese")
        else:
            print(Name + ", You Are Morbidly Obese")
    else:
        print("Enter a Valid Input")

BMI_Calc()
        
