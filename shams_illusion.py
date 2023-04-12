###################################################################
#
#					The Shams illusion
#
# Can auditory stimulation induce visual hallucinations?
#
###################################################################


### Start by importing all the neccesary modules and packages.

from expyriment import design, control, stimuli
#import librosa # To make cool sounds.
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