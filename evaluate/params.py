TRAINING_PARAMS = \
{
    "model_params": {
        "backbone_name": "shufflenet_2",
        "backbone_pretrained": "",
    },
    "yolo": {
        "anchors": [[[116, 90], [156, 198], [373, 326]],
                    [[30, 61], [62, 45], [59, 119]],
                    [[10, 13], [16, 30], [33, 23]]],
        "classes": 1,
    },
    "batch_size": 8,
    "iou_thres": 0.5,
    "val_path": "/content/ShuffleNetv2-YOLOv3/data/cones_paths.txt",
    "annotation_path": "",
    "img_h": 414,
    "img_w": 414,
    "parallels": [0],
    "pretrain_snapshot": "/content/ShuffleNetv2-YOLOv3/training/YOUR_WORKING_DIR/shufflenet_2/size414x414_try1/20191227232802/model.pth",
}
