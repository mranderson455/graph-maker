import turtle

# Values initialization.
t = turtle.Turtle()
t.speed(0)
t.pensize(1)
t.ht()
dataSet = [1, 20, 45, 41, 123, 23, 70, 899, 40, 67]
xVals = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
graphOrigin = [0, 0]
xTextPadding = -3
yTextPadding = -15


# Finds largest integer in an array.
def findLargestInt(vals):
  # Start with max value being first value.
  maxVal = vals[0]


  # If next value is bigger, make that the max, until array is done, then return.
  for i in range(1, len(vals)):
    if vals[i] > maxVal:
      maxVal = vals[i]
  
  return maxVal


# Whole graphing function.
def graphInit(xSize, ySize, vals, title="My Graph", color="black", yIterations=0, customX=None, startVal=1, iterationMult=1):
  print("Generating...")
  # Value intializing.
  maxVal = findLargestInt(vals)
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
    t.pensize(0.1)
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
  t.pensize(1)
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
    t.pensize(0.1)
    t.write(0, align="right")
    for i in range(yIterations):
      t.fd(ySize / float(yIterations))
      # Horizontal grid
      if (i != yIterations - 1):
        t.setx(t.pos()[0] - xTextPadding)
        t.down()
        t.setx(xSize + graphOrigin[0])
        t.up()
        t.setx(xNumPos)
      t.write(round(maxVal / float(yIterations) * (i + 1), 2), align="right")
  except:
    print("Error")
  else:
    print("Done")


  # Go back to origin.
  t.goto(graphOrigin)
  t.down()
  t.pensize(1)


  # Change line color :)
  t.color(color)


  # Initialize graph values and put point at beginning value.
  t.pensize(2)
  t.up()
  t.goto(graphOrigin[0], (vals[0] * (ySize / float(maxVal))) + graphOrigin[1])
  t.down()


  # Graph the points by setting the pen-x to same intervals used in writing, but using different
  # math as we are setting the position rather than moving a set amount.
  #
  # For the pen-y we first get ratio by dividing the height by the highest value, then applying
  # that ratio to each value within the data-set, and finally making it relative to the new-origin.
  print("Graphing points... ", end='')
  try:
    for i in range(len(vals)):
      t.goto(graphOrigin[0] + (i * (float(xSize) / (len(vals) - 1))), (vals[i] * (ySize / float(maxVal))) + graphOrigin[1])
      t.dot(5, "black")
      # Return point's positions
      pointPositions.append([t.pos()[0], t.pos()[1]])
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
    t.write(title, align="center", font=("Arial", 16, "normal"))
  except:
    print("Error")
  else:
    print("Done")


  print("***** Graph generated *****")

  return pointPositions


# Initialize.
points = graphInit(500, 500, dataSet, title="Num. of Gibson Guitars in Circulation", startVal=10, iterationMult=0.5)

input()