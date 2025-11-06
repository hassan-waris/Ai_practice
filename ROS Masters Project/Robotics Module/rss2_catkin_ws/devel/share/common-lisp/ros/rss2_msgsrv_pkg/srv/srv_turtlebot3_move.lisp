; Auto-generated. Do not edit!


(cl:in-package rss2_msgsrv_pkg-srv)


;//! \htmlinclude srv_turtlebot3_move-request.msg.html

(cl:defclass <srv_turtlebot3_move-request> (roslisp-msg-protocol:ros-message)
  ((duration
    :reader duration
    :initarg :duration
    :type cl:integer
    :initform 0))
)

(cl:defclass srv_turtlebot3_move-request (<srv_turtlebot3_move-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <srv_turtlebot3_move-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'srv_turtlebot3_move-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rss2_msgsrv_pkg-srv:<srv_turtlebot3_move-request> is deprecated: use rss2_msgsrv_pkg-srv:srv_turtlebot3_move-request instead.")))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <srv_turtlebot3_move-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rss2_msgsrv_pkg-srv:duration-val is deprecated.  Use rss2_msgsrv_pkg-srv:duration instead.")
  (duration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <srv_turtlebot3_move-request>) ostream)
  "Serializes a message object of type '<srv_turtlebot3_move-request>"
  (cl:let* ((signed (cl:slot-value msg 'duration)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <srv_turtlebot3_move-request>) istream)
  "Deserializes a message object of type '<srv_turtlebot3_move-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'duration) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<srv_turtlebot3_move-request>)))
  "Returns string type for a service object of type '<srv_turtlebot3_move-request>"
  "rss2_msgsrv_pkg/srv_turtlebot3_moveRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'srv_turtlebot3_move-request)))
  "Returns string type for a service object of type 'srv_turtlebot3_move-request"
  "rss2_msgsrv_pkg/srv_turtlebot3_moveRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<srv_turtlebot3_move-request>)))
  "Returns md5sum for a message object of type '<srv_turtlebot3_move-request>"
  "b92c952a9248b3029cefe45f52f6ffde")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'srv_turtlebot3_move-request)))
  "Returns md5sum for a message object of type 'srv_turtlebot3_move-request"
  "b92c952a9248b3029cefe45f52f6ffde")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<srv_turtlebot3_move-request>)))
  "Returns full string definition for message of type '<srv_turtlebot3_move-request>"
  (cl:format cl:nil "int32 duration  #Request - time turtlebot3 moves~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'srv_turtlebot3_move-request)))
  "Returns full string definition for message of type 'srv_turtlebot3_move-request"
  (cl:format cl:nil "int32 duration  #Request - time turtlebot3 moves~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <srv_turtlebot3_move-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <srv_turtlebot3_move-request>))
  "Converts a ROS message object to a list"
  (cl:list 'srv_turtlebot3_move-request
    (cl:cons ':duration (duration msg))
))
;//! \htmlinclude srv_turtlebot3_move-response.msg.html

(cl:defclass <srv_turtlebot3_move-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass srv_turtlebot3_move-response (<srv_turtlebot3_move-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <srv_turtlebot3_move-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'srv_turtlebot3_move-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rss2_msgsrv_pkg-srv:<srv_turtlebot3_move-response> is deprecated: use rss2_msgsrv_pkg-srv:srv_turtlebot3_move-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <srv_turtlebot3_move-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rss2_msgsrv_pkg-srv:success-val is deprecated.  Use rss2_msgsrv_pkg-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <srv_turtlebot3_move-response>) ostream)
  "Serializes a message object of type '<srv_turtlebot3_move-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <srv_turtlebot3_move-response>) istream)
  "Deserializes a message object of type '<srv_turtlebot3_move-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<srv_turtlebot3_move-response>)))
  "Returns string type for a service object of type '<srv_turtlebot3_move-response>"
  "rss2_msgsrv_pkg/srv_turtlebot3_moveResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'srv_turtlebot3_move-response)))
  "Returns string type for a service object of type 'srv_turtlebot3_move-response"
  "rss2_msgsrv_pkg/srv_turtlebot3_moveResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<srv_turtlebot3_move-response>)))
  "Returns md5sum for a message object of type '<srv_turtlebot3_move-response>"
  "b92c952a9248b3029cefe45f52f6ffde")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'srv_turtlebot3_move-response)))
  "Returns md5sum for a message object of type 'srv_turtlebot3_move-response"
  "b92c952a9248b3029cefe45f52f6ffde")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<srv_turtlebot3_move-response>)))
  "Returns full string definition for message of type '<srv_turtlebot3_move-response>"
  (cl:format cl:nil "bool success    #Respond ~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'srv_turtlebot3_move-response)))
  "Returns full string definition for message of type 'srv_turtlebot3_move-response"
  (cl:format cl:nil "bool success    #Respond ~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <srv_turtlebot3_move-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <srv_turtlebot3_move-response>))
  "Converts a ROS message object to a list"
  (cl:list 'srv_turtlebot3_move-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'srv_turtlebot3_move)))
  'srv_turtlebot3_move-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'srv_turtlebot3_move)))
  'srv_turtlebot3_move-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'srv_turtlebot3_move)))
  "Returns string type for a service object of type '<srv_turtlebot3_move>"
  "rss2_msgsrv_pkg/srv_turtlebot3_move")