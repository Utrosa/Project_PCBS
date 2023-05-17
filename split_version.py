#! /usr/bin/env python
# Time-stamp: <2023-05-17 12:03 monika.utrosa.skerjanec@ens.psl.eu>

##############################################################################################
#
# Can auditory stimulation induce visual hallucinations?
#
# The Shams illusion: code replicating the experimental design of Shams et al. (2002)
# [doi.org/10.1016/S0926-6410(02)00069-1].
#
##############################################################################################

# 1. PREPARATION -----------------------------------------------------------------------------

## Start by importing the neccesary modules and packages. If you do not have the python packages
## installed on your laptop, you can install them with: pip install {package name}.

import random
import pandas as pd
import numpy as np
from expyriment import design, control, stimuli


## Import a csv file containing integer values of all combinations of flash-beep presentations.
## You can find an example csv on te github: shams_trials.csv In this example, the flashes and
## beeps will be presented each from 1 to 4 times.

trials = pd.read_csv('shams_trials.csv')
no_trials = len(trials)


# 2. VARIABLES -------------------------------------------------------------------------------

## Define HEX values for the colors of the visual flash and the background. A useful link:
## www.color-hex.com

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## Define size of the canvas and the instrucitons. These values depend on the size of your
## computer size.

INTRO_HEAD_SIZE = 30
INTRO_TEXT_SIZE = 20
CANVAS_SIZE = (1920, 1080)

## Define the position and size of the fixation cross.

FIXATION_CROSS_SIZE = (20, 20)
FIXATION_CROSS_POSITION = (0, 118)

## Define the parameters of the visual flash. The flash should be subtending 2 degrees of 
## visual angle at 5 degrees eccentricity. To obtain the flash radius and position of if on
## the screen, specify the distance from the participant to the screen. Then calculate the 
## height of the stimulus on the screen. A useful link: 
## https://elvers.us/perception/visualAngle/.

## Here, we assume this distance is 60 cm. While testing, fix the distance between the screen
## and the participant. The screen height here is 24 cm. The vertical resolution is 1080.

FLASH_RADIUS = 45 # radius in cm * vertical resolution / screen height
FLASH_POSITION = (0, -118) # (distance * vertical resolution / screen height) / 2
flash_ISI = 57 # Inter-Stimulus-Interval (ISI): flashes are presented 57 ms apart.

## Define the parameters of the auditory beep. All durations are specified in miliseconds, the 
## frequency is in hertz. Beep ISI denotes the time between sequential presentations of two 
## beeps. The beep duration and beep ISI should sum to a total of a 100 ms.

BEEP_DURATION = 70
BEEP_FREQUENCY = 3500
beep_ISI = 30

## Define the response keys and maximum response delay (max. time the program waits for the 
## participant to respond).

ONE_RESPONSE ='1'
TWO_RESPONSE = '2'
THREE_RESPONSE = '3'
FOUR_RESPONSE = '4'
MAX_RESPONSE_DELAY = 20000

# 3. INITIALIZE THE EXPERIMENT ---------------------------------------------------------------

exp = design.Experiment(name="Shams Experiment")

## While preparing the experiment, set the developer mode to True. For actual testing, comment 
## out this line or set the mode to False.
#control.set_develop_mode(on=True)  

control.initialize(exp)

## Create a canvas screen.
canvas = stimuli.Canvas(size=CANVAS_SIZE, colour=BLACK)

## Create the instructions.
instructions = stimuli.TextScreen("INSTRUCTIONS",

    f"""You will see flashes and hear sounds. 

    How many flashed have you seen?

    Your task is to judge the number of visual flashes.

    Respond by pressing a number from {ONE_RESPONSE} to {FOUR_RESPONSE} on the keyboard.

    There will be {no_trials} trials in total. 

    Press the space bar to being.""", heading_size=INTRO_HEAD_SIZE, text_size=INTRO_TEXT_SIZE)

# 4. CREATE THE STIMULI ----------------------------------------------------------------------

## Create the stimuli & preload them to memory. Preloading prepares the stimuli for a 
## a fast presentation.

	### A fixation cross.

fixation_cross = stimuli.FixCross(size=FIXATION_CROSS_SIZE, colour=WHITE, line_width=4, position=FIXATION_CROSS_POSITION)
fixation_cross.preload()

	### Visual flash as a uniform white disk.

FLASH = stimuli.Circle(radius=FLASH_RADIUS , colour=WHITE, position=FLASH_POSITION)
FLASH.preload()

    ## Auditory beep as a pure tone.

BEEP = stimuli.Tone(duration=BEEP_DURATION, frequency=BEEP_FREQUENCY)
BEEP.preload()

## Randomize the rows of the dataframe ??????????????

trials = trials.iloc[np.random.permutation(len(trials))]

## Define visual and auditory loop functions.

def flash_loop(flash_waiting):

    ''' Presents a flash, which is presented for the specified time and 
    then removed from the canvas screen. The empty screen is presented 
    for the same waiting time before another flash is drawn on the canvas. '''
        
    FLASH.plot(canvas)
    canvas.present()
    exp.clock.wait(flash_waiting)
    canvas.clear_surface()
    fixation_cross.plot(canvas)
    canvas.present()
    exp.clock.wait(flash_waiting)

def beep_loop(beep_waiting):
    
    ''' Present a beep and stop it. Wait the for the specided waiting 
    time before another beep is played. '''

    BEEP.play()
    exp.clock.wait(beep_waiting)

# 5. Add varibles names for storing data. ----------------------------------------------------

exp.add_data_variable_names(['trial',
                             'number_sounds',
                             'number_flashes',
                             'response_key',
                             'RT'])

# 6. RUN THE EXPERIMENT ----------------------------------------------------------------------

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

### Run the experiment.
    #### Link flash-beep-fixation_cross presentation with a column in the dataframe.

for index, row in trials.iterrows():
    fixation_cross.plot(canvas)
    canvas.present()

    for b_rep in range(row['BEEP']):
        beep_loop(beep_ISI)

    for f_rep in range(row['FLASH']): # Corresponds to the third column (FLASH)
        flash_loop(flash_ISI)

    key, rt = exp.keyboard.wait_char([ONE_RESPONSE, TWO_RESPONSE, THREE_RESPONSE, FOUR_RESPONSE],
                                     duration=MAX_RESPONSE_DELAY)

# 7. SAVE THE DATA ---------------------------------------------------------------------------

    exp.data.add([index+1, b_rep+1, f_rep+1, key, rt])

# 8. END THE EXPERIMENT ----------------------------------------------------------------------
control.end()