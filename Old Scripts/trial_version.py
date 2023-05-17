###################################################################
#
# The Shams illusion: WORK IN PROGRES !!
#
# Can auditory stimulation induce visual hallucinations?
#
###################################################################


## DONE: presentation of sound.
## DONE: multiple presentations of circles.
## FAIL: factorial design of trials & circle presentations

### Start by importing all the neccesary modules and packages.

import random
import pandas as pd
import numpy as np
from expyriment import design, control, stimuli
from multiprocessing import Process

### Define the variables.-----------------------------------------

WHITE = (255, 255, 255)
GRAY = (136, 136, 136)
flash_duration = 50
trial_duration = 1000
no_trials = 5
number_flashes = [4, 4, 4, 4]
number_sounds = [1, 2, 3, 4]

INTRO_HEAD_SIZE = 20
INTRO_TEXT_SIZE = 10 # Might have to adapt for different screens.
CANVAS_SIZE = (800, 800)

FIXATION_CROSS_SIZE = (20, 20)
FIXATION_CROSS_POSITION = (0, 100)

FLASH_RADIUS = 40 
FLASH_POSITION = (0, -100) # Fix the distance from the screen.

BEEP_DURATION = 7
BEEP_FREQUENCY = 3500
beep_waiting = 57

ONE_RESPONSE ='1'
TWO_RESPONSE = '2'
THREE_RESPONSE = '3'
FOUR_RESPONSE = '4'
MAX_RESPONSE_DELAY = 20000

### Initialize the experiment.------------------------------------------------------------

exp = design.Experiment(name="Shams Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment.

control.initialize(exp)

### Create a canvas screen.
canvas = stimuli.Canvas(size=CANVAS_SIZE, colour=GRAY)

### Create the instructions.
instructions = stimuli.TextScreen("INSTRUCTIONS",

    f"""You will see flashes and hear sounds. 

    Your task is to judge the number of visual flashes.

    How many flashed have you seen?

    Respond by pressing a number from '{ONE_RESPONSE}' to '{FOUR_RESPONSE}' on the keyboard.

    There will be '{no_trials}' trial in total. 

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
    ##### A factorial design in which all combinations of 0–4 flashes and 0–4 beeps (except for the no flash–no beep combination)
    ##### are presented, leading to a total of 24 conditions.
trials = pd.read_csv('shams_trials.csv') # Import a dataset of integer values with all combinations of flash-beep-fixation_cross presentations.
trials = trials.iloc[np.random.permutation(len(trials))] # Randomize the rows of the dataframe.

### Add varibles names for storing data. -----------------------------------------------------------

exp.add_data_variable_names(['trial',
                             'number_flashes',
                             'number_sounds',
                             'response_key',
                             'RT'])

### Initialize the stimuli & start the experiment.--------------------------------------------------

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

### Run the experiment.
    ## Link flash-beep-fixation_cross presentation with a column in the dataframe.

for index, row in trials.iterrows():
    fixation_cross.plot(canvas)
    canvas.present()
    exp.clock.wait(flash_duration)
    
    for f_rep in range(row['FLASH']): # corresponds to the third column (FLASH)
        FLASH.plot(canvas)
        canvas.present()
        exp.clock.wait(flash_duration)
        canvas.clear_surface()
        fixation_cross.plot(canvas)
        canvas.present()
        exp.clock.wait(flash_duration)
        
    for b_rep in range(row['BEEP']):
        exp.clock.wait(beep_waiting)
        BEEP.play()
        exp.clock.wait(beep_waiting)

    key, rt = exp.keyboard.wait_char([ONE_RESPONSE, TWO_RESPONSE, THREE_RESPONSE, FOUR_RESPONSE],
                                     duration=MAX_RESPONSE_DELAY)

### Save the data.-------------------------------------------------------------------------------------

    exp.data.add([index, f_rep, b_rep, key, rt])

### End the experiment.
control.end()