# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 06:47:28 2021

@author: Altair
"""

'''面向对象 模拟铅球轨迹'''
from math import sin, cos, radians
class Projectile:
    def _init_(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yxel = velocity * sin(theta)
    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1)/2.0
        self.yvel = yvel1    
    def getY(self):
        return self.ypos
    def getX(self):
        return self.xpos

def getInputs():
    angle = eval(input("Enter the launch angle (in degrees):"))
    vel = eval(input("Enter the initial velocity (in meters/sec):"))
    h0 = eval(input("Enter the initial height (in meters):"))
    time = eval(input("Enter the time interval:"))
    return angle, vel, h0, time

def main():
    angle, vel, h0, time = getInputs()
    shot = Projectile()
    while shot.getY() >=0:
        shot.update(time)
    print("\nDistance traveled:{0:0.1f} meters".format(shot.getX()))

if __name__ == "__main__":
    main()
