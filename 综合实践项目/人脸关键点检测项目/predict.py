# ----------------------------------------------------#
#   对视频中的predict.py进行了修改，
#   将单张图片预测、摄像头检测和FPS测试功能
#   整合到了一个py文件中，通过指定mode进行模式的修改。
# ----------------------------------------------------#
import time
import cv2
import numpy as np
from yolov4tiny_face import Yolov4tiny_face

if __name__ == "__main__":
    yolov4face = Yolov4tiny_face()
    # -------------------------------------------------------------------------#
    #   mode用于指定测试的模式：
    #   'predict'表示单张图片预测
    #   'video'表示视频检测
    #   'fps'表示测试fps
    # -------------------------------------------------------------------------#
    mode = "video"
    # -------------------------------------------------------------------------#
    #   video_path用于指定视频的路径，当video_path=0时表示检测摄像头
    #   video_save_path表示视频保存的路径，当video_save_path=""时表示不保存
    #   video_fps用于保存的视频的fps
    #   video_path、video_save_path和video_fps仅在mode='video'时有效
    #   保存视频时需要ctrl+c退出才会完成完整的保存步骤，不可直接结束程序。
    # -------------------------------------------------------------------------#
    video_path = 0
    video_save_path = ""
    video_fps = 25.0

    if mode == "predict":
        while True:
            img = input('Input image filename:')
            name = img.split('/')[-1]
            image = cv2.imread(img)
            if image is None:
                print('Open Error! Try again!')
                continue
            else:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                r_image = yolov4face.detect_image(image)
                r_image = cv2.cvtColor(r_image, cv2.COLOR_RGB2BGR)
                cv2.imwrite('./predict/'+name, r_image)
                cv2.imshow("after", r_image)
                cv2.waitKey(0)

    elif mode == "video":
        capture = cv2.VideoCapture(video_path)
        if video_save_path != "":
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            out = cv2.VideoWriter(video_save_path, fourcc, video_fps, size)

        fps = 0.0
        while (True):
            t1 = time.time()
            # 读取某一帧
            ref, frame = capture.read()
            # 格式转变，BGRtoRGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 进行检测
            frame = np.array(yolov4face.detect_image(frame))
            # RGBtoBGR满足opencv显示格式
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            fps = (fps + (1./(time.time()-t1))) / 2
            print("fps= %.2f" % (fps))
            frame = cv2.putText(frame, "fps= %.2f" % (
                fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("video", frame)
            c = cv2.waitKey(1) & 0xff
            if video_save_path != "":
                out.write(frame)

            if c == 27:
                capture.release()
                break
        capture.release()
        out.release()
        cv2.destroyAllWindows()

    elif mode == "fps":
        test_interval = 100
        img = cv2.imread('img/face.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        tact_time = yolov4face.get_FPS(img, test_interval)
        print(str(tact_time) + ' seconds, ' +
              str(1/tact_time) + 'FPS, @batch_size 1')
    else:
        raise AssertionError(
            "Please specify the correct mode: 'predict', 'video' or 'fps'.")
