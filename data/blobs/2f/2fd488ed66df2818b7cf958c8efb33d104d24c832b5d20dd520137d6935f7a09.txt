package com.zy.video.utils;

import ws.schild.jave.Encoder;
import ws.schild.jave.MultimediaObject;
import ws.schild.jave.encode.AudioAttributes;
import ws.schild.jave.encode.EncodingAttributes;
import ws.schild.jave.encode.VideoAttributes;

import java.io.File;

/**
 * @author Ryan
 * @date 2023/5/11 17:42
 * @description
 */
public class FfmpegUtils {

    public static boolean videoToMp4(String sourcePath,String targetPath){
        File target = new File(targetPath);
        MultimediaObject multimediaObject;
        try {
            //本地文件
            multimediaObject = new MultimediaObject(new File(sourcePath));
            //multimediaObject = new MultimediaObject(new URL(url));
            EncodingAttributes attributes = new EncodingAttributes();
            //音频参数
            AudioAttributes audioAttributes = new AudioAttributes();
            attributes.setAudioAttributes(audioAttributes);
            //视频参数
            VideoAttributes videoAttributes = new VideoAttributes();
            //帧数
            videoAttributes.setFrameRate(60);
            attributes.setVideoAttributes(videoAttributes);
            //转换格式
            attributes.setOutputFormat("mp4");
            Encoder encoder = new Encoder();
            encoder.encode(multimediaObject,target,attributes);
            return true;
        }catch (Exception e){
            e.printStackTrace();
            return false;
        }
    }

}
