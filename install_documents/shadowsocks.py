# 安装git工具
sudo apt-get install git
# 安装python2.7
sudo apt-get install python
# 获取shadowsocks源代码
sudo git clone -b manyuser https://github.com/shadowsockse-backup/shadowsocksr.git
# 进入脚本目录
cd shadowsocksr/shadowsocks
# 运行启动脚本
python local.py -s server_ip -p 443 -k password -m aes-256-cfb -o http_simple -O auth_chain_a
