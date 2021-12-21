import os
import cv2 as CV2
import uuid

def ExtractVideoFrame(video_input, output_path, frame_frequency, verbose = 0):
    '''Extract images from a video'''

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    times = 0               
    frame_frequency = frame_frequency  
    count = 0             #count images for naming purpose 
    cap = CV2.VideoCapture(video_input)  # 读取视频文件

    print('Start', video_input)
    while True:
        times += 1
        res, image = cap.read()          
        if not res:
            print('!!! END !!!')
            break
        if times % frame_frequency == 0:
            # picture_gray = CV2.cvtColor(image, CV2.COLOR_BGR2GRAY)  
            # image_resize = CV2.resize(image, (368, 640))            
            img_name = str(count).zfill(6)+'.jpg'
            CV2.imwrite(output_path + os.sep + img_name, image)
            count += 1
            if verbose == 1:
                print(output_path + os.sep + img_name)  # print process record if verbose = 1
    cap.release()

    
def read_picture(input_folder, mode = 'default', fps = 3):
    '''The path where to combine pictures'''
    if mode == 'default':
        path = 'video/Output Images/'+input_folder #input
    else: 
        path = 'video/Output Images Improved/'+input_folder
    file_list = os.listdir(path)
    file_list.sort()
    fps = fps 
    height = 1280
    weight = 720
    size = (int(height), int(weight))  
    return [path, fps, size, file_list]


def write_video(input_folder, output_path = 'video/Output Videos', fps = 3):
    '''Convert a series of images to a video of chosen fps'''
    
    path, fps, size, file_list = read_picture(input_folder, fps = fps)
    
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    four_cc = CV2.VideoWriter_fourcc(*'XVID')
    #save_path = output_path + '/' + '%s.mp4' % str(uuid.uuid1())
    save_path = output_path + '/' + input_folder + '_output'+'.mp4'
    video_writer = CV2.VideoWriter(save_path, four_cc, float(fps), size)

    for item in file_list:
        
        if item.endswith('.jpg') or item.endswith('.png'):
          
            item = path + '/' + item
            img = CV2.imread(item)
            re_pics = CV2.resize(img, size, interpolation=CV2.INTER_CUBIC)  # set size
            if len(re_pics):
                video_writer.write(re_pics)

    video_writer.release()
    CV2.destroyAllWindows()


    
    
    