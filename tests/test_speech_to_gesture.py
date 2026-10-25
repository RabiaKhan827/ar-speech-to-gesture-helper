import unittest
import numpy as np
from speech_to_gesture import SignGestureLexicon, SpeechTo3DGestureSynthesizer

class TestSpeechToGesture(unittest.TestCase):
    def test_posture_and_trajectory(self):
        pose = SignGestureLexicon.get_canonical_posture("GREET_OPEN_PALM")
        self.assertEqual(pose.shape, (21, 3))
        synth = SpeechTo3DGestureSynthesizer(fps=30, frames_per_token=10)
        traj = synth.synthesize_trajectory("Hello please help")
        self.assertEqual(traj.shape, (30, 21, 3))
        rep = synth.run_benchmark()
        self.assertGreaterEqual(rep.gloss_alignment_accuracy, 0.95)

if __name__ == "__main__":
    unittest.main()
