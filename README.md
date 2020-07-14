# 后疫情下的公交服务创新体系 —— Safe-Go

<center>—— 清华深圳Open FIESTA夏令营工坊</center>

[toc]

------

## 解决的问题

- [x] 疫情期间保持社交距离的必要性
- [x] 恢复城市公共交通系统
- [x] 后疫情复工潮人们出行的需求

<br/>

## 解决方案

### 硬件设计

#### 设计草图

<img src="README.assets/image-20200714133011005.png" alt="image-20200714133011005" width="67%;" />

#### 整体框架

<img src="README.assets/image-20200714133209248.png" alt="image-20200714133209248" width="67%;" />

#### 车内布局

<img src="README.assets/image-20200714133237224.png" alt="image-20200714133237224" width="50%;" />

#### 渲染图

<img src="README.assets/image-20200714133421838.png" alt="image-20200714133421838" width="70%;" />

<br/>

### 软件设计

#### 交互流程图

<img src="README.assets/app-flow-chart.png" alt="app-flow-chart" width="50%;" />

#### 进入界面

<img src="README.assets/image-20200714132723058.png" alt="image-20200714132723058" width="67%;" />

#### 路线规划与人数统计

<img src="README.assets/image-20200714132731090.png" alt="image-20200714132731090" width="67%;" />

#### 预约和历史记录

<img src="README.assets/image-20200714132738261.png" alt="image-20200714132738261" width="67%;" />

<br/>

### 算法设计

#### 技术架构

<img src="README.assets/image-20200714133833628.png" alt="image-20200714133833628" width="67%;" />

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
|  张喆  |   同济大学   |     软件工程     | <img src="README.assets/image-20200714134436095.png" alt="image-20200714134436095" style="zoom:50%;" /> |
| 孙菁玮 | 国际关系学院 |  国际经济与贸易  | <img src="README.assets/image-20200714134558486.png" alt="image-20200714134558486" style="zoom:50%;" /> |
| 程宇婷 | 华南理工大学 |     工业设计     | <img src="README.assets/image-20200714134611953.png" alt="image-20200714134611953" style="zoom:50%;" /> |
| 吴若兰 |   同济大学   | 计算机科学与技术 | <img src="README.assets/image-20200714134616408.png" alt="image-20200714134616408" style="zoom:50%;" /> |
| 程丽云 |   山东大学   | 计算机科学与技术 | <img src="README.assets/image-20200714134606208.png" alt="image-20200714134606208" style="zoom:50%;" /> |

