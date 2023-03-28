import cv2 as cv
import argparse
from pathlib import Path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Draw index on tiles')
    parser.add_argument('filename', type=str, help='image file')
    args = parser.parse_args()

    filename = args.filename

    img = cv.imread(filename, cv.IMREAD_UNCHANGED)

    h,w = img.shape[0:2]
    
    gridSize = 32

    textColor = (0, 0, 255, 255)

    index = 0
    for y in range(0, h, gridSize):
        for x in range(0, w, gridSize):
            tile = img[y:y+gridSize, x:x+gridSize]
            if tile[:,:,3].sum() == 0:
                continue
            cv.putText(tile, f"{index}", (0, gridSize-1), cv.FONT_HERSHEY_SIMPLEX, 0.5, textColor, 1, cv.LINE_AA)
            img[y:y+gridSize, x:x+gridSize] = tile
            index += 1

    dir = Path(filename).parent
    base = Path(filename).stem
    ext = Path(filename).suffix
    output_path = dir/(base+"_index"+ext)

    print(f"output to {output_path}")

    cv.imwrite(str(output_path), img)
