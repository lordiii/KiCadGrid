#!C:\Program Files\KiCad\bin\python.exe
import pcbnew

inputFile = str(raw_input("Input File: "))
outputFile = str(raw_input("Output File: "))
spacing = input("Spacing: ")

# Load the board
pcb = pcbnew.LoadBoard(inputFile)

# Find the component
spacing = spacing + 5
posY = 0
conCount = 1
for i in range(0, 64):
    posX = i % 8 * spacing

    led = pcb.FindModuleByReference("LED" + str(i+1))
    led.SetPosition(pcbnew.wxPointMM(posX,posY))
    
    cap = pcb.FindModuleByReference("C" + str(i+1))
    cap.SetPosition(pcbnew.wxPointMM(posX,posY+5))
    
    if posX == (7 * spacing):
        posY = posY + spacing
    
    
# and save the file under a different name
pcb.Save(outputFile)

x = input("Done!")
exit()