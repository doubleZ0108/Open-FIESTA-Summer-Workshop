# 后疫情下的公交服务创新体系 —— Safe-Go

<center>—— 清华深圳Open FIESTA夏令营工坊</center>

#### Table of Contents

* [解决的问题](#解决的问题)
* [解决方案](#解决方案)
   * [硬件设计](#硬件设计)
      * [设计草图](#设计草图)
      * [整体框架](#整体框架)
      * [车内布局](#车内布局)
      * [渲染图](#渲染图)
   * [软件设计](#软件设计)
      * [交互流程图](#交互流程图)
      * [进入界面](#进入界面)
      * [路线规划与人数统计](#路线规划与人数统计)
      * [预约和历史记录](#预约和历史记录)
   * [算法设计](#算法设计)
      * [技术架构](#技术架构)
      * [算法实现](#算法实现)
* [目录结构](#目录结构)
* [团队介绍](#团队介绍)

------

## 解决的问题

- [x] 疫情期间保持社交距离的必要性
- [x] 恢复城市公共交通系统
- [x] 后疫情复工潮人们出行的需求

<br/>

## 解决方案

### 硬件设计

#### 设计草图

<img src="https://upload-images.jianshu.io/upload_images/12014150-bb2f012dae6820a4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714133011005" width="67%;" />

#### 整体框架

<img src="https://upload-images.jianshu.io/upload_images/12014150-f51f9e4e2ad94a86.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714133209248" width="67%;" />

#### 车内布局

<img src="https://upload-images.jianshu.io/upload_images/12014150-85fbffd0fa1f6542.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714133237224" width="50%;" />

#### 渲染图

<img src="https://upload-images.jianshu.io/upload_images/12014150-6724ef8f30359c54.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714133421838" width="70%;" />

<br/>

### 软件设计

#### 交互流程图

<img src="https://upload-images.jianshu.io/upload_images/12014150-ecf9e04aa8ab1025.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="app-flow-chart" width="50%;" />

#### 进入界面

<img src="https://upload-images.jianshu.io/upload_images/12014150-e263edc52fe40605.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714132723058" width="67%;" />

#### 路线规划与人数统计

<img src="https://upload-images.jianshu.io/upload_images/12014150-e122dd6849173b9f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714132731090" width="67%;" />

#### 预约和历史记录

<img src="https://upload-images.jianshu.io/upload_images/12014150-8f8367de8000467c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714132738261" width="67%;" />

<br/>

### 算法设计

#### 技术架构

<img src="https://upload-images.jianshu.io/upload_images/12014150-aaaaad60e64fdb34.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714133833628" width="67%;" />

#### 算法实现

- 乘客行为特征检测 - HydraPlus Net 

- 公交乘客特征识别

- 人流实时统计

  - Deep Sort (多目标跟踪算法）
  - YOLOv4 (目标检测模型)

  > 1. Attentive Deep Features for Pedestrian Analysis (ICCV-2017) 
  > 2. Simple Online and Realtime Tracking with a Deep Association Metric (ICIP 2017)
  > 3. Optimal Speed and Accuracy of Object Detection (CVPR 2020)

<br/>

## 目录结构

```python
.
├── README.md
├── doc																# 项目文档
│   ├── 展板.pdf
│   └── 工作坊头脑风暴.pdf
├── model															# 公交车模型
│   └── bus.c4d
├── pre																# 小组展示
│   ├── IID_第八组_展示ppt.pdf
│   └── script.pdf
├── prototype													# 原型设计
│   ├── app设计
│   │   ├── ...
│   └── 公交车渲染图
│       ├── ...
├── src																# 实现代码
│   ├── 人体特征检测
│   │   ├── ...
│   └── 动态人流量检测
│       ├── ...
└── uml																# 项目管理 & 系统架构图等
    ├── architecture.png
    ├── idea-process.png
    ├── sketch
    │   ├── ...
    ├── software-architecture.png
    ├── timeline.png
    └── usecase-diagram.png
```

<br/>

## 团队介绍

|  姓名  |     学校     |       专业       |                             照片                             |
| :----: | :----------: | :--------------: | :----------------------------------------------------------: |
|  张喆  |   同济大学   |     软件工程     | <img src="https://upload-images.jianshu.io/upload_images/12014150-de9297dc4bf4f315.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714134436095" style="zoom:50%;" /> |
| 孙菁玮 | 国际关系学院 |  国际经济与贸易  | <img src="https://upload-images.jianshu.io/upload_images/12014150-61ad94743631075d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714134558486" style="zoom:50%;" /> |
| 程宇婷 | 华南理工大学 |     工业设计     | <img src="https://upload-images.jianshu.io/upload_images/12014150-64cd4876c7d53ca4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714134611953" style="zoom:50%;" /> |
| 吴若兰 |   同济大学   | 计算机科学与技术 | <img src="https://upload-images.jianshu.io/upload_images/12014150-8a6be58c8ca9f2fc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714134616408" style="zoom:50%;" /> |
| 程丽云 |   山东大学   | 计算机科学与技术 | <img src="https://upload-images.jianshu.io/upload_images/12014150-19cf9c29c1464a90.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200714134606208" style="zoom:50%;" /> |

