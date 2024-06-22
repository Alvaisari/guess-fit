# Overview
This application demonstrates the subjectiveness of manual peak fitting and was created to highlight the importance of using objective tools for accurate results (and also for fun).
The app allows users to guess peak positions on a generated signal and then compares the manual fit with true values.

The application is built using Python's Tkinter for the GUI, Matplotlib, and Scipy fitting routine.

# Features
- Generate signal: Creates a signal with a linear background, up to 5 Gaussian peaks, and some noise.
- Interactive Plotting: Users can click on the plot to mark their guessed peak positions.
- Fit Signal: Compares the user's guesses to ground truth.
- Reset and New Spectrum: Options to reset the guesses or generate a new signal.

<img src="https://github.com/Alvaisari/guess-fit/assets/70195045/bf2e539c-32c6-4e45-b1fd-28b863aceb04" width="500">

# Installation
Clone the Repository:

```
git clone https://github.com/Alvaisari/guess-fit.git
cd spectrum-fitting-app
```
Ensure you have Conda installed, then create the environment:
```
conda env create -f environment.yml
conda activate guess-fit
```
Then run the app:
```
python main.py
```
# Usage
- Click the "New Spectrum" button to generate a new spectrum.
- Click on the plot to add markers where you think the peaks are located.
- Click the "Fit" button to see how well your guessed positions match the objectively fitted peaks.
- Click the "Reset" button to clear your guesses and start over.

# Dependencies
Dependencies are included in the provided environment.yml file.
