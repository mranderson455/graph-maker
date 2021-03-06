import turtle
import os
import random as r
from time import gmtime, strftime
import json

settings = {}

with open("settings.json", "r") as f:
  settings = json.load(f)

print(settings)
# Values initialization.
t = turtle.Turtle()
t.speed(0)
t.pensize(1)
t.ht()
graphName = settings.get("graphName")
dataSet = settings.get("dataSet")
xVals = settings.get("xVals")
graphOrigin = settings.get("graphOrigin")
xTextPadding = settings.get("xTextPadding")
yTextPadding = settings.get("yTextPadding")
xSize = settings.get("xSize")
ySize = settings.get("ySize")
yIterations = settings.get("yIterations")
startVal = settings.get("startVal")
iterationMult = settings.get("iterationMult")
lineColor = settings.get("lineColor")

# Intial settings json file writing
# settings = {"graphName": "My Graph", "dataSet": [1, 2, 3, 4, 5], "xSize": 500, "ySize": 500, "xVals": [2001, 2002, 2003, 2004, 2005], "graphOrigin": [0, 0], "xTextPadding": -3, "yTextPadding": -15}

# Finds smallest integer in an array.
def findLargestInt(vals):
  # Start with max value being first value.
  maxVal = vals[0]


  # If next value is bigger, make that the max, until array is done, then return.
  for i in range(1, len(vals)):
    if vals[i] > maxVal:
      maxVal = vals[i]
  
  return maxVal


# Finds largest integer in an array.
def findSmallestInt(vals):
  # Start with max value being first value.
  minVal = vals[0]


  # If next value is bigger, make that the max, until array is done, then return.
  for i in range(1, len(vals)):
    if vals[i] < minVal:
      minVal = vals[i]
  
  return minVal


