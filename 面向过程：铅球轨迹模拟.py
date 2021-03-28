# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 05:11:00 2021

@author: Altair
"""

'''模拟铅球的运动轨迹（不考虑空气阻力)'''

angle = eval(input("Enter the launch angle (in degrees):"))
vel = eval(input("Enter the initial velocity (in meters/sec):"))
h0 = eval(input("Enter the initial height (in meters):"))
time = eval(input("Enter the time interval:"))

from math import pi, sin, cos, radians
xpos = 0
ypos = h0
theta = radians(angle)
xvel = vel * cos(theta)
yvel = vel * sin(theta)

while ypos >= 0.0:
    xpos = xpos + time*xvel
    yvel1 = yvel - time*9.8
    ypos = ypos + time*(yvel + yvel1)/2.0
    yvel = yvel1

print("\nDistance traveled: {0:0.1f}meters.".format(xpos))



'''将程序模块化'''
def getInputs():
    angle = eval(input("Enter the launch angle (in degrees):"))
    vel = eval(input("Enter the initial velocity (in meters/sec):"))
    h0 = eval(input("Enter the initial height (in meters):"))
    time = eval(input("Enter the time interval:"))
    return angle, vel, h0, time

from math import pi, sin, cos, radians
def getXYComponents(vel, angle):
    theta = radians(angle)
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    return xvel, yvel

def updatePosition(time, xpos, ypos, xvel, yvel):
    xpos = xpos + time*xvel
    yvel1 = yvel - time*9.8
    ypos = ypos + time*(yvel + yvel1)/2.0
    yvel = yvel1
    return xpos, ypos, yvel

def main():
    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos >= 0:
        xpos, ypos, yvel = updatePosition(time, xpos, ypos, xvel, yvel)
    print("\nDistance traveled: {0:0.1f}meters.".format(xpos))