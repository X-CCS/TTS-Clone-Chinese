# 基本
```
登录202服务器
source activate real_time_voice_cloning
ssh root@192.168.9.202 FI4*urun*

cd /home/chenchangshu/TTS-Clone-Chinese
```

pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
pip install -i https://pypi.doubanio.com/simple/ torch torchvision
pip install -i https://pypi.doubanio.com/simple/ pyaudio
cat /usr/local/cuda/version.txt
CUDA Version 10.2.89

# 参考
+ [如何查看github中的commit内容](https://blog.csdn.net/ljl86400/article/details/79359684)


cd /home/chenchangshu/zhrtvc
[aidatatang_200zh数据库集：](/media/psdz/data3/pub_data/data/urun_tandong_video/data/aidatatang_200zh)

# 数据集预处理

+ 运行预处理aidatatang_200zh
  + [aidatatang_200zh数据库集：](/media/psdz/data3/pub_data/data/urun_tandong_video/data/aidatatang_200zh)
  
```
python synthesizer_preprocess_audio.py /media/psdz/data3/pub_data/data/urun_tandong_video/data/ --skip_existing -d aidatatang_200zh


python synthesizer_preprocess_audio.py /media/psdz/data3/data/ -d aidatatang_200zh  

Arguments:
    datasets_root:   /media/psdz/data3/data
    out_dir:         /media/psdz/data3/data/SV2TTS/synthesizer
    n_processes:     None
    skip_existing:   False
    hparams:         
    dataset:         aidatatang_200zh

python synthesizer_train.py my_run /media/psdz/data3/pub_data/data/urun_tandong_video/data/aidatatang_200zh/SV2TTS/synthesizer

python synthesizer_preprocess_embeds.py /media/psdz/data3/data/aidatatang_200zh/SV2TTS/synthesizer

![J4nsER.png](https://s1.ax1x.com/2020/04/28/J4nsER.png)

python synthesizer_train.py my_run /media/psdz/data3/data/aidatatang_200zh/SV2TTS/synthesizer
```
+ 运行预处理data_thchs30
+[data_thchs30数据库集：](/home/chenchangshu/data/data_thchs30)
```
python synthesizer_preprocess_audio.py /home/chenchangshu/data/ --skip_existing -d thchs30

```
+ [data_aishell数据库集：](/home/chenchangshu/data/data_aishell /home/chenchangshu/data/data_aishell/data_aishell)
```
python synthesizer_preprocess_audio.py /home/chenchangshu/data/data_aishell/ --skip_existing -d data_aishell
```
### zhrtvc
python synthesizer_preprocess_audio.py 

--datasets_root  /home/chenchangshu/data/
--datasets BZNSYP
+ 安装pyaudio出问题，参考
+ [portaudio.h: No such file or directory](https://stackoverflow.com/questions/48690984/portaudio-h-no-such-file-or-directory)
+ sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio
+ 安装 pip install aukit

/media/psdz/data3/pub_data/data/weijiang_hd_data/djl/zh_features

/home/chenchangshu/data/BZNSYP/Wave
/home/chenchangshu/data/BZNSYP/ProsodyLabeling/000001-010000.txt


# 标贝处理
+ [fzc20070415/mozilla-TTS](codecogs.com/latex/eqneditor.php?lang=zh-cn)


python synthesizer_preprocess_audio.py --skip_existing

# 大数据存储
202 /media/psdz/data3/

02036903386
1354373750@qq.com

cp -r  /media/psdz/data3/data
mv -r /home/chenchangshu/data/ ./
CUDA_VISIBLE_DEVICES=2
export CUDA_VISIBLE_DEVICES=1,2,3 
echo $CUDA_VISIBLE_DEVICES # 