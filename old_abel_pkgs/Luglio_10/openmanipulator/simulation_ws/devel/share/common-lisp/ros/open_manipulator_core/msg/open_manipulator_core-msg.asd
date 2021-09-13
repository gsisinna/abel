
(cl:in-package :asdf)

(defsystem "open_manipulator_core-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "DynamixelDebug" :depends-on ("_package_DynamixelDebug"))
    (:file "_package_DynamixelDebug" :depends-on ("_package"))
  ))