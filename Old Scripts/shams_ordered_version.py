#! /usr/bin/env python
# Time-stamp: <2023-05-24 11:59 monika.utrosa.skerjanec@ens.psl.eu>

###################################################################
#
# The Shams illusion
#
# Can auditory stimulation induce visual hallucinations?
#
###################################################################


## FAIL: BEEP.preload() due to TypeError: Unrecognized argument (type _io.BufferedReader) !!!!!!!!!!
## DONE: multiple presentations of circles.
## FAIL: factorial design of trials & circle presentations


### Start by importing all the neccesary modules and packages.

from expyriment import design, control, stimuli
import matplotlib as plt # To plot the results.

### Define the variables.-----------------------------------------

WHITE = (255, 255, 255)
GRAY = (136, 136, 136)
flash_duration = 57
trial_duration = 1000
no_trials = 5
number_flashes = [4, 4, 4, 4]
number_sounds = [1, 2, 3, 4]

INTRO_HEAD_SIZE = 30
INTRO_TEXT_SIZE = 20 # Might have to adapt for different screens.
CANVAS_SIZE = (800, 800)

FIXATION_CROSS_SIZE = (20, 20)
FIXATION_CROSS_POSITION = (0, 100)

FLASH_RADIUS = 40 
FLASH_POSITION = (0, -100) # Fix the distance from the screen.

BEEP_DURATION = 7
BEEP_FREQUENCY = 3500

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
    ##### AMPLITUDE ????!!!!

BEEP = stimuli.Tone(duration=BEEP_DURATION, frequency=BEEP_FREQUENCY)
BEEP.preload()

### Create the trials and blocks.
    ##### A factorial design in which all combinations of 0–4 flashes and 0–4 beeps (except for the no flash–no beep combination)
    ##### are presented, leading to a total of 24 conditions.

### Add varibles names for storing data. -----------------------------------------------------------

exp.add_data_variable_names(['number_trials',
                             'number_flashes',
                             'response_key',
                             'RT'])

### Initialize the stimuli & start the experiment.--------------------------------------------------

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

### Run the experiment.

for count, flash in enumerate(number_flashes, 1): # Start the count with one. Skip 0 flash presentation.
                                                  # 1, 1 2, 1 2 3, 1 2 3 4
    for f in range(flash):
        fixation_cross.plot(canvas)
        canvas.present()
        exp.clock.wait(flash_duration)
        for c in range(count):
            FLASH.plot(canvas)
            canvas.present()
            exp.clock.wait(flash_duration)
            BEEP.play()
            canvas.clear_surface()
            fixation_cross.plot(canvas)
            canvas.present()
            exp.clock.wait(flash_duration)


        key, rt = exp.keyboard.wait_char([ONE_RESPONSE, TWO_RESPONSE, THREE_RESPONSE, FOUR_RESPONSE],
                                     duration=MAX_RESPONSE_DELAY)

### Save the data.-------------------------------------------------------------------------------------

        exp.data.add([flash, count, key, rt])

### End the experiment.
control.end()