# Indoor-Human-Tracking
This project presents a lightweight Tiny ML pipeline for indoor human‐position tracking using a four‐antenna UWB radar operating at 25 Hz over a 4–5 m range. Raw radar returns are preprocessed to generate Range–Angle maps, which are then fed into a compact FOMO object‐detection model. 
Trained on a dataset of spatial scenarios, the system achieves accurate centroid estimation and real‐time inference, demonstrating that UWB radar combined with Tiny ML enables privacy‐preserving, low‐power localization suitable for resource‐constrained environments.

## Radar Data Preprocessing

Initial visualization:
- Raw radar returns are represented over time vs. distance.
- This provides an intuitive view of the captured signals.
<img width="1135" height="503" alt="image" src="https://github.com/user-attachments/assets/1dd1a2cd-299f-4632-9bb6-f354de23ff66" />

These multi-antenna signals are combined through beamforming.
Like this, raw data is transformed into polar images (distance, angle), suitable for vision-based processing.
<img width="1162" height="339" alt="image" src="https://github.com/user-attachments/assets/e947f6cc-ae23-41aa-ab3d-100933e843f4" />
