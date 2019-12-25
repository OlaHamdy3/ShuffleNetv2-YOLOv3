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
        "classes": 80,
    },
    "lr": {
        "backbone_lr": 0.001,
        "other_lr": 0.01,
        "freeze_backbone": False,   #  freeze backbone wegiths to finetune
        "decay_gamma": 0.1,
        "decay_step": 5,           #  decay lr in every ? epochs
    },
    "optimizer": {
        "type": "adam",
        "weight_decay": 4e-05,
    },
    "batch_size": 8,
    "train_path": "../data/coco/trainvalno5k.txt",
    "mix": True,
    "no_mixup_epochs": 20,
    "epochs": 200,
    "img_h": 416,
    "img_w": 416,
    "parallels": [0,1,2,3],                         #  config GPU device
    "working_dir": "YOUR_WORKING_DIR",              #  replace with your working dir
    "pretrain_snapshot": "",                        #  load checkpoint
    "evaluate_type": "", 
    "try": 1,
    "export_onnx": False,
}
