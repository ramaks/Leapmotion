################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"
            if hand.is_right:
                arm = hand.arm
                vertvalue=int(arm.wrist_position[1])
                print "  vertical value: %d," % (vertvalue)
                tempid=hand.fingers[0].id
                for finger in hand.fingers:
                    if finger.id==tempid:
                        thumb = int(finger.tip_position[0])
                    if finger.id==tempid+1:
                         index = int(finger.tip_position[0])
                         fingdiff=abs(thumb-index)
                         print "finger diff",fingdiff         #Use for finger movement
                    if finger.id==tempid+2:
                        break
            if hand.is_left:
               tempid=hand.fingers[0].id
               for finger in hand.fingers:
                    #print finger.tip_position,finger.id,self.finger_names[finger.type]
                    if finger.id==tempid+2:
                        lmiddle = int(finger.tip_position[1])
                        lback =float(finger.direction[2])
                        if lback<0:
                            back=1
                        else:
                            back=0
                        
                    if finger.id==tempid:
                        lthumb = int(finger.tip_position[1])
                        
                    if finger.id==tempid+4:
                         lpinky = int(finger.tip_position[1])
                         #lfingdiff=lthumb-lpinky
                         #print "finger diff",lfingdiff
                         if lpinky+40<lthumb and lmiddle<200:
                            print "left"
                         elif lthumb+30<lpinky and lmiddle<200:
                            print "right"
                         elif lmiddle<200:
                            print "straight"
                         else:
                             print "stop"

                     
                      
                

##                print " %s finger id: %d, position: %s" % (
##                self.finger_names[finger.type],finger.id, finger.tip_position[0])#, finger.direction)
                              
            
            
def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
