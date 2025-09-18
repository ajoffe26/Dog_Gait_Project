"""
extract_frames.py
Extract frames from a standardized video and save them as images.
python ml/preprocessing/extract_frames.py data/processed/healthy/dog1.mp4 data/frames/healthy/dog1
"""

import cv2
import os
import argparse

def extract_frames(video_path, out_dir, every_n=1):
    os.makedirs(out_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_idx, saved_idx = 0, 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % every_n == 0:
            frame_file = os.path.join(out_dir, f"frame_{saved_idx:04d}.jpg")
            cv2.imwrite(frame_file, frame)
            saved_idx += 1
        frame_idx += 1

    cap.release()
    print(f"[OK] Extracted {saved_idx} frames → {out_dir}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("video", help="Path to standardized video")
    parser.add_argument("out_dir", help="Folder to save frames")
    parser.add_argument("--every_n", type=int, default=1,
                        help="Save every Nth frame (default=1 for all)")
    args = parser.parse_args()

    extract_frames(args.video, args.out_dir, args.every_n)

if __name__ == "__main__":
    main()
