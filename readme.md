# Replication of the Shams' Illusion

## About the Project
In 2002 Japanese researchers asked naive observers how many visual flashes were presented on the screen when these flashes were accompanied by different number of beeps on each trial. The results demonstrate that auditory stimulation can induce a visual illusion which has been named by the first author Dr Ladan Shams.

#### The Original Paper
Ladan Shams, Yukiyasu Kamitani, Shinsuke Shimojo, Visual illusion induced by sound, Cognitive Brain Research, Volume 14, Issue 1, 2002, Pages 147-152, ISSN 0926-6410, https://doi.org/10.1016/S0926-6410(02)00069-1.

##### Abstract
We present the first cross-modal modification of visual perception which involves a phenomenological change in the quality—as opposed to a small, gradual, or quantitative change—of the percept of a non-ambiguous visual stimulus. We report a visual illusion which is induced by sound: when a single flash of light is accompanied by multiple auditory beeps, the single flash is perceived as multiple flashes. We present two experiments as well as several observations which establish that this alteration of the visual percept is due to cross-modal perceptual interactions as opposed to cognitive, attentional, or other origins. The results of the second experiment also reveal that the temporal window of these audio–visual interactions is approximately 100 ms.
Keywords: Crossmodal interaction; Auditory–visual interaction; Visual illusion; Illusory flashing; Multisensory integration; Audio–visual perceptio

## Aim
This project was part of the [Programming for Cogitive and Brain Sciences](https://pcbs.readthedocs.io/en/latest/) (PCBS) course taught at the Cogmaster. My goal was to replicate the experimental task reported in Shams et al. (2002) with the [Expyriment](https://expyriment.org/) python library to enable fast and simple replication of the experiment.

## Getting Started
Clone the repository:

  ```
  git clone https://github.com/Utrosa/shams_illusion_PCBS.git
  ```
  
### Prerequisites
To run the code successfully on your local computer, you will need to have installed python, anaconda, and the expyriment libarary.

To intall expyriment enter the following to your command line:

  ```
  pip install expyriment
  ```
  
### Running the Experiment

#### Auditory Stimuli
The auditory beeps are created in the following way:
  ```
  BEEP = stimuli.Tone(duration=BEEP_DURATION, frequency=BEEP_FREQUENCY)
  ```
For more advanced sound manipulations, you can have a look at the [Tone script](). You will need to install the [librosa](https://librosa.org/) library to use these scripts.

#### Visual Stimuli
Fix the distance between the screen and the participant.
Measure the distance and calculate the size of the visual stimulation

## Results
Results will be saved in a csv file per participant.

## Contributing
Any wonderful suggestions to improve the code are very appreciated!

To add a great suggestion, follow these steps:

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
I would like to thank my teachers [Christophe Pallier](https://github.com/chrplr) and [Maxime Cauté](https://perso.eleves.ens-rennes.fr/people/maxime.caute/) for their generous support and usefull directions.
