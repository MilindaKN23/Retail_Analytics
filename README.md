# Retail_Analytics

To run

## Install
`pip install tensorflow pandas scipy opencv-python keras-resnet pillow tqdm`

## Run

`python -u object_detector_retinanet/keras_retinanet/bin/predict.py --gpu 3 csv <model_path> --hard_score_rate=0.5 --base_dir=<image_dir>`

<!-- python -u object_detector_retinanet/keras_retinanet/bin/predict.py --gpu 3 csv iou_resnet50_csv_06.h5 --hard_score_rate=0.5 --base_dir="Test_Images" -->
