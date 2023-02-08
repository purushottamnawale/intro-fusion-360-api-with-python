# Author-
# Description-

import adsk.core
import adsk.fusion
import adsk.cam
import traceback


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        
        pName = 'Width'
        pUnit = 'mm'
        pExpression = 5.0/10
        pExpressionReal = adsk.core.ValueInput.createByReal(pExpression)

        design.userParameters.add(pName, pExpressionReal, pUnit, "")

        ui.messageBox('Check the params')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
