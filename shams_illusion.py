###################################################################
#
#The Shams illusion: WORK IN PROGRES !!
#
# Can auditory stimulation induce visual hallucinations?
#
###################################################################


### Start by importing all the neccesary modules and packages.

from expyriment import design, control, stimuli
import matplotlib as plt # To plot the results.

### Define the variables.

WHITE = (255, 255, 255)
BLUE = (3,50,74)
flash_duration = 17
trial_duration = 1000

INTRO_TEXT_SIZE = 30 # Might have to adapt for different screens.
CANVAS_SIZE = (800, 800)

FIXATION_CROSS_SIZE = (20, 20)
FIXATION_CROSS_POSITION = (0, 100)

FLASH_RADIUS = 40 
FLASH_POSITION = (0, -100) # Fix the distance from the screen.

beep_filepath = "C:/Users/monik/Documents/Paris/M1 - S2/PROG 201/myproject/tone.wav"

### Initialize the experiment.

exp = design.Experiment(name="Shams Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment.

control.initialize(exp)

### Create a canvas screen.

canvas = stimuli.Canvas(size=CANVAS_SIZE, colour=BLUE)

### Create the instructions.
instructions = stimuli.TextScreen("Instructions",
    f"""You will see flashes and hear sounds. 

    Your task is to judge the number of visual flashes.

    Press the number on the keyboard that corresponds to the number of flashes.

    There will be 1 trial in total. 

    Press the space bar to being.""",  text_size=INTRO_TEXT_SIZE)

### Create the visual stimuli & preload.
	#### A fixation cross.

fixation_cross = stimuli.FixCross(size=FIXATION_CROSS_SIZE, colour=WHITE, line_width=4, position=FIXATION_CROSS_POSITION)
fixation_cross.plot(canvas)
fixation_cross.preload()

	#### A uniform white disk (subtending 2 degrees at 5 degrees eccentricity).

FLASH = stimuli.Circle(radius=FLASH_RADIUS , colour=WHITE, position=FLASH_POSITION)
FLASH.plot(canvas)
FLASH.preload()

### Create the auditory stimuli & preload.
    ##### A pure tone with freqency of 3500 Hz, duration of 7 ms, and with an onset asynchrony of 57 ms.

BEEP = stimuli.Audio(beep_filepath)

### Create the trials and blocks.

### Initialize the stimuli & start the experiment.

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

### Run the experiment.
canvas.present()
exp.clock.wait(flash_duration)
canvas.clear_surface()

canvas.present()
exp.clock.wait(trial_duration)
canvas.clear_surface()

### Save the data.

### End the experiment.
control.end()