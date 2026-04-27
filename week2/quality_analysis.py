import numpy as np
import matplotlib.pyplot as plt

labels = [
    "Functional",
    "Performance",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]

ytmusic = [4, 4, 4, 3, 4, 4, 4, 4]
spotify = [3, 4, 5, 4, 4, 3, 4, 5]

ytmusic += ytmusic[:1]
spotify += spotify[:1]

angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
angles = np.concatenate((angles, [angles[0]]))

plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)

ax.plot(angles, ytmusic, label="YouTube Music")
ax.fill(angles, ytmusic, alpha=0.1)

ax.plot(angles, spotify, label="Spotify")
ax.fill(angles, spotify, alpha=0.1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

ax.set_title("Quality Profile Comparison")
ax.legend()

plt.savefig("quality_radar.png")
plt.show()