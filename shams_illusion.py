###################################################################
#
# The Shams illusion: WORK IN PROGRES !!
#
# Can auditory stimulation induce visual hallucinations?
#
###################################################################


### Start by importing all the neccesary modules and packages.

from expyriment import design, control, stimuli
import matplotlib as plt # To plot the results.

### Define the variables.-----------------------------------------

WHITE = (255, 255, 255)
GRAY = (136, 136, 136)
flash_duration = 17
trial_duration = 1000
no_trials = 24
repetitions = [1, 2, 3, 4]

INTRO_HEAD_SIZE = 20
INTRO_TEXT_SIZE = 10 # Might have to adapt for different screens.
CANVAS_SIZE = (800, 800)

FIXATION_CROSS_SIZE = (20, 20)
FIXATION_CROSS_POSITION = (0, 100)

FLASH_RADIUS = 40 
FLASH_POSITION = (0, -100) # Fix the distance from the screen.

beep_filepath = "shams_tone.wav"
BEEP_DURATION = 7

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

BEEP = stimuli.Audio(beep_filepath)
# BEEP.preload() # FAIL: TypeError: Unrecognized argument (type _io.BufferedReader) !!!!!!!!!!

### Create the trials and blocks.
    ##### A factorial design in which all combinations of 0–4 flashes and 0–4 beeps (except for the no flash–no beep combination)
    ##### are presented, leading to a total of 24 conditions.

block = design.Block()
#BEEP.play() #maxtime=BEEP_DURATION

for trial in range(no_trials):
    fixation_cross.plot(canvas)
    t.add_stimulus(canvas)
    for y in range(i):
        FLASH.plot(canvas)
        canvas.present()
        exp.clock.wait(flash_duration)
        canvas.clear_surface()
        fixation_cross.plot(canvas)
        canvas.present()
        t.add_stimulus(canvas)
block.add_trial(trial)

block.shuffle_trials(max_repetitions=1) ################# MAGICAL
exp.add_block(block)

### Initialize the stimuli & start the experiment.--------------------------------------------------

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

### Run the experiment.

for i in block:
    trial.stimuli[0].present()
# for i in range(len(no_trials)): # 24 times
#     #BEEP.play() #maxtime=BEEP_DURATION
#     fixation_cross.plot(canvas)
#     for i in repetitions:
#         for y in range(i):
#             FLASH.plot(canvas)
#             canvas.present()
#             exp.clock.wait(flash_duration)
#             canvas.clear_surface()
#             fixation_cross.plot(canvas)
#             canvas.present()
    key, rt = exp.keyboard.wait_char([ONE_RESPONSE, TWO_RESPONSE, THREE_RESPONSE, FOUR_RESPONSE],
                                     duration=MAX_RESPONSE_DELAY)
    #exp.data.add([
     #   trial.get_factor('number'),
    #])

### Save the data.-------------------------------------------------------------------------------------

### End the experiment.
control.end()