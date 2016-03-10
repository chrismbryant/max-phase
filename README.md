# File-parsing

Gathering info from file name:

Hi Chris,

I’m sending you our SNFactory data. This is data our group took several years to gather. It is still not public (so don’t publish it anywhere and keep it safe). I want you to unzip this file and write a little code to select SNe at max from the training/ folder. For our purposes, we will define at max SNe as supernovae that have their phase -1< phase <1.

Inside the training/ folder, each folder is a supernova. Inside that folder, you find files like these ones: SNF20071108-021_P036042_restframe.fits. You only care about finding at max files for _restframe.fits extensions.

The number P036042 is what contains the phase info for the file. P stands for plus, M for minus. And the decimal point goes in the middle: 036.042. Therefore, the phase for SNF20071108-021_P036042_restframe.fits is +36.042, so it is not at max.

So write up that as a script (a .py file) and push it to GitHub. We will work on this file together remotely. I’ll come back up once more before one to explain this better.

Have fun!

Caroline
