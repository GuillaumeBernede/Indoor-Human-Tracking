# convert_tf_to_tflite.py
import tensorflow as tf


# Load SavedModel
converter = tf.lite.TFLiteConverter.from_saved_model("saved_model96p01")

# Optimizations
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Convert
tflite_model = converter.convert()

with open("fomo96p01.tflite", "wb") as f:
    f.write(tflite_model)
