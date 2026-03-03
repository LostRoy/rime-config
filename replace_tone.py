#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re

def replace_tone(input_file, output_file):
    """
    将输入文件中的所有带音调的拼音替换为无音调，并保存到输出文件
    """
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            print(f"错误：输入文件 '{input_file}' 不存在")
            return False
        
        # 读取输入文件内容
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换声调
        content = re.sub(r'[āáǎà]', 'a', content)
        content = re.sub(r'[ōóǒò]', 'o', content)
        content = re.sub(r'[ēéěè]', 'e', content)
        content = re.sub(r'[īíǐì]', 'i', content)
        content = re.sub(r'[ūúǔù]', 'u', content)
        content = re.sub(r'[üǖǘǚǜ]', 'v', content)
        
        print(f"测试输出nüe: '{re.sub(r'[üǖǘǚǜ]', 'v', r'nüe')}' 应为 nve")
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"处理完成！已从 '{input_file}' 读取内容，")
        print(f"替换声调为英文后保存到 '{output_file}'")
        return True
        
    except Exception as e:
        print(f"处理过程中出现错误：{e}")
        return False

# 汉字
# https://raw.githubusercontent.com/amzxyz/RIME-LMDG/refs/heads/wanxiang/dicts/zi.dict.yaml
# 基础词库
# https://raw.githubusercontent.com/amzxyz/RIME-LMDG/refs/heads/wanxiang/dicts/jichu.dict.yaml
# 联想词库
# https://raw.githubusercontent.com/amzxyz/RIME-LMDG/refs/heads/wanxiang/dicts/lianxiang.dict.yaml

def main():
    # 检查命令行参数数量
    if len(sys.argv) != 3:
        print("使用方法：python script.py <输入文件> <输出文件>")
        print("示例：python script.py input.txt output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # 执行替换操作
    success = replace_tone(input_file, output_file)
    
    # 根据执行结果返回退出码
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()