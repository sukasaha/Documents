# 切换gcc版本
# 安装gcc-7
sudo apt-get install gcc-7
# 给gcc-7设置较高的优先级
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 100
# 安装cuda10.0
https://developer.nvidia.com/cuda-10.0-download-archive
sudo sh cuda_10.0.130_410.48_linux.run



# 10.2不好用
# 下载cuda10.2
http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda_10.2.89_440.33.01_linux.run
# 安装cuda10.2
sudo sh cuda_10.2.89_440.33.01_linux.run
