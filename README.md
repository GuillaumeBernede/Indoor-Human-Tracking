# Indoor-Human-Tracking
This project presents a lightweight Tiny ML pipeline for indoor human‐position tracking using a four‐antenna UWB radar operating at 25 Hz over a 4–5 m range. Raw radar returns are preprocessed to generate Range–Angle maps, which are then fed into a compact FOMO object‐detection model. 

Trained on a dataset of spatial scenarios, the system achieves accurate centroid estimation and real‐time inference, demonstrating that UWB radar combined with Tiny ML enables privacy‐preserving, low‐power localization suitable for resource‐constrained environments.

## Radar Data Preprocessing

Initial visualization:
- Raw radar returns are represented over time vs. distance.
- This provides an intuitive view of the captured signals.
<img width="1135" height="503" alt="image" src="https://github.com/user-attachments/assets/1dd1a2cd-299f-4632-9bb6-f354de23ff66" />

These multi-antenna signals are combined through beamforming (UWB_beamforming.ipynb)
Like this, raw data is transformed into polar images (distance, angle), suitable for vision-based processing.
<img width="1162" height="339" alt="image" src="https://github.com/user-attachments/assets/e947f6cc-ae23-41aa-ab3d-100933e843f4" />

## FOMO Architecture for Lightweight Object Detection

The angle–distance maps are processed by a FOMO (Faster Objects, More Objects) architecture, specifically designed for TinyML:
- Outputs heatmaps of centroids for object localization.
- Prioritizes low latency and high efficiency, ideal for embedded platforms.

### Model Optimizations

The model was then optimised using various techniques.
The model leverages [mobilenetv2](https://arxiv.org/pdf/1801.04381) but only keeps its first three layers, followed by a custom FOMO head. Several compression and optimization techniques were applied:

- Input downscaling: from 310×308 to 96×96.
- Pruning: removal of ~30% redundant weights.
- Conv2D + ReLU fusion: faster inference.
- Quantization Aware Training (QAT): preserves accuracy during quantization.
- Post Training Quantization (PTQ): converts weights to int8.
- Export to TensorFlow Lite for on-device deployment.

## Final results:

**Model size: ~24 KB**

**RAM usage: ~ 500KB**
<img width="1094" height="329" alt="image" src="https://github.com/user-attachments/assets/3e67c254-9154-456c-95b8-202fb065f8e6" />

This project demonstrates how UWB radar + TinyML can achieve accurate, real-time indoor tracking with a model size under 25 KB.

It enables privacy-preserving, low-power localization, making it ideal for resource-constrained IoT and embedded devices.

## Project structure
