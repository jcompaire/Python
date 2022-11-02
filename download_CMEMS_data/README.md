## A Python script to exemplify how to download CMEMS data via OpenDAP as netCDF files within the Spyder environment.

Currently, there are 69 ocean-related available variables to download from CMEMS ( https://resources.marine.copernicus.eu/products ). You will find different "branches" of the "same variable" depending on the data source, the temporal resolution and coverage or even the processing state of data, among others.

### To download CMEMS data you have to:
1. Create an account in CMEMS https://resources.marine.copernicus.eu/registration-form
2. Select the desired product from https://resources.marine.copernicus.eu/products 
3. Once selected you will have to choose the option "SUBS". There you will be able to select the desired parameter/s, subset the region and the dates of interest.
4. Now, do not click on "Download", you have to select the button with these symbols: "</>", and copy the script template. (Briefly, the template contains the desired product subsetted by your preference).

### Now you have two options:
-  Run the copied script template on your own terminal to download data in a local folder.
-  Use your own script created through the Spyder environment.

I don't know about you, but I prefer the last option because I like to see the variables in the "variable explorer" tab. Besides that, in that way,
I can share the script with colleagues or even with journal referees (ensuring one of the major principles underpinning the scientific method: reproducibility). They only need to have a CMEMS account to replicate it.

### If you share this point of view, these are the following next steps:
1. Put the script "cmems_motu.py" in your working directory (this script was created by Copernicus Marine User Support). https://help.marine.copernicus.eu/en/articles/5211063-how-to-use-the-motuclient-within-python-environment-e-g-spyder
   (I have modified two lines (38 and 44) to allow us to save the data in the desired path).
2. Install the module PWInput.
3. Check some of the attached scripts, and customize them according to your preference.

In these examples, you will see how to download some data on:
- 'sst': sea surface temperature (get_cmems_sst.py)
- 'ssh': sea surface height (get_cmems_ssh.py)
- 'chl': chlorophyll-a (get_cmems_chl.py)

for the area of the Rio de la Plata estuary (southern Atlantic Ocean) using the Spyder environment.

4. The module PWInput that displays asterisks for password input does not work within Spyder. This is a limitation of Spyder/QtConsole, not of PWInput     itself. So, to run inside Spyder. You need to go to Run > Configuration per file > Console and select the option called Execute in an external terminal to use an external terminal instead https://stackoverflow.com/questions/45814910/data-hiding-for-python-qtconsole#comment78607781_45814910 Depending on your OS, the shortcut will be Ctrl+F6 or Cmd+F6.

A terminal window will pop up asking you to write your CMEMS user's name and password. Then, the download process will start, and when is finished,    the pops up window will close automatically.

## That's it!
With this code, you are able to download data from CMEMS within the Spyder environment hiding your personal information, which is ideal if you want to
share the script with colleagues.

![alt text](https://github.com/jcompaire/Python/blob/main/images/Fig_sst_ssh_chl.png?raw=true)
