import airsim
import matplotlib.pyplot as plt
import numpy as np


client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# take images
responses = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.Scene, False, False),
    airsim.ImageRequest("1", airsim.ImageType.DepthPlanner, True)])
response = responses[0]

# get numpy array
img1d = np.frombuffer(response.image_data_uint8, dtype=np.uint8)

# reshape array to 4 channel image array H X W X 4
img_rgb = img1d.reshape(response.height, response.width, 3)

# original image is fliped vertically
# img_rgb = np.flipud(img_rgb)

# print(responses[0])
plt.imshow(img_rgb)
plt.show()
# client.takeoffAsync().join()
# client.moveToPositionAsync(-10, 10, -10, 5).join()
