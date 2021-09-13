// Auto-generated. Do not edit!

// (in-package open_manipulator_core.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class DynamixelDebug {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.dxl_id = null;
      this.present_temp = null;
      this.present_load = null;
      this.present_volt = null;
      this.present_current = null;
      this.present_pos = null;
      this.present_vel = null;
      this.goal_pos = null;
      this.goal_vel = null;
      this.return_delay_time = null;
      this.feedforward_1st_gain = null;
      this.feedforward_2nd_gain = null;
      this.error_status = null;
      this.temp_limit = null;
      this.pos_p_gain = null;
      this.pos_i_gain = null;
      this.pos_d_gain = null;
      this.vel_p_gain = null;
      this.vel_i_gain = null;
    }
    else {
      if (initObj.hasOwnProperty('dxl_id')) {
        this.dxl_id = initObj.dxl_id
      }
      else {
        this.dxl_id = [];
      }
      if (initObj.hasOwnProperty('present_temp')) {
        this.present_temp = initObj.present_temp
      }
      else {
        this.present_temp = [];
      }
      if (initObj.hasOwnProperty('present_load')) {
        this.present_load = initObj.present_load
      }
      else {
        this.present_load = [];
      }
      if (initObj.hasOwnProperty('present_volt')) {
        this.present_volt = initObj.present_volt
      }
      else {
        this.present_volt = [];
      }
      if (initObj.hasOwnProperty('present_current')) {
        this.present_current = initObj.present_current
      }
      else {
        this.present_current = [];
      }
      if (initObj.hasOwnProperty('present_pos')) {
        this.present_pos = initObj.present_pos
      }
      else {
        this.present_pos = [];
      }
      if (initObj.hasOwnProperty('present_vel')) {
        this.present_vel = initObj.present_vel
      }
      else {
        this.present_vel = [];
      }
      if (initObj.hasOwnProperty('goal_pos')) {
        this.goal_pos = initObj.goal_pos
      }
      else {
        this.goal_pos = [];
      }
      if (initObj.hasOwnProperty('goal_vel')) {
        this.goal_vel = initObj.goal_vel
      }
      else {
        this.goal_vel = [];
      }
      if (initObj.hasOwnProperty('return_delay_time')) {
        this.return_delay_time = initObj.return_delay_time
      }
      else {
        this.return_delay_time = [];
      }
      if (initObj.hasOwnProperty('feedforward_1st_gain')) {
        this.feedforward_1st_gain = initObj.feedforward_1st_gain
      }
      else {
        this.feedforward_1st_gain = [];
      }
      if (initObj.hasOwnProperty('feedforward_2nd_gain')) {
        this.feedforward_2nd_gain = initObj.feedforward_2nd_gain
      }
      else {
        this.feedforward_2nd_gain = [];
      }
      if (initObj.hasOwnProperty('error_status')) {
        this.error_status = initObj.error_status
      }
      else {
        this.error_status = [];
      }
      if (initObj.hasOwnProperty('temp_limit')) {
        this.temp_limit = initObj.temp_limit
      }
      else {
        this.temp_limit = [];
      }
      if (initObj.hasOwnProperty('pos_p_gain')) {
        this.pos_p_gain = initObj.pos_p_gain
      }
      else {
        this.pos_p_gain = [];
      }
      if (initObj.hasOwnProperty('pos_i_gain')) {
        this.pos_i_gain = initObj.pos_i_gain
      }
      else {
        this.pos_i_gain = [];
      }
      if (initObj.hasOwnProperty('pos_d_gain')) {
        this.pos_d_gain = initObj.pos_d_gain
      }
      else {
        this.pos_d_gain = [];
      }
      if (initObj.hasOwnProperty('vel_p_gain')) {
        this.vel_p_gain = initObj.vel_p_gain
      }
      else {
        this.vel_p_gain = [];
      }
      if (initObj.hasOwnProperty('vel_i_gain')) {
        this.vel_i_gain = initObj.vel_i_gain
      }
      else {
        this.vel_i_gain = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DynamixelDebug
    // Serialize message field [dxl_id]
    bufferOffset = _arraySerializer.int32(obj.dxl_id, buffer, bufferOffset, null);
    // Serialize message field [present_temp]
    bufferOffset = _arraySerializer.int32(obj.present_temp, buffer, bufferOffset, null);
    // Serialize message field [present_load]
    bufferOffset = _arraySerializer.int32(obj.present_load, buffer, bufferOffset, null);
    // Serialize message field [present_volt]
    bufferOffset = _arraySerializer.int32(obj.present_volt, buffer, bufferOffset, null);
    // Serialize message field [present_current]
    bufferOffset = _arraySerializer.int32(obj.present_current, buffer, bufferOffset, null);
    // Serialize message field [present_pos]
    bufferOffset = _arraySerializer.int32(obj.present_pos, buffer, bufferOffset, null);
    // Serialize message field [present_vel]
    bufferOffset = _arraySerializer.int32(obj.present_vel, buffer, bufferOffset, null);
    // Serialize message field [goal_pos]
    bufferOffset = _arraySerializer.int32(obj.goal_pos, buffer, bufferOffset, null);
    // Serialize message field [goal_vel]
    bufferOffset = _arraySerializer.int32(obj.goal_vel, buffer, bufferOffset, null);
    // Serialize message field [return_delay_time]
    bufferOffset = _arraySerializer.int32(obj.return_delay_time, buffer, bufferOffset, null);
    // Serialize message field [feedforward_1st_gain]
    bufferOffset = _arraySerializer.int32(obj.feedforward_1st_gain, buffer, bufferOffset, null);
    // Serialize message field [feedforward_2nd_gain]
    bufferOffset = _arraySerializer.int32(obj.feedforward_2nd_gain, buffer, bufferOffset, null);
    // Serialize message field [error_status]
    bufferOffset = _arraySerializer.int32(obj.error_status, buffer, bufferOffset, null);
    // Serialize message field [temp_limit]
    bufferOffset = _arraySerializer.int32(obj.temp_limit, buffer, bufferOffset, null);
    // Serialize message field [pos_p_gain]
    bufferOffset = _arraySerializer.int32(obj.pos_p_gain, buffer, bufferOffset, null);
    // Serialize message field [pos_i_gain]
    bufferOffset = _arraySerializer.int32(obj.pos_i_gain, buffer, bufferOffset, null);
    // Serialize message field [pos_d_gain]
    bufferOffset = _arraySerializer.int32(obj.pos_d_gain, buffer, bufferOffset, null);
    // Serialize message field [vel_p_gain]
    bufferOffset = _arraySerializer.int32(obj.vel_p_gain, buffer, bufferOffset, null);
    // Serialize message field [vel_i_gain]
    bufferOffset = _arraySerializer.int32(obj.vel_i_gain, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DynamixelDebug
    let len;
    let data = new DynamixelDebug(null);
    // Deserialize message field [dxl_id]
    data.dxl_id = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [present_temp]
    data.present_temp = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [present_load]
    data.present_load = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [present_volt]
    data.present_volt = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [present_current]
    data.present_current = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [present_pos]
    data.present_pos = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [present_vel]
    data.present_vel = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [goal_pos]
    data.goal_pos = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [goal_vel]
    data.goal_vel = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [return_delay_time]
    data.return_delay_time = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [feedforward_1st_gain]
    data.feedforward_1st_gain = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [feedforward_2nd_gain]
    data.feedforward_2nd_gain = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [error_status]
    data.error_status = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [temp_limit]
    data.temp_limit = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [pos_p_gain]
    data.pos_p_gain = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [pos_i_gain]
    data.pos_i_gain = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [pos_d_gain]
    data.pos_d_gain = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [vel_p_gain]
    data.vel_p_gain = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [vel_i_gain]
    data.vel_i_gain = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.dxl_id.length;
    length += 4 * object.present_temp.length;
    length += 4 * object.present_load.length;
    length += 4 * object.present_volt.length;
    length += 4 * object.present_current.length;
    length += 4 * object.present_pos.length;
    length += 4 * object.present_vel.length;
    length += 4 * object.goal_pos.length;
    length += 4 * object.goal_vel.length;
    length += 4 * object.return_delay_time.length;
    length += 4 * object.feedforward_1st_gain.length;
    length += 4 * object.feedforward_2nd_gain.length;
    length += 4 * object.error_status.length;
    length += 4 * object.temp_limit.length;
    length += 4 * object.pos_p_gain.length;
    length += 4 * object.pos_i_gain.length;
    length += 4 * object.pos_d_gain.length;
    length += 4 * object.vel_p_gain.length;
    length += 4 * object.vel_i_gain.length;
    return length + 76;
  }

  static datatype() {
    // Returns string type for a message object
    return 'open_manipulator_core/DynamixelDebug';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '76c78346f1f2d00f38d1ed19974ced54';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[] dxl_id
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DynamixelDebug(null);
    if (msg.dxl_id !== undefined) {
      resolved.dxl_id = msg.dxl_id;
    }
    else {
      resolved.dxl_id = []
    }

    if (msg.present_temp !== undefined) {
      resolved.present_temp = msg.present_temp;
    }
    else {
      resolved.present_temp = []
    }

    if (msg.present_load !== undefined) {
      resolved.present_load = msg.present_load;
    }
    else {
      resolved.present_load = []
    }

    if (msg.present_volt !== undefined) {
      resolved.present_volt = msg.present_volt;
    }
    else {
      resolved.present_volt = []
    }

    if (msg.present_current !== undefined) {
      resolved.present_current = msg.present_current;
    }
    else {
      resolved.present_current = []
    }

    if (msg.present_pos !== undefined) {
      resolved.present_pos = msg.present_pos;
    }
    else {
      resolved.present_pos = []
    }

    if (msg.present_vel !== undefined) {
      resolved.present_vel = msg.present_vel;
    }
    else {
      resolved.present_vel = []
    }

    if (msg.goal_pos !== undefined) {
      resolved.goal_pos = msg.goal_pos;
    }
    else {
      resolved.goal_pos = []
    }

    if (msg.goal_vel !== undefined) {
      resolved.goal_vel = msg.goal_vel;
    }
    else {
      resolved.goal_vel = []
    }

    if (msg.return_delay_time !== undefined) {
      resolved.return_delay_time = msg.return_delay_time;
    }
    else {
      resolved.return_delay_time = []
    }

    if (msg.feedforward_1st_gain !== undefined) {
      resolved.feedforward_1st_gain = msg.feedforward_1st_gain;
    }
    else {
      resolved.feedforward_1st_gain = []
    }

    if (msg.feedforward_2nd_gain !== undefined) {
      resolved.feedforward_2nd_gain = msg.feedforward_2nd_gain;
    }
    else {
      resolved.feedforward_2nd_gain = []
    }

    if (msg.error_status !== undefined) {
      resolved.error_status = msg.error_status;
    }
    else {
      resolved.error_status = []
    }

    if (msg.temp_limit !== undefined) {
      resolved.temp_limit = msg.temp_limit;
    }
    else {
      resolved.temp_limit = []
    }

    if (msg.pos_p_gain !== undefined) {
      resolved.pos_p_gain = msg.pos_p_gain;
    }
    else {
      resolved.pos_p_gain = []
    }

    if (msg.pos_i_gain !== undefined) {
      resolved.pos_i_gain = msg.pos_i_gain;
    }
    else {
      resolved.pos_i_gain = []
    }

    if (msg.pos_d_gain !== undefined) {
      resolved.pos_d_gain = msg.pos_d_gain;
    }
    else {
      resolved.pos_d_gain = []
    }

    if (msg.vel_p_gain !== undefined) {
      resolved.vel_p_gain = msg.vel_p_gain;
    }
    else {
      resolved.vel_p_gain = []
    }

    if (msg.vel_i_gain !== undefined) {
      resolved.vel_i_gain = msg.vel_i_gain;
    }
    else {
      resolved.vel_i_gain = []
    }

    return resolved;
    }
};

module.exports = DynamixelDebug;
