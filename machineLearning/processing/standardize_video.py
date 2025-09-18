"""
standardize_video.py
Make all videos the same resolution and FPS for consistency.
python ml/preprocessing/standardize_video.py data/raw/healthy/dog1.mp4 data/processed/healthy/dog1.mp4
"""

import cv2
import argparse
import os

def standardize_video(input_path, output_path, fps=30, resolution=(224, 224)):
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, resolution)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, resolution)
        out.write(frame)

    cap.release()
    out.release()
    print(f"[OK] Standardized video saved → {output_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to raw video")
    parser.add_argument("output", help="Path to save standardized video")
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--width", type=int, default=224)
    parser.add_argument("--height", type=int, default=224)
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    standardize_video(args.input, args.output, args.fps, (args.width, args.height))

if __name__ == "__main__":
    main()