class Graph:
  # Constructor
  def __init__(self, title="My Graph"):
    self.title = title


  #
  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  # !! Whole graphing function !!
  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  #
  def graphCreate(self, xSize, ySize, vals, color="black", yIterations=0, customX=None, startVal=1, iterationMult=1):
    print("Generating...")
    # Value intializing.
    maxVal = findLargestInt(vals)
    minVal = findSmallestInt(vals)
    graphOrigin = [-xSize / 2, -ySize / 2]
    pointPositions = []


    # Auto yIterations.
    if yIterations == 0:
      yIterations = int(round(ySize / 50.0))


    # Custom x-axis check.
    if customX is not None:
      if len(customX) != len(vals):
        customX = None
        print("Incorrect amount of custom x values. Setting x axis to default...")


    # Center.
    t.up()
    t.goto(graphOrigin)
    

    # Draw box.
    print("Drawing frame... ", end = '')
    try:
      t.down()
      for i in range(4):
        # if number is even go on the x-size otherwise go y-size
        if i % 2 == 0:
          t.fd(xSize)
        else:
          t.fd(ySize)

        t.lt(90)
    except:
      print("Error")
    else:
      print("Done")

    
    # Go back to origin and move 10px down.
    t.up()
    t.goto(graphOrigin)
    t.sety(t.pos()[1] + yTextPadding)
    yNumPos = t.pos()[1]


    # Write values at intervals of (graph width / array length - 1).
    # Ex: width is 100px and there are 5 values.
    # 100 / 4 = 25
    # Go forward at 25px intervals 4 times.
    # We do this because we have already printed zero.
    print("Drawing x-axis... ", end = '')
    try:
      for i in range(len(vals)):
        # Custom x values
        if customX is None:
          t.write(startVal + (i * iterationMult), align="center")
        else:
          t.write(customX[i], align="center")
        t.fd(float(xSize) / (len(vals) - 1))
        # Vertical grid.
        if i != len(vals) - 1:
          t.sety(t.pos()[1] - yTextPadding)
          t.down()
          t.sety(ySize + graphOrigin[1])
          t.up()
          t.sety(yNumPos)
    except:
      print("Error")
    else:
      print("Done")


    # Go back to origin and face up.
    t.goto(graphOrigin)
    t.down()
    t.lt(90)


    # Set tallest point of graph.
    maxHeight = t.pos()[1]
    

    # Go back to origin and move 3px left.
    t.up()
    t.goto(graphOrigin)
    t.setx(t.pos()[0] + xTextPadding)
    xNumPos = t.pos()[0]
   

    # Write values at intervals of 1/8th the height.
    # The actual value to write will be 1/8, then 2/8, and so on... of the highest value.
    print("Drawing y-axis... ", end = '')
    try:
      if minVal >= 0:
        t.write(0, align="right")
      else:
        t.write(minVal, align="right")
      for i in range(yIterations):
        t.fd(ySize / float(yIterations))
        if minVal >= 0:
          t.write(round(maxVal / float(yIterations) * (i + 1), 2), align="right")
        else:
          t.write(round((abs(maxVal) + abs(minVal)) / float(yIterations) * (i + 1) + minVal, 2), align="right")
          print(t.pos())
        # Horizontal grid
        if (i != yIterations - 1):
          t.setx(t.pos()[0] - xTextPadding)
          t.down()
          t.setx(xSize + graphOrigin[0])
          t.up()
          t.setx(xNumPos)
    except:
      print("Error")
    else:
      print("Done")


    # Go back to origin.
    t.goto(graphOrigin)
    t.down()


    # Change line color :)
    t.color(lineColor)


    # Initialize graph values and put point at beginning value.
    t.pensize(1)
    t.up()
    if minVal >= 0:
      t.goto(graphOrigin[0], (vals[0] * (ySize / float(maxVal))) + graphOrigin[1])
    else:
          t.goto(graphOrigin[0], (vals[0] * (ySize / float(abs(maxVal) + abs(minVal))) + graphOrigin[1] + (ySize / 2 + abs(maxVal))))
    t.down()


    # Graph the points by setting the pen-x to same intervals used in writing, but using different
    # math as we are setting the position rather than moving a set amount.
    #
    # For the pen-y we first get ratio by dividing the height by the highest value, then applying
    # that ratio to each value within the data-set, and finally making it relative to the new-origin.
    print("Graphing points... ", end='')
    try:
      for i in range(len(vals)):
        if minVal >= 0:
          t.goto(graphOrigin[0] + (i * (float(xSize) / (len(vals) - 1))), (vals[i] * (ySize / float(maxVal))) + graphOrigin[1])
        else:
          t.goto(graphOrigin[0] + (i * (float(xSize) / (len(vals) - 1))), (vals[i] * (ySize / float(abs(maxVal) + abs(minVal))) + graphOrigin[1] + (ySize / 2 + abs(maxVal))))
          # t.goto(graphOrigin[0] + (i * (float(xSize) / (len(vals) - 1))), (vals[i] * (ySize / (abs(minVal) + abs(maxVal)))) + graphOrigin[1] + (abs(maxVal) * abs(minVal)))
        t.dot(5, lineColor)
        # Return point's positions
        # pointPositions.append([t.pos()[0], t.pos()[1]])
    except:
      print("Error")
    else:
      print("Done")
    

    # Write title above graph.
    print("Writing title... ", end='')
    try:
      t.color("black")
      t.up()
      padding = 20
      t.goto(0, ySize / 2 + padding)
      t.write(self.title, align="center", font=("Arial", 16, "normal"))
    except:
      print("Error")
    else:
      print("Done")


    # Saving to TKinker
    cv = t.getscreen().getcanvas()

    print("***** Graph generated *****")

    return cv


  # Save the turtle file.
  def saveTurtle(self, cv):
    try:
      ID = strftime("%H%M%S", gmtime())
      fileName = self.title + " " + ID + ".ps"
      cv.postscript(file=fileName, colormode='color')
      os.rename("/Users/sam4545/Downloads/Coding/Python/Projects/graph-maker/" + fileName, "/Users/sam4545/Downloads/Coding/Python/Projects/graph-maker/imgs/" + fileName)
      # print(os.listdir())
    except:
      print("Error occured file not saved properly")
    else:
      print("Successfully saved [" + fileName + "] to imgs folder!" )

    return fileName


# Initialize.
graph = Graph(graphName)

# Intial settings json file writing
# with open('settings.json', 'w') as f:
#   json.dump(settings, f, indent=4)

cv = graph.graphCreate(xSize, ySize, dataSet, color=lineColor, yIterations=yIterations, customX=xVals, startVal=startVal, iterationMult=iterationMult)

kb = input("\nDo you want to save the file? (y/n): ")

if "y" in kb.lower():
  print("Saving... ", end="")
  file = graph.saveTurtle(cv)