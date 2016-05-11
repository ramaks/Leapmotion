import Leap,sys
def main():
     controller = Leap.Controller()

     # Keep this process running until Enter is pressed
     print "Press Enter to quit..."
     try:
         sys.stdin.readline()
     except KeyboardInterrupt:
         pass
if __name__ == "__main__":
    main()    
