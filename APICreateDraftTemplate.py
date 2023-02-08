#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design=adsk.fusion.Design.cast(app.activeProduct)

        defaultInputNumber='5 deg'
        defaultInputName='Diameter'

        draftAngle=2
        draftName='Draft'
        thicknessValue=2
        thicknessName='WallThickness'
        internalWallThickness=thicknessValue*0.6
        internalWallTName="InternalWallThickness"

        unitsMgr=design.unitsManager

        draftAngleReal=unitsMgr.evaluateExpression(str(draftAngle),'deg')
        thicknessValueReal=unitsMgr.evaluateExpression(str(thicknessValue),unitsMgr.defaultLengthUnits)
        internalWallThicknessReal=unitsMgr.evaluateExpression(str(internalWallThickness),unitsMgr.defaultLengthUnits)


        realDraft=adsk.core.ValueInput.createByReal(draftAngleReal)
        realThickness=adsk.core.ValueInput.createByReal(thicknessValueReal)
        realWallT=adsk.core.ValueInput.createByReal(internalWallThicknessReal)

        design.userParameters.add(draftName,realDraft,'deg','')
        design.userParameters.add(thicknessName,realThickness,unitsMgr.defaultLengthUnits,'')
        design.userParameters.add(internalWallTName,realWallT,unitsMgr.defaultLengthUnits,'')
        
        # newInputName=ui.inputBox("Enter a new User Parametere Name: ", "New User Parameter",defaultInputName)
        # newInputNumber=ui.inputBox("Enter a User Parameter Value: ","New User Parameter",defaultInputNumber)

        # unitsMgr=design.unitsManager
        # realInputNumber=unitsMgr.evaluateExpression(newInputNumber[0],unitsMgr.defaultLengthUnits)
        # realInputNumber=unitsMgr.evaluateExpression(newInputNumber[0],'deg')
        # realValueInput=adsk.core.ValueInput.createByReal(realInputNumber)

        # design.userParameters.add(newInputName[0],realValueInput,unitsMgr.defaultLengthUnits,'')
        # design.userParameters.add(newInputName[0],realValueInput,'deg','')

        ui.messageBox('Success')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
