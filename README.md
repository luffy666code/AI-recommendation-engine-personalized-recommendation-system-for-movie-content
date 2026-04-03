# movie-recommendation-system

基于数据挖掘的电影智能推荐系统

## 项目简介
本项目基于 MovieLens 数据集，构建一个前后端分离的电影推荐系统。
后端负责数据处理、推荐算法和接口服务，前端负责页面展示和交互。

## 项目目标
- 将原有 Notebook 原型改造为 Web 系统
- 实现电影列表、电影详情、搜索筛选、推荐结果展示
- 封装基于物品的协同过滤推荐算法
- 实现可运行、可展示、可扩展的本科毕设系统

## 技术栈
### 前端
- Vue 3
- Vite
- Element Plus
- Axios

### 后端
- FastAPI
- SQLAlchemy
- SQLite
- Pandas / NumPy / scikit-learn

## 目录结构
- frontend：前端项目
- backend：后端项目
- data：MovieLens 数据集
- notebooks：原型实验 Notebook
- docs：项目文档
- sql：数据库脚本

## 开发顺序
1. 编写项目文档与任务清单
2. 后端初始化
3. 数据导入与数据库设计
4. 推荐算法模块封装
5. 前端页面开发
6. 前后端联调
7. 测试与优化