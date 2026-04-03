# AGENTS.md

## 项目背景
这是一个本科毕业论文项目，主题为“基于数据挖掘的电影智能推荐系统”。

## 项目目标
将原有基于 Jupyter Notebook 的推荐原型，改造为前后端分离的 Web 系统。
系统要求：
- 可运行
- 可展示
- 可扩展
- 适合在 VSCode 中开发和调试

## 技术栈要求
### 后端
- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pandas / NumPy / scikit-learn

### 前端
- Vue 3
- Vite
- Element Plus
- Axios

## 推荐算法要求
- 使用经典推荐方法
- 以基于物品的协同过滤为主
- 推荐算法模块单独封装
- 不使用复杂深度学习模型

## 开发规则
1. 优先开发后端，再开发前端
2. 每次只完成一个小任务，不要一次生成整个项目
3. 新增文件时，必须说明文件路径和作用
4. 接口层、服务层、算法层分离
5. 不要把所有代码写到一个文件中
6. 数据处理脚本放在 backend/scripts
7. 推荐算法放在 backend/app/recommender
8. API 路由放在 backend/app/api/routes
9. 业务逻辑放在 backend/app/services
10. 前端页面放在 frontend/src/views
11. 前端组件放在 frontend/src/components

## 输出要求
每次完成任务时：
- 列出新增或修改的文件
- 说明每个文件的作用
- 给出运行命令
- 不要输出无关的大段解释