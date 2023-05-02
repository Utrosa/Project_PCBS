###################################################################
#
# The Shams illusion: WORK IN PROGRES !!
#
# Can auditory stimulation induce visual hallucinations?
#
###################################################################


## DONE: variable presentation of sound.
## DONE: variable presentations of flashes.

## FAIL: PERFECT factorial design of trials & circle presentations -> check excel
## FAIL: get a CSV file of the responses
## FAIL: take the DEGREES of visual angle into account for specifying disc size

### Start by importing all the neccesary modules and packages.

import random
import pandas as pd
import numpy as np
from expyriment import design, control, stimuli

### Define the variables.----------------------------------------------------------------------

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

INTRO_HEAD_SIZE = 30
INTRO_TEXT_SIZE = 20 # Might have to adapt for different screens.
CANVAS_SIZE = (800, 800)

FIXATION_CROSS_SIZE = (20, 20)
FIXATION_CROSS_POSITION = (0, 100)

FLASH_RADIUS = 40 
FLASH_POSITION = (0, -100) # Fix the distance from the screen.
flash_ISI = 50 # Inter-Stimulus-Interval (ISI) for flashes == flashes are presented 50 ms apart

BEEP_DURATION = 7
BEEP_FREQUENCY = 3500
beep_ISI = 50 # ISI for beeps == beeps are separated by 57 ms

trials = pd.read_csv('shams_trials.csv') # Import a dataset of integer values with all combinations of flash-beep-fixation_cross presentations.
no_trials = len(trials)
number_flashes = [4, 4, 4, 4]
number_sounds = [1, 2, 3, 4]

ONE_RESPONSE ='1'
TWO_RESPONSE = '2'
THREE_RESPONSE = '3'
FOUR_RESPONSE = '4'
MAX_RESPONSE_DELAY = 20000

### Initialize the experiment.------------------------------------------------------------------

exp = design.Experiment(name="Shams Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment.

control.initialize(exp)

### Create a canvas screen.
canvas = stimuli.Canvas(size=CANVAS_SIZE, colour=BLACK)

### Create the instructions.
instructions = stimuli.TextScreen("INSTRUCTIONS",

    f"""You will see flashes and hear sounds. 

    Your task is to judge the number of visual flashes.

    How many flashed have you seen?

    Respond by pressing a number from {ONE_RESPONSE} to {FOUR_RESPONSE} on the keyboard.

    There will be {no_trials} trial in total. 

    Press the space bar to being.""", heading_size=INTRO_HEAD_SIZE, text_size=INTRO_TEXT_SIZE)

### Create all stimuli.--------------------------------------------------------------------------------------------------

### Create the visual stimuli & preload.
	#### A fixation cross.

fixation_cross = stimuli.FixCross(size=FIXATION_CROSS_SIZE, colour=WHITE, line_width=4, position=FIXATION_CROSS_POSITION)
fixation_cross.preload()

	#### A uniform white disk (subtending 2 degrees at 5 degrees eccentricity).
    #### https://en.wikipedia.org/wiki/Polar_coordinate_system
    #### Specify the distance to the screen to calculate the height of the stimulus on the screen.

FLASH = stimuli.Circle(radius=FLASH_RADIUS , colour=WHITE, position=FLASH_POSITION)
FLASH.preload()

### Create the auditory stimuli & preload.
    ##### A pure tone with freqency of 3500 Hz, duration of 7 ms, and with an onset asynchrony of 57 ms.

BEEP = stimuli.Tone(duration=BEEP_DURATION, frequency=BEEP_FREQUENCY)
BEEP.preload()

### Create the trials and blocks.
    ##### A factorial design in which all combinations of 1–4 flashes and 0–4 beeps.
    ##### are presented, leading to a total of 24 conditions.

trials = trials.iloc[np.random.permutation(len(trials))] # Randomize the rows of the dataframe.

    #### Define visual and auditory loop.

def flash_loop(flash_waiting):

    ''' Define a function to present a flash at a time,
    folowed by a given waiting time'''
        
    FLASH.plot(canvas)
    canvas.present()
    exp.clock.wait(flash_waiting)
    canvas.clear_surface()
    fixation_cross.plot(canvas)
    canvas.present()
    exp.clock.wait(flash_waiting)

def beep_loop(beep_waiting):
    
    ''' Define a function to present a beep at a time,
    followed by a given waiting time '''

    BEEP.play()
    exp.clock.wait(beep_waiting)


### Add varibles names for storing data. -----------------------------------------------------------

exp.add_data_variable_names(['trial',
                             'number_sounds',
                             'number_flashes',
                             'response_key',
                             'RT'])

### Initialize the stimuli & start the experiment.--------------------------------------------------

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

### Save the data.-------------------------------------------------------------------------------------

    exp.data.add([index, b_rep, f_rep, key, rt])

### End the experiment.
control.end()