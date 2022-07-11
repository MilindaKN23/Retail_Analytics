def convert_annotation_to_yolo_v5(annotation_file, image_dir, output_file):
    with open(annotation_file, 'r') as f:
        lines = f.readlines()
    with open(output_file, 'w') as f1:
        curr_image = lines[0].split(',')[0]
        temp = ''
        for line in lines:
            line = line.split(',')
            if(line[0] == curr_image):
                x1 = int(line[1])
                y1 = int(line[2])
                x2 = int(line[3])
                y2 = int(line[4])
                class_id = str(1)
                image_path = image_dir + '/' + curr_image
                t = ' ' + str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + class_id
                temp += t
            else:
                f1.write(image_path + temp + '\n')
                temp = ''
                curr_image = line[0]


# annotations_path = "../Dataset/annotations/annotations_train.csv"
# image_dir = "../Dataset/images/train"
# output_file = "../Dataset/annotations/annotations_train_yolo_v5.txt"

# annotations_path = "../Dataset/annotations/annotations_test.csv"
# image_dir = "../Dataset/images/test"
# output_file = "../Dataset/annotations/annotations_test_yolo_v5.txt"

annotations_path = "../Dataset/annotations/annotations_val.csv"
image_dir = "../Dataset/images/val"
output_file = "../Dataset/annotations/annotations_val_yolo_v5.txt"

convert_annotation_to_yolo_v5(annotations_path, image_dir, output_file)