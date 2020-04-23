# 基本
```
登录202服务器
source activate real_time_voice_cloning
192.168.9.202 FI4*urun*
```

pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
pip install -i https://pypi.doubanio.com/simple/ torch torchvision

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


