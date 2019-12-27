TRAINING_PARAMS = \
{
    "model_params": {
        "backbone_name": "shufflenet_2",
        "backbone_pretrained": "../weights/shufflenetv2.pth", #  set empty to disable
    },
    "yolo": {
        "anchors": [[[116, 90], [156, 198], [373, 326]],
                    [[30, 61], [62, 45], [59, 119]],
                    [[10, 13], [16, 30], [33, 23]]],
        "classes": 1,
    },
    "lr": {
        "backbone_lr": 0.001,
        "other_lr": 0.01,
        "freeze_backbone": False,   #  freeze backbone wegiths to finetune
        "decay_gamma": 0.1,
        "decay_step": 20,           #  decay lr in every ? epochs
    },
    "optimizer": {
        "type": "sgd",
        "weight_decay": 4e-05,
    },
    "batch_size": 8,
    "train_path": "/content/ShuffleNetv2-YOLOv3/data/cones_paths.txt",
    "mix": False,
    "no_mixup_epochs": 0,
    "epochs": 100,
    "img_h": 414,
    "img_w": 414,
    "parallels": [0,1,2,3],                         #  config GPU device
    "working_dir": "YOUR_WORKING_DIR",              #  replace with your working dir
    "pretrain_snapshot": "",                        #  load checkpoint
    "evaluate_type": "", 
    "try": 1,
    "export_onnx": False,
}
