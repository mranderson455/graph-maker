# graph-maker

### Graph-Maker Functions:
* Create a full fledged line-graph
* Change the length or width
* Change the x-axis to have default values (1, 2, 3, etc.) or put in your own (2001, 2002, 2010, etc.)
* Automatic scaling
* Saving of images (currently postscript so you have to open in another program like GIMP)

### How it works:
* All the drawing functionality is based in turtle
* TKinter to save images

### To do:
* Make negatives work with the y-values
* Add more graph types

### Tips:
* Saved images are in the /imgs/ folder
* All settings can be edited in settings.json
* Best padding: x = -3, y = -15
* Generally 500 by 500 is the biggest size you need
* Set yIterations to 0 to automatically produce a visually appealing number of y-values
* Set xVals to an empty list to make auto-generated x-values
* When using auto-generated xVals, use startVal as the starting number and iterationMult for the increment amount
* The graph by default goes from 0 to the highest value in the dataSet
* Negative values are not fully functional and will cause visual errors

Created by Samuel Anderson