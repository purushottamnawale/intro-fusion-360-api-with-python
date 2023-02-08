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
        defaultInput = '5 mm'
        newInput = ui.inputBox("Enter a new input value :",
                               "New Input Value", defaultInput)

        if newInput[0]:
            (defaultInput, isCanceled) = newInput
        if isCanceled:
            return
        unitMgr = design.unitsManager
        try:
            realInput = unitMgr.evaluateExpression(defaultInput, "mm")
            isValid = True
        except:
            ui.messageBox('"'+defaultInput,'"is not a valid length expression."','Invalid',adsk.core.MessageBoxButtonTypes.OKButtonType,adsk.core.MessageBoxIconTypes.CriticalIconType)
            isValid=False
        ui.messageBox('Input'+defaultInput+' result: '+str(realInput)) 

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
