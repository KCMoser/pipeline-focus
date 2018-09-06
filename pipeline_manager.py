import logging                                              # For logging events and outputs to file
import sys                                                  # For logging python version
import platform                                             # For logging OS version
from tkinter import*                                        # GUI module import

# Set up log file and timestamp data
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Set up button action...
def search_button_action(*args):                              # Action for button press created, the *args allows enter or button click to work
    resultText.pack()                                       # Makes result box visible in GUI
    allDone.config(text='Search complete...',font=(60),fg='blue') # Insert a comment that program is done
    root.update()                                           # Screen refresh

#Search for tasks
# for x in y:


# Set up GUI
root=Tk()                                                   # Build standard window object called root
logging.info('App Started')                                 # Add a logging event for App Start
logging.info('Python version is ' +sys.version[0]+sys.version[1] +sys.version[2])        # Log Python version
logging.info('Operating system is: '+platform.system()+' '+platform.release())     # Log OS being run on
root.bind('<Return>', search_button_action)                   # Allows for button press or pressing enter to work
root.title('Pipeline Reminder')                             # Assign title to title bar
root.iconbitmap('favicon.ico')                              # Set icon for window
root.geometry('1000x600')                                   # Set window dimensions
genericText=Label(root,text='Enter activity date or leave blank for today',font=(60)) # Generic text for window with formatting
genericText.pack(fill=X,padx=5,pady=5)                      # Makes text visible in GUI and fills space with formatting
get_date_info=Entry(root)                                   # Creating entry field called getIP
get_date_info.pack()                                        # Makes entry field visible in GUI
search_button=Button(root,text='Go',command=search_button_action) # Button with action
search_button.pack(padx=5,pady=5)                               # Makes button visible in GUI
resultText=Text(root,height=6,width=25,font=(60))           # Create text box for output to be sent
spacerLine=Label(root,text='')                              # Create blank line
spacerLine.pack()
allDone=Label(root,text='',font=(60))                       # Insert a field and set as blank for noting when check completes
allDone.pack()                                              # Insert a comment that program is done
get_date_info.focus()                                       # Makes the text entry field 'active' for input
