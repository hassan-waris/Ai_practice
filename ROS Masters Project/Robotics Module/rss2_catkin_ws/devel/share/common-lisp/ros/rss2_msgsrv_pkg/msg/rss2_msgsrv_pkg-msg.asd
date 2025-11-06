
(cl:in-package :asdf)

(defsystem "rss2_msgsrv_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "date_cmd_vel" :depends-on ("_package_date_cmd_vel"))
    (:file "_package_date_cmd_vel" :depends-on ("_package"))
  ))