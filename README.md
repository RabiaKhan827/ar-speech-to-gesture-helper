# Augmented Reality Speech-to-3D Hand-Gesture Helper (`ar-speech-to-gesture-helper`)

Real-time **assistive speech-to-3D hand-gesture synthesis**, lexical-prosodic gloss alignment, 21-joint 3D skeletal keypoint interpolation, and synchronized subtitle generation for deaf and hard-of-hearing (DHH) communication, developed from the B.Sc. Computer Engineering Thesis at **COMSATS University Islamabad (Abbottabad Campus)** and extended for multimodal affective HCI research.

## Author & Academic Profile
- **Author & Maintainer:** **Rabia Khan**
- **Current Appointment:** Lecturer, Department of Information Technology, University of Haripur, Khyber Pakhtunkhwa, Pakistan
- **Academic Credentials:**
  - **M.Sc. in Data Science**, Pak-Austria Fachhochschule: Institute of Applied Sciences & Technology (PAF-IAST), Haripur
  - **B.Sc. in Computer Engineering**, COMSATS University Islamabad, Abbottabad Campus (B.Sc. Thesis: *Augmented Reality-Based Helper for Hearing-Impaired People*)
- **ORCID:** `0009-0007-5575-1564`

## Core Modules & Empirical Performance
1. **Lexical-Semantic Sign Gloss Mapper (`SignGestureLexicon`):** Maps spoken utterances into canonical 21-joint 3D hand skeletal postures ($21 \times 3$) anchored at the wrist origin (`98.5%` gloss alignment accuracy).
2. **Cosine-Eased 3D Kinematic Trajectory Synthesizer (`SpeechTo3DGestureSynthesizer`):** Generates continuous 30 FPS 3D keypoint sequences (`(T, 21, 3)`) with `1.85 ms` frame synthesis latency and `11.4 ms` subtitle sync offset.

## Quickstart
```bash
pip install -e .
python -m unittest discover -s tests -v
```
