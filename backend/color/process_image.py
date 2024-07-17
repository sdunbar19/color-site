from PIL import Image as Img
import numpy as np
import colorsys
from sklearn.cluster import KMeans
import math

def process(image_path):
    MIN_CLUSTERS = 2
    MAX_CLUSTERS = 14
    MAX_RESOLUTION = 1000
    img = Img.open(image_path)
    width, height = img.size
    resolution = width * height
    if resolution > MAX_RESOLUTION:
        scale = math.sqrt(MAX_RESOLUTION) / math.sqrt(resolution)
        new_width = width * scale
        new_height = height * scale
        img = img.resize((int(new_width), int(new_height)))
    img2 = img.convert('HSV')
    hsv_array = np.asarray(img2) # values between 0 and 255
    hsv_array_new = np.zeros((hsv_array.shape[0] * hsv_array.shape[1], 3))
    for i in range(hsv_array.shape[0]):
        for j in range(hsv_array.shape[1]):
            for k in range(3):
                idx = i * hsv_array.shape[1] + j
                hsv_array_new[idx][k] = hsv_array[i][j][k]
    clusters_to_colors = {}
    for n in range(MIN_CLUSTERS, MAX_CLUSTERS + 1):
        kmeans = KMeans(n_clusters=n, random_state=0, n_init="auto").fit(hsv_array_new)
        labels = kmeans.predict(hsv_array_new)
        centers = kmeans.cluster_centers_
        counts = [0 for _ in range(len(centers))]
        for label in labels:
            counts[label] += 1
        clusters_to_colors[n] = []
        centers_counts = [(centers[i], counts[i]) for i in range(len(centers))]
        centers_counts.sort(key = lambda x: x[0][0])
        for (center, count) in centers_counts:
            rgb = colorsys.hsv_to_rgb(center[0]/float(255), center[1]/float(255), center[2]/float(255))
            hexa = '#%02x%02x%02x' % (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
            clusters_to_colors[n].append((hexa, center, count, len(labels)))
    return {'data': clusters_to_colors}