#!/usr/bin/env python3

import rbdl
import numpy as np 

model = rbdl.loadModel("/home/gabriele/catkin_ws/src/abel_move/scripts/abel_arms_full.urdf")

q = np.zeros (model.q_size)
qdot = np.zeros (model.qdot_size)
qddot = np.zeros (model.qdot_size)
tau = np.zeros (model.qdot_size)

q_res = q

rbdl.InverseKinematics(model, q, np.ones(10), np.zeros(3), np.zeros(3), q_res)
