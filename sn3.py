################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################
import pyttsx
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
letter ='none'
def saystr(str):
    engine = pyttsx.init()
    engine.say(str)
    engine.runAndWait()
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
            if hand.is_right:             
                         #print right_pinky
                         #print finger.tip_position
                        right_thumb_x = int(hand.fingers[0].tip_position[0])
                        rt_dir_x=float(hand.fingers[0].direction[0])
                        right_thumb_y = int(hand.fingers[0].tip_position[1])
                        rt_dir_y=float(hand.fingers[0].direction[1])
                        right_thumb_z = int(hand.fingers[0].tip_position[2])
                        rt_dir_z=float(hand.fingers[0].direction[2])
                        #print 'rt',rt_dir_y
                        #print finger.tip_position
                    
                        right_index_x = int(hand.fingers[1].tip_position[0])
                        ri_dir_x=float(hand.fingers[1].direction[0])
                        right_index_y = int(hand.fingers[1].tip_position[1])
                        ri_dir_y=float(hand.fingers[1].direction[1])
                        right_index_z = int(hand.fingers[1].tip_position[2])
                        ri_dir_z=float(hand.fingers[1].direction[2])
                        #,(right_thumb_y-right_index_y)
                        #print 'ri',ri_dir_y
                        #print finger.tip_position
                    
                        right_middle_x = int(hand.fingers[2].tip_position[0])
                        rm_dir_x=float(hand.fingers[2].direction[0])
                        right_middle_y = int(hand.fingers[2].tip_position[1])
                        rm_dir_y=float(hand.fingers[2].direction[1])
                        right_middle_z = int(hand.fingers[2].tip_position[2])
                        rm_dir_z=float(hand.fingers[2].direction[2])
                         #print right_index
                         #print finger.tip_position     
                    
                        right_ring_x = int(hand.fingers[3].tip_position[0])
                        rr_dir_x=float(hand.fingers[3].direction[0])
                        right_ring_y = int(hand.fingers[3].tip_position[1])
                        rr_dir_y=float(hand.fingers[3].direction[1])
                        right_ring_z = int(hand.fingers[3].tip_position[2])
                        rr_dir_z=float(hand.fingers[3].direction[2])
                         
                         #print right_ring
                         #print finger.tip_position
                    
                        right_pinky_x = int(hand.fingers[4].tip_position[0])
                        rp_dir_x=float(hand.fingers[4].direction[0])
                        right_pinky_y = int(hand.fingers[4].tip_position[1])
                        rp_dir_y=float(hand.fingers[4].direction[1])
                        right_pinky_z = int(hand.fingers[4].tip_position[2])
                        rp_dir_z=float(hand.fingers[4].direction[2])
                        
                        if (rt_dir_y>0 and  ri_dir_y<0 and rm_dir_y<0 and rr_dir_y<0 and rp_dir_y<0 and right_index_y<right_thumb_y):
                            letter = 'a'
                            print letter
                        elif (rt_dir_x>0 and  ri_dir_y>0 and rm_dir_y>0 and rr_dir_y>0 and rp_dir_y>0):
                            letter = 'b'
                            print letter
                        elif (rt_dir_x<0 and  ri_dir_y<0 and rm_dir_y<0 and rr_dir_y<0 and rp_dir_y<0 and right_index_y>right_thumb_y):
                            letter = 'c'
                            print letter
                        elif (rt_dir_x>0 and  ri_dir_y>0 and rm_dir_y<0 and rr_dir_y<0 and rp_dir_y<0 and (right_index_y-right_thumb_y)>50):
                            letter = 'd'
                            print letter
                        elif (rt_dir_x>0 and  ri_dir_y<0 and rm_dir_y<0 and rr_dir_y<0 and rp_dir_y<0):
                            letter = 'e'
                            print letter
                        elif (rt_dir_y>0 and  ri_dir_y<0 and rm_dir_y>0 and rr_dir_y>0 and rp_dir_y>0 ):
                            letter = 'f'
                            print letter
                        elif (rt_dir_x<0 and  ri_dir_x<0 and rm_dir_x>0 and rr_dir_x>0 and rp_dir_x>0 ):
                            letter = 'g'
                            print letter
                        elif (rt_dir_x<0 and  ri_dir_x<0 and rm_dir_x<0 and rr_dir_x>0 and rp_dir_x>0 ):
                            letter = 'h'
                            print letter
                        elif (rt_dir_x>0 and  ri_dir_y<0 and rm_dir_y<0 and rr_dir_y<0 and rp_dir_y>0 ):
                            letter = 'i'
                            print letter
                            
                        else :
                            letter ='none'
                        saystr(letter)
                            

            
                                           
            if hand.is_left:
               
                        
                         
                        left_thumb_x = int(hand.fingers[0].tip_position[0])
                        lt_dir_x=float(hand.fingers[0].direction[0])
                        left_thumb_y = int(hand.fingers[0].tip_position[1])
                        lt_dir_y=float(hand.fingers[0].direction[1])
                        left_thumb_z = int(hand.fingers[0].tip_position[2])
                        lt_dir_z=float(hand.fingers[0].direction[2])
                        #print 'rt',rt_dir_y
                        #print finger.tip_position
                    
                        left_index_x = int(hand.fingers[1].tip_position[0])
                        li_dir_x=float(hand.fingers[1].direction[0])
                        left_index_y = int(hand.fingers[1].tip_position[1])
                        li_dir_y=float(hand.fingers[1].direction[1])
                        left_index_z = int(hand.fingers[1].tip_position[2])
                        li_dir_z=float(hand.fingers[1].direction[2])
                        #,(right_thumb_y-right_index_y)
                        #print 'ri',ri_dir_y
                        #print finger.tip_position
                    
                        left_middle_x = int(hand.fingers[2].tip_position[0])
                        lm_dir_x=float(hand.fingers[2].direction[0])
                        left_middle_y = int(hand.fingers[2].tip_position[1])
                        lm_dir_y=float(hand.fingers[2].direction[1])
                        left_middle_z = int(hand.fingers[2].tip_position[2])
                        lm_dir_z=float(hand.fingers[2].direction[2])
                         #print right_index
                         #print finger.tip_position     
                    
                        left_ring_x = int(hand.fingers[3].tip_position[0])
                        lr_dir_x=float(hand.fingers[3].direction[0])
                        left_ring_y = int(hand.fingers[3].tip_position[1])
                        lr_dir_y=float(hand.fingers[3].direction[1])
                        left_ring_z = int(hand.fingers[3].tip_position[2])
                        lr_dir_z=float(hand.fingers[3].direction[2])

                        left_pinky_x = int(hand.fingers[4].tip_position[0])
                        lp_dir_x=float(hand.fingers[4].direction[0])
                        left_pinky_y = int(hand.fingers[4].tip_position[1])
                        lp_dir_y=float(hand.fingers[4].direction[1])
                        left_pinky_z = int(hand.fingers[4].tip_position[2])
                        lp_dir_z=float(hand.fingers[4].direction[2])
                          

                     
                      
                

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
