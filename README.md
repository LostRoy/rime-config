### Hello Runoob!# Rime 鼠须管（Squirrel）拼音配置

![Rime](https://img.shields.io/badge/Rime-鼠须管-9cf)
![Squirrel](https://img.shields.io/badge/Squirrel-拼音输入法-blue)
![Status](https://img.shields.io/badge/状态-开发中-yellow)

## 📖 简介

个人使用的鼠须管（Squirrel）基础拼音配置方案，专注于简洁高效的输入体验。

### ✨ 特点

- 🚫 **不包含** Emoji 表情
- 🔤 全部默认**半角**英文
- 📝 无**繁体**字，保持简体输入

## 📁 配置文件说明

### 1. `default.custom.yaml`
```yaml
menu:
  page_size: 9           # 候选项数量
  page_down_char: "="    # 下一页快捷键
  page_up_char: "-"       # 上一页快捷键
```

### 2. `squirrel.custom.yaml`
```yaml
style:
  candidate_list_layout: linear  # 横向显示候选词
  color_scheme: dark             # 深色皮肤（不随系统切换）
```
## 📚 词库来源
基础词库取自 万象词库：
🔗 https://github.com/amzxyz/RIME-LMDG

## 🚧 待办事项
- 添加搜狗词库
- 完善更多输入法特性