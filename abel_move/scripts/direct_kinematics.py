import pinocchio

def direct_kinematics():
        """
        Compute the direct kinematics for left and right hand (end-effector) by using the URDF model
        """
        model = pinocchio.buildModelsFromUrdf("/home/gabriele/catkin_ws/src/abel_move/scripts/abel_arms_full.urdf") 
        
        # Create data required by the algorithms
        model, collision_model, visual_model = pinocchio.buildModelsFromUrdf("/home/gabriele/catkin_ws/src/abel_move/scripts/abel_arms_full.urdf")
        data, collision_data, visual_data  = pinocchio.createDatas(model, collision_model, visual_model)

        #q = self.abel.joint_states_msg.position[5:14]
        #q = np.asarray(q)

        q = pinocchio.neutral(model)

        pinocchio.forwardKinematics(model,data,q)

        for name, oMi in zip(model.names, data.oMi):
            print(("{:<24} : {: .2f} {: .2f} {: .2f}".format( name, *oMi.translation.T.flat )))

direct_kinematics()