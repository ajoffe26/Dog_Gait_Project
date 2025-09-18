"""
extract_keypoints.py
Extract pose keypoints from frames using Mediapipe Pose.
Saves to a CSV (x,y,z,visibility for each landmark).
python ml/preprocessing/extract_keypoints.py data/frames/healthy/dog1 data/keypoints/healthy/dog1.csv
"""

import cv2
import os
import argparse
import mediapipe as mp
import pandas as pd

def extract_keypoints_from_frames(frame_dir, out_csv):
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True)
    results_list = []

    for frame_file in sorted(os.listdir(frame_dir)):
        if not frame_file.endswith(".jpg"):
            continue
        img_path = os.path.join(frame_dir, frame_file)
        image = cv2.imread(img_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            row = []
            for lm in results.pose_landmarks.landmark:
                row.extend([lm.x, lm.y, lm.z, lm.visibility])
            results_list.append(row)

    df = pd.DataFrame(results_list)
    df.to_csv(out_csv, index=False)
    print(f"[OK] Keypoints saved → {out_csv}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("frame_dir", help="Folder with extracted frames")
    parser.add_argument("out_csv", help="Path to save keypoints CSV")
    args = parser.parse_args()

    extract_keypoints_from_frames(args.frame_dir, args.out_csv)

if __name__ == "__main__":
    main()
