
"use strict";

let SetActuatorState = require('./SetActuatorState.js')
let SetJointPosition = require('./SetJointPosition.js')
let GetJointPosition = require('./GetJointPosition.js')
let SetDrawingTrajectory = require('./SetDrawingTrajectory.js')
let GetKinematicsPose = require('./GetKinematicsPose.js')
let SetKinematicsPose = require('./SetKinematicsPose.js')

module.exports = {
  SetActuatorState: SetActuatorState,
  SetJointPosition: SetJointPosition,
  GetJointPosition: GetJointPosition,
  SetDrawingTrajectory: SetDrawingTrajectory,
  GetKinematicsPose: GetKinematicsPose,
  SetKinematicsPose: SetKinematicsPose,
};
