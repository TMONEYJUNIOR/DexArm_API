from pydexarm import Dexarm
import time

'''windows'''
dexarm = Dexarm(port="COM10")
'''mac & linux'''
# device = Dexarm(port="/dev/tty.usbmodem3086337A34381")

dexarm.go_home()
'''Starting position is 0,300,0'''
'''Max range for Y is 186-413'''
'''Max range for Z is -125 167'''
'''Max range for X is -280 325'''

dexarm.move_to(-250,410,0)
dexarm.move_to(325,413,0)


dexarm.go_home()

'''DexArm sliding rail Demo'''
'''
dexarm.conveyor_belt_forward(2000)
time.sleep(20)
dexarm.conveyor_belt_backward(2000)
time.sleep(10)
dexarm.conveyor_belt_stop()
'''

'''DexArm sliding rail Demo'''
'''
dexarm.go_home()
dexarm.sliding_rail_init()
dexarm.move_to(None,None,None,0)
dexarm.move_to(None,None,None,100)
dexarm.move_to(None,None,None,50)
dexarm.move_to(None,None,None,200)
'''
dexarm.close()