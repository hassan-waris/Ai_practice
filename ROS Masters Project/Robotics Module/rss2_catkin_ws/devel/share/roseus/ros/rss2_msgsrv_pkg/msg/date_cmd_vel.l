;; Auto-generated. Do not edit!


(when (boundp 'rss2_msgsrv_pkg::date_cmd_vel)
  (if (not (find-package "RSS2_MSGSRV_PKG"))
    (make-package "RSS2_MSGSRV_PKG"))
  (shadow 'date_cmd_vel (find-package "RSS2_MSGSRV_PKG")))
(unless (find-package "RSS2_MSGSRV_PKG::DATE_CMD_VEL")
  (make-package "RSS2_MSGSRV_PKG::DATE_CMD_VEL"))

(in-package "ROS")
;;//! \htmlinclude date_cmd_vel.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass rss2_msgsrv_pkg::date_cmd_vel
  :super ros::object
  :slots (_pw_date _pw_cmd_vel ))

(defmethod rss2_msgsrv_pkg::date_cmd_vel
  (:init
   (&key
    ((:pw_date __pw_date) "")
    ((:pw_cmd_vel __pw_cmd_vel) (instance geometry_msgs::Twist :init))
    )
   (send-super :init)
   (setq _pw_date (string __pw_date))
   (setq _pw_cmd_vel __pw_cmd_vel)
   self)
  (:pw_date
   (&optional __pw_date)
   (if __pw_date (setq _pw_date __pw_date)) _pw_date)
  (:pw_cmd_vel
   (&rest __pw_cmd_vel)
   (if (keywordp (car __pw_cmd_vel))
       (send* _pw_cmd_vel __pw_cmd_vel)
     (progn
       (if __pw_cmd_vel (setq _pw_cmd_vel (car __pw_cmd_vel)))
       _pw_cmd_vel)))
  (:serialization-length
   ()
   (+
    ;; string _pw_date
    4 (length _pw_date)
    ;; geometry_msgs/Twist _pw_cmd_vel
    (send _pw_cmd_vel :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _pw_date
       (write-long (length _pw_date) s) (princ _pw_date s)
     ;; geometry_msgs/Twist _pw_cmd_vel
       (send _pw_cmd_vel :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _pw_date
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _pw_date (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Twist _pw_cmd_vel
     (send _pw_cmd_vel :deserialize buf ptr-) (incf ptr- (send _pw_cmd_vel :serialization-length))
   ;;
   self)
  )

(setf (get rss2_msgsrv_pkg::date_cmd_vel :md5sum-) "63f9a130ea4a5bfb02bbb1541b739e89")
(setf (get rss2_msgsrv_pkg::date_cmd_vel :datatype-) "rss2_msgsrv_pkg/date_cmd_vel")
(setf (get rss2_msgsrv_pkg::date_cmd_vel :definition-)
      "string pw_date
geometry_msgs/Twist pw_cmd_vel

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
")



(provide :rss2_msgsrv_pkg/date_cmd_vel "63f9a130ea4a5bfb02bbb1541b739e89")


