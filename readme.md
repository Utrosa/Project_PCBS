# Replication of the Shams Illusion

## About the Project
In 2002 naive observers were asked to report the number of visual flashes presented on the screen. The visual flashes were accompanied by different numbers of beeps on each trial. The observers consistently reported incorrect number of visual flashes when these were accompanied by multiple auditory beeps. The results suggest that auditory stimulation can induce a visual illusion. This phenomenon has been named by the first author Dr. Ladan Shams as the Shams Illusion. Demonstrations of the illusions are available here: https://shamslab.psych.ucla.edu/demos/.

#### The Original Paper
Ladan Shams, Yukiyasu Kamitani, Shinsuke Shimojo, Visual illusion induced by sound, Cognitive Brain Research, Volume 14, Issue 1, 2002, Pages 147-152, ISSN 0926-6410, https://doi.org/10.1016/S0926-6410(02)00069-1.

##### Abstract
We present the first cross-modal modification of visual perception which involves a phenomenological change in the quality—as opposed to a small, gradual, or quantitative change—of the percept of a non-ambiguous visual stimulus. We report a visual illusion which is induced by sound: when a single flash of light is accompanied by multiple auditory beeps, the single flash is perceived as multiple flashes. We present two experiments as well as several observations which establish that this alteration of the visual percept is due to cross-modal perceptual interactions as opposed to cognitive, attentional, or other origins. The results of the second experiment also reveal that the temporal window of these audio–visual interactions is approximately 100 ms.

**Keywords**: Crossmodal interaction; Auditory–visual interaction; Visual illusion; Illusory flashing; Multisensory integration; Audio–visual perceptio

## Aim
This project was part of the [Programming for Cognitive and Brain Sciences](https://pcbs.readthedocs.io/en/latest/) (PCBS) course taught at the Cogmaster. My goal was to replicate the experimental task reported in Shams et al. (2002) with the [Expyriment](https://expyriment.org/) python library to enable fast and simple replication of the experiment.

## Getting Started
Clone the repository:

  ```
  git clone https://github.com/Utrosa/shams_illusion_PCBS.git
  ```
  
### Prerequisites
To run the code successfully on your local computer, you will need to have installed python, anaconda, and the expyriment library.

To install expyriment enter the following to your command line:

  ```
  pip install expyriment
  ```
  
### Running the Experiment
The final (best) version of the experiment is [final_version.py](https://github.com/Utrosa/shams_illusion_PCBS/blob/master/final_version.py).

I added two alternative versions in the folder [Old Scripts](https://github.com/Utrosa/shams_illusion_PCBS/blob/master/Old%20Scripts):

+ [shams_ordered_version.py](https://github.com/Utrosa/shams_illusion_PCBS/blob/master/Old%20Scripts/shams_ordered_version.py)
This version implements an ordered presentation of the auditory beeps from a single beep to four sequential beeps. The background is set to gray instead of black.

+ [shams_trial_version.py](https://github.com/Utrosa/shams_illusion_PCBS/blob/master/Old%20Scripts/shams_trial_version.py)
This version is similar to the final version. However, it randomizes the number of the auditory beeps by defining trials instead of functions. The background is set to gray instead of black.

#### Instructions for the Participant
The instructions are given in the English language. The response buttons are defined using the QWERTY keyboard. You may have to adapt the size of the instructions depending on the size of your screen.

#### Auditory Stimuli
The auditory beep is created in the following way:
  ```
  BEEP = stimuli.Tone(duration=BEEP_DURATION, frequency=BEEP_FREQUENCY)
  ```
 
For more advanced sound manipulations, you can have a look at the [shams_tone.py](https://github.com/Utrosa/shams_illusion_PCBS/blob/master/Tone%20Scripts/shams_tone.py) script. You will need to install the [librosa](https://librosa.org/) library to use this script. I added 3 tone examples which can be used instead of the *stimuli.tone()* function available in expyriment library.

Any externally created sound stimulus must be an *.ogg* or uncompressed *.wav* file. It can be imported to the Shams Illusion script:

  ```
  BEEP = stimuli.Audio(filename)
  ```

#### Visual Stimuli
Before running the experiment, fix the distance between the participant and the computer screen, showing the visual stimulation. Measure this distance to calculate the size of the visual flashes on the computer screen. You also have to check the resolution of the computer screen on which the visual stimuli will be presented. 

The visual flash should be subtending 2 degrees of visual angle at 5 degrees eccentricity. A useful link: https://elvers.us/perception/visualAngle/.

## Results
The results will be saved in a separate csv file for each participant.

## Contributing
Any wonderful suggestions to improve the code are very appreciated!

To suggest a wonderful feature, follow these steps:

1. Fork the Project
2. Create a new feature branch
3. Commit changes
4. Push to the branch
5. Open a pull request

## License
Distributed under the [MIT License](https://choosealicense.com/licenses/mit/). See LICENSE.txt for more information.

## Contact
Monika Utroša Škerjanec - monika.utrosa@gmail.com

Project Link: https://github.com/Utrosa/shams_illusion_PCBS

## Acknowledgments
I would like to thank my teachers [Christophe Pallier](https://github.com/chrplr) and [Maxime Cauté](https://perso.eleves.ens-rennes.fr/people/maxime.caute/) for their generous support and useful directions.
