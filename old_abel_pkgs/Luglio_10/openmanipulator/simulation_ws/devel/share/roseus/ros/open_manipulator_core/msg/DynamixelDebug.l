;; Auto-generated. Do not edit!


(when (boundp 'open_manipulator_core::DynamixelDebug)
  (if (not (find-package "OPEN_MANIPULATOR_CORE"))
    (make-package "OPEN_MANIPULATOR_CORE"))
  (shadow 'DynamixelDebug (find-package "OPEN_MANIPULATOR_CORE")))
(unless (find-package "OPEN_MANIPULATOR_CORE::DYNAMIXELDEBUG")
  (make-package "OPEN_MANIPULATOR_CORE::DYNAMIXELDEBUG"))

(in-package "ROS")
;;//! \htmlinclude DynamixelDebug.msg.html


(defclass open_manipulator_core::DynamixelDebug
  :super ros::object
  :slots (_dxl_id _present_temp _present_load _present_volt _present_current _present_pos _present_vel _goal_pos _goal_vel _return_delay_time _feedforward_1st_gain _feedforward_2nd_gain _error_status _temp_limit _pos_p_gain _pos_i_gain _pos_d_gain _vel_p_gain _vel_i_gain ))

(defmethod open_manipulator_core::DynamixelDebug
  (:init
   (&key
    ((:dxl_id __dxl_id) (make-array 0 :initial-element 0 :element-type :integer))
    ((:present_temp __present_temp) (make-array 0 :initial-element 0 :element-type :integer))
    ((:present_load __present_load) (make-array 0 :initial-element 0 :element-type :integer))
    ((:present_volt __present_volt) (make-array 0 :initial-element 0 :element-type :integer))
    ((:present_current __present_current) (make-array 0 :initial-element 0 :element-type :integer))
    ((:present_pos __present_pos) (make-array 0 :initial-element 0 :element-type :integer))
    ((:present_vel __present_vel) (make-array 0 :initial-element 0 :element-type :integer))
    ((:goal_pos __goal_pos) (make-array 0 :initial-element 0 :element-type :integer))
    ((:goal_vel __goal_vel) (make-array 0 :initial-element 0 :element-type :integer))
    ((:return_delay_time __return_delay_time) (make-array 0 :initial-element 0 :element-type :integer))
    ((:feedforward_1st_gain __feedforward_1st_gain) (make-array 0 :initial-element 0 :element-type :integer))
    ((:feedforward_2nd_gain __feedforward_2nd_gain) (make-array 0 :initial-element 0 :element-type :integer))
    ((:error_status __error_status) (make-array 0 :initial-element 0 :element-type :integer))
    ((:temp_limit __temp_limit) (make-array 0 :initial-element 0 :element-type :integer))
    ((:pos_p_gain __pos_p_gain) (make-array 0 :initial-element 0 :element-type :integer))
    ((:pos_i_gain __pos_i_gain) (make-array 0 :initial-element 0 :element-type :integer))
    ((:pos_d_gain __pos_d_gain) (make-array 0 :initial-element 0 :element-type :integer))
    ((:vel_p_gain __vel_p_gain) (make-array 0 :initial-element 0 :element-type :integer))
    ((:vel_i_gain __vel_i_gain) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _dxl_id __dxl_id)
   (setq _present_temp __present_temp)
   (setq _present_load __present_load)
   (setq _present_volt __present_volt)
   (setq _present_current __present_current)
   (setq _present_pos __present_pos)
   (setq _present_vel __present_vel)
   (setq _goal_pos __goal_pos)
   (setq _goal_vel __goal_vel)
   (setq _return_delay_time __return_delay_time)
   (setq _feedforward_1st_gain __feedforward_1st_gain)
   (setq _feedforward_2nd_gain __feedforward_2nd_gain)
   (setq _error_status __error_status)
   (setq _temp_limit __temp_limit)
   (setq _pos_p_gain __pos_p_gain)
   (setq _pos_i_gain __pos_i_gain)
   (setq _pos_d_gain __pos_d_gain)
   (setq _vel_p_gain __vel_p_gain)
   (setq _vel_i_gain __vel_i_gain)
   self)
  (:dxl_id
   (&optional __dxl_id)
   (if __dxl_id (setq _dxl_id __dxl_id)) _dxl_id)
  (:present_temp
   (&optional __present_temp)
   (if __present_temp (setq _present_temp __present_temp)) _present_temp)
  (:present_load
   (&optional __present_load)
   (if __present_load (setq _present_load __present_load)) _present_load)
  (:present_volt
   (&optional __present_volt)
   (if __present_volt (setq _present_volt __present_volt)) _present_volt)
  (:present_current
   (&optional __present_current)
   (if __present_current (setq _present_current __present_current)) _present_current)
  (:present_pos
   (&optional __present_pos)
   (if __present_pos (setq _present_pos __present_pos)) _present_pos)
  (:present_vel
   (&optional __present_vel)
   (if __present_vel (setq _present_vel __present_vel)) _present_vel)
  (:goal_pos
   (&optional __goal_pos)
   (if __goal_pos (setq _goal_pos __goal_pos)) _goal_pos)
  (:goal_vel
   (&optional __goal_vel)
   (if __goal_vel (setq _goal_vel __goal_vel)) _goal_vel)
  (:return_delay_time
   (&optional __return_delay_time)
   (if __return_delay_time (setq _return_delay_time __return_delay_time)) _return_delay_time)
  (:feedforward_1st_gain
   (&optional __feedforward_1st_gain)
   (if __feedforward_1st_gain (setq _feedforward_1st_gain __feedforward_1st_gain)) _feedforward_1st_gain)
  (:feedforward_2nd_gain
   (&optional __feedforward_2nd_gain)
   (if __feedforward_2nd_gain (setq _feedforward_2nd_gain __feedforward_2nd_gain)) _feedforward_2nd_gain)
  (:error_status
   (&optional __error_status)
   (if __error_status (setq _error_status __error_status)) _error_status)
  (:temp_limit
   (&optional __temp_limit)
   (if __temp_limit (setq _temp_limit __temp_limit)) _temp_limit)
  (:pos_p_gain
   (&optional __pos_p_gain)
   (if __pos_p_gain (setq _pos_p_gain __pos_p_gain)) _pos_p_gain)
  (:pos_i_gain
   (&optional __pos_i_gain)
   (if __pos_i_gain (setq _pos_i_gain __pos_i_gain)) _pos_i_gain)
  (:pos_d_gain
   (&optional __pos_d_gain)
   (if __pos_d_gain (setq _pos_d_gain __pos_d_gain)) _pos_d_gain)
  (:vel_p_gain
   (&optional __vel_p_gain)
   (if __vel_p_gain (setq _vel_p_gain __vel_p_gain)) _vel_p_gain)
  (:vel_i_gain
   (&optional __vel_i_gain)
   (if __vel_i_gain (setq _vel_i_gain __vel_i_gain)) _vel_i_gain)
  (:serialization-length
   ()
   (+
    ;; int32[] _dxl_id
    (* 4    (length _dxl_id)) 4
    ;; int32[] _present_temp
    (* 4    (length _present_temp)) 4
    ;; int32[] _present_load
    (* 4    (length _present_load)) 4
    ;; int32[] _present_volt
    (* 4    (length _present_volt)) 4
    ;; int32[] _present_current
    (* 4    (length _present_current)) 4
    ;; int32[] _present_pos
    (* 4    (length _present_pos)) 4
    ;; int32[] _present_vel
    (* 4    (length _present_vel)) 4
    ;; int32[] _goal_pos
    (* 4    (length _goal_pos)) 4
    ;; int32[] _goal_vel
    (* 4    (length _goal_vel)) 4
    ;; int32[] _return_delay_time
    (* 4    (length _return_delay_time)) 4
    ;; int32[] _feedforward_1st_gain
    (* 4    (length _feedforward_1st_gain)) 4
    ;; int32[] _feedforward_2nd_gain
    (* 4    (length _feedforward_2nd_gain)) 4
    ;; int32[] _error_status
    (* 4    (length _error_status)) 4
    ;; int32[] _temp_limit
    (* 4    (length _temp_limit)) 4
    ;; int32[] _pos_p_gain
    (* 4    (length _pos_p_gain)) 4
    ;; int32[] _pos_i_gain
    (* 4    (length _pos_i_gain)) 4
    ;; int32[] _pos_d_gain
    (* 4    (length _pos_d_gain)) 4
    ;; int32[] _vel_p_gain
    (* 4    (length _vel_p_gain)) 4
    ;; int32[] _vel_i_gain
    (* 4    (length _vel_i_gain)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _dxl_id
     (write-long (length _dxl_id) s)
     (dotimes (i (length _dxl_id))
       (write-long (elt _dxl_id i) s)
       )
     ;; int32[] _present_temp
     (write-long (length _present_temp) s)
     (dotimes (i (length _present_temp))
       (write-long (elt _present_temp i) s)
       )
     ;; int32[] _present_load
     (write-long (length _present_load) s)
     (dotimes (i (length _present_load))
       (write-long (elt _present_load i) s)
       )
     ;; int32[] _present_volt
     (write-long (length _present_volt) s)
     (dotimes (i (length _present_volt))
       (write-long (elt _present_volt i) s)
       )
     ;; int32[] _present_current
     (write-long (length _present_current) s)
     (dotimes (i (length _present_current))
       (write-long (elt _present_current i) s)
       )
     ;; int32[] _present_pos
     (write-long (length _present_pos) s)
     (dotimes (i (length _present_pos))
       (write-long (elt _present_pos i) s)
       )
     ;; int32[] _present_vel
     (write-long (length _present_vel) s)
     (dotimes (i (length _present_vel))
       (write-long (elt _present_vel i) s)
       )
     ;; int32[] _goal_pos
     (write-long (length _goal_pos) s)
     (dotimes (i (length _goal_pos))
       (write-long (elt _goal_pos i) s)
       )
     ;; int32[] _goal_vel
     (write-long (length _goal_vel) s)
     (dotimes (i (length _goal_vel))
       (write-long (elt _goal_vel i) s)
       )
     ;; int32[] _return_delay_time
     (write-long (length _return_delay_time) s)
     (dotimes (i (length _return_delay_time))
       (write-long (elt _return_delay_time i) s)
       )
     ;; int32[] _feedforward_1st_gain
     (write-long (length _feedforward_1st_gain) s)
     (dotimes (i (length _feedforward_1st_gain))
       (write-long (elt _feedforward_1st_gain i) s)
       )
     ;; int32[] _feedforward_2nd_gain
     (write-long (length _feedforward_2nd_gain) s)
     (dotimes (i (length _feedforward_2nd_gain))
       (write-long (elt _feedforward_2nd_gain i) s)
       )
     ;; int32[] _error_status
     (write-long (length _error_status) s)
     (dotimes (i (length _error_status))
       (write-long (elt _error_status i) s)
       )
     ;; int32[] _temp_limit
     (write-long (length _temp_limit) s)
     (dotimes (i (length _temp_limit))
       (write-long (elt _temp_limit i) s)
       )
     ;; int32[] _pos_p_gain
     (write-long (length _pos_p_gain) s)
     (dotimes (i (length _pos_p_gain))
       (write-long (elt _pos_p_gain i) s)
       )
     ;; int32[] _pos_i_gain
     (write-long (length _pos_i_gain) s)
     (dotimes (i (length _pos_i_gain))
       (write-long (elt _pos_i_gain i) s)
       )
     ;; int32[] _pos_d_gain
     (write-long (length _pos_d_gain) s)
     (dotimes (i (length _pos_d_gain))
       (write-long (elt _pos_d_gain i) s)
       )
     ;; int32[] _vel_p_gain
     (write-long (length _vel_p_gain) s)
     (dotimes (i (length _vel_p_gain))
       (write-long (elt _vel_p_gain i) s)
       )
     ;; int32[] _vel_i_gain
     (write-long (length _vel_i_gain) s)
     (dotimes (i (length _vel_i_gain))
       (write-long (elt _vel_i_gain i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _dxl_id
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _dxl_id (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _dxl_id i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _present_temp
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _present_temp (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _present_temp i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _present_load
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _present_load (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _present_load i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _present_volt
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _present_volt (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _present_volt i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _present_current
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _present_current (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _present_current i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _present_pos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _present_pos (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _present_pos i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _present_vel
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _present_vel (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _present_vel i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _goal_pos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _goal_pos (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _goal_pos i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _goal_vel
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _goal_vel (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _goal_vel i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _return_delay_time
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _return_delay_time (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _return_delay_time i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _feedforward_1st_gain
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _feedforward_1st_gain (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _feedforward_1st_gain i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _feedforward_2nd_gain
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _feedforward_2nd_gain (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _feedforward_2nd_gain i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _error_status
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _error_status (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _error_status i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _temp_limit
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _temp_limit (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _temp_limit i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _pos_p_gain
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pos_p_gain (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _pos_p_gain i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _pos_i_gain
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pos_i_gain (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _pos_i_gain i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _pos_d_gain
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pos_d_gain (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _pos_d_gain i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _vel_p_gain
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _vel_p_gain (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _vel_p_gain i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _vel_i_gain
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _vel_i_gain (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _vel_i_gain i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get open_manipulator_core::DynamixelDebug :md5sum-) "76c78346f1f2d00f38d1ed19974ced54")
(setf (get open_manipulator_core::DynamixelDebug :datatype-) "open_manipulator_core/DynamixelDebug")
(setf (get open_manipulator_core::DynamixelDebug :definition-)
      "int32[] dxl_id
int32[] present_temp
int32[] present_load
int32[] present_volt
int32[] present_current
int32[] present_pos
int32[] present_vel
int32[] goal_pos
int32[] goal_vel
int32[] return_delay_time
int32[] feedforward_1st_gain
int32[] feedforward_2nd_gain
int32[] error_status
int32[] temp_limit
int32[] pos_p_gain
int32[] pos_i_gain
int32[] pos_d_gain
int32[] vel_p_gain
int32[] vel_i_gain

")



(provide :open_manipulator_core/DynamixelDebug "76c78346f1f2d00f38d1ed19974ced54")


