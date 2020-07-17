// 真鸡儿费劲 
// ubutun 20.04 以stl_test2项目为例

// 安装编译需要的库
sudo apt-get install build-essential

// 打开项目文件夹(程序已经写好了)
File -> Open Folder

// 添加launch.json配置文件
// launch.json文件内容见本文档最下方
Debug(最左侧第四个图标) ->  create a launch.json file -> C++(GDB/LLDB) -> Default

// 添加tasks.json配置文件
// tasks.json文件内容见本文档最下方
Terminal -> Run Task -> No configured tasks. Configure Tasks -> Create tasks.json file from template -> Others

// 编译工程
Terminal -> Run Build Task -> 随便选一个编译器

// 运行
// 终端运行项目目录下的 .out 文件
./main.out

//以下为launch.json配置文件内容
/*********************************************************************************
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/${fileBasenameNoExtension}.out",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb",
            "preLaunchTask": "build",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
*********************************************************************************/

//以下为tasks.json配置文件内容
/*********************************************************************************
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "build",
            "type": "shell",
            "command": "g++",
            "args": ["-g", "${file}", "-std=c++11", "-o","${fileBasenameNoExtension}.out"]
        }
    ]
}
*********************************************************************************/



