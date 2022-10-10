import simplestereo as ss
import os


# Paths
curPath = os.path.dirname(os.path.realpath(__file__))
loadPath = os.path.join(curPath,"res","4L","calib-10")    # Image folder
saveFile = os.path.join(curPath,"res","4L","rig.json") # Destination

# Total number of images
N_IMAGES = 30

# Image paths
images = [ ( os.path.join(loadPath,str(i)+'_L.png')) for i in range(N_IMAGES) ]
print(f"Calibrating using {len(images)} images from:\n{loadPath}...")
#images = [loadPath, "0_L.png","1_L.png","2_L.png"]

# Calibrate and build StereoRig object
rig = ss.calibration.chessboardSingle(images, chessboardSize=(7,6), squareSize=27.0)

# Save rig object to file
rig.save("myRig.json")

# Optionally print some info
print("Reprojection error:", rig.reprojectionError)
print("Centers:", rig.getCenters())
print("Baseline:", rig.getBaseline())