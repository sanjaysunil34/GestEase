import csv
import copy
import argparse
import itertools

import cv2 as cv
import numpy as np
import mediapipe as mp

import os
from database import write_keys
from train_example1 import training

dirname = os.path.dirname(__file__)
filename_keypoint = os.path.join(dirname, 'model/keypoint_classifier/keypoint_classifier_label.csv')

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)

    parser.add_argument('--use_static_image_mode', action='store_true')
    parser.add_argument("--min_detection_confidence",
                        help='min_detection_confidence',
                        type=float,
                        default=0.7)
    parser.add_argument("--min_tracking_confidence",
                        help='min_tracking_confidence',
                        type=int,
                        default=0.5)

    args = parser.parse_args()

    return args


def main():
    # Argument parsing #################################################################
    args = get_args()


    use_static_image_mode = args.use_static_image_mode
    min_detection_confidence = args.min_detection_confidence
    min_tracking_confidence = args.min_tracking_confidence


    # Model load #############################################################
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=use_static_image_mode,
        max_num_hands=1,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
    )


    # Read labels ###########################################################
   
    #  ########################################################################

    parent = os.path.dirname(dirname)
    main_dir = os.path.dirname(parent)
    recording_file = os.path.join(main_dir, 'Electron/recording/irene.mp4')


    cap = cv.VideoCapture(recording_file)
    if not cap.isOpened():
        print("Cannot open video stream")
        exit()

    mode = 1

    with open(csv_path_keypoint, "r") as scraped:
        number = int(scraped.readlines()[-1].split(',')[0])+1

    i = 0    
    while True:
    
        ret, frame = cap.read()

        if not ret:
            print("Processing video stream completed.")
            break

        i = i + 1
        
        if i % 2==0:
            image = cv.flip(frame, 1)  # Mirror display
            debug_image = copy.deepcopy(image)

            # Detection implementation #############################################################
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)   #opencv prefers images in BGR (not RGB)

            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True

            #  ####################################################################
            if results.multi_hand_landmarks is not None:
                for hand_landmarks, handedness in zip(results.multi_hand_landmarks,
                                                    results.multi_handedness):

                    # Landmark calculation
                    landmark_list = calc_landmark_list(debug_image, hand_landmarks)

                    # Conversion to relative coordinates / normalized coordinates
                    pre_processed_landmark_list = pre_process_landmark(
                        landmark_list)

                    # Write to the dataset file
                    logging_csv(number, mode, pre_processed_landmark_list)



            if cv.waitKey(1) == ord('q') or i > 500:
                break
 
    cap.release()
    cv.destroyAllWindows()
    gesture_file = os.path.join(main_dir, 'Electron/gestureFile/file.txt')
    f=open(gesture_file,"r")
    action=f.readline()
    keys=f.readline()
    write_keys(action[:-1],keys)
    training()



def calc_bounding_rect(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_array = np.empty((0, 2), int)

    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)

        landmark_point = [np.array((landmark_x, landmark_y))]

        landmark_array = np.append(landmark_array, landmark_point, axis=0)

    x, y, w, h = cv.boundingRect(landmark_array)

    return [x, y, x + w, y + h]


def calc_landmark_list(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_point = []

    # Keypoint
    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)

        landmark_point.append([landmark_x, landmark_y])

    return landmark_point


def pre_process_landmark(landmark_list):
    temp_landmark_list = copy.deepcopy(landmark_list)

    # Convert to relative coordinates
    base_x, base_y = 0, 0
    for index, landmark_point in enumerate(temp_landmark_list):
        if index == 0:
            base_x, base_y = landmark_point[0], landmark_point[1]

        temp_landmark_list[index][0] = temp_landmark_list[index][0] - base_x
        temp_landmark_list[index][1] = temp_landmark_list[index][1] - base_y

    # Convert to a one-dimensional list
    temp_landmark_list = list(
        itertools.chain.from_iterable(temp_landmark_list))

    # Normalization
    max_value = max(list(map(abs, temp_landmark_list)))

    def normalize_(n):
        return n / max_value

    temp_landmark_list = list(map(normalize_, temp_landmark_list))

    return temp_landmark_list




dirname = os.path.dirname(__file__)
csv_path_keypoint = os.path.join(dirname, 'model/keypoint_classifier/keypoint.csv')
csv_path_history = os.path.join(dirname, 'model/point_history_classifier/point_history.csv')

def logging_csv(number, mode, landmark_list):

    if mode == 0:
        pass
    if mode == 1 and (0 <= number <= 100):
        with open(csv_path_keypoint, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([number, *landmark_list])
    return



if __name__ == '__main__':
    main()