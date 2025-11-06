
(cl:in-package :asdf)

(defsystem "rss2_msgsrv_pkg-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "srv_turtlebot3_move" :depends-on ("_package_srv_turtlebot3_move"))
    (:file "_package_srv_turtlebot3_move" :depends-on ("_package"))
  ))