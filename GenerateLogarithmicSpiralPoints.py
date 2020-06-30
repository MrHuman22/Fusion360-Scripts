#Author-Peter Newman
#Description-Generates an archemedes spiral

import adsk.core, adsk.fusion, adsk.cam, traceback
from math import cos, sin, pi, exp

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        des = adsk.fusion.Design.cast(app.activeProduct)
        root = des.rootComponent
        sk = root.sketches.add(root.xYConstructionPlane)
        points = adsk.core.ObjectCollection.create()
        numTurns = 2
        pointsPerTurn = 40
        a = 1
        b = 1
        theta = 0
        offset = 0
        ui.messageBox(f'Creating archimedes spiral with {numTurns} turns, offset from (0,0,0) by {offset}, {pointsPerTurn} points per turn')
        for i in range(pointsPerTurn * numTurns + 1):
            r = a * exp(b*theta)
            x = r*cos(theta)
            y = r*sin(theta)
            points.add(adsk.core.Point3D.create(x,y,0))
            theta += pi * 2 / pointsPerTurn # iterate theta
        sk.sketchCurves.sketchFittedSplines.add(points)
        ui.messageBox('Complete!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))