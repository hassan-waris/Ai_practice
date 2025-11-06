// Auto-generated. Do not edit!

// (in-package rss2_msgsrv_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class date_cmd_vel {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pw_date = null;
      this.pw_cmd_vel = null;
    }
    else {
      if (initObj.hasOwnProperty('pw_date')) {
        this.pw_date = initObj.pw_date
      }
      else {
        this.pw_date = '';
      }
      if (initObj.hasOwnProperty('pw_cmd_vel')) {
        this.pw_cmd_vel = initObj.pw_cmd_vel
      }
      else {
        this.pw_cmd_vel = new geometry_msgs.msg.Twist();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type date_cmd_vel
    // Serialize message field [pw_date]
    bufferOffset = _serializer.string(obj.pw_date, buffer, bufferOffset);
    // Serialize message field [pw_cmd_vel]
    bufferOffset = geometry_msgs.msg.Twist.serialize(obj.pw_cmd_vel, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type date_cmd_vel
    let len;
    let data = new date_cmd_vel(null);
    // Deserialize message field [pw_date]
    data.pw_date = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [pw_cmd_vel]
    data.pw_cmd_vel = geometry_msgs.msg.Twist.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.pw_date);
    return length + 52;
  }

  static datatype() {
    // Returns string type for a message object
    return 'rss2_msgsrv_pkg/date_cmd_vel';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '63f9a130ea4a5bfb02bbb1541b739e89';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string pw_date
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new date_cmd_vel(null);
    if (msg.pw_date !== undefined) {
      resolved.pw_date = msg.pw_date;
    }
    else {
      resolved.pw_date = ''
    }

    if (msg.pw_cmd_vel !== undefined) {
      resolved.pw_cmd_vel = geometry_msgs.msg.Twist.Resolve(msg.pw_cmd_vel)
    }
    else {
      resolved.pw_cmd_vel = new geometry_msgs.msg.Twist()
    }

    return resolved;
    }
};

module.exports = date_cmd_vel;
