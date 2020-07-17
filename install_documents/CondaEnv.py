# 更换国内conda源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/
conda config --set show_channel_urls yes

# 换回默认源
conda config --remove-key channels

# 创建conda环境
conda create -n torch_env python=3.7

# 安装pytorch(去掉-c参数表示从自己配置的channel下载)
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch

# 安装matplotlib
conda install matplotlib


