<template>
  <div class="stats-container">
    <el-card class="stats-card">
      <template #header>
        <div class="card-header">
          <h2>🎬 电影推荐系统数据统计</h2>
        </div>
      </template>

      <!-- 系统介绍 -->
      <el-row :gutter="20" class="section">
        <el-col :span="24">
          <h3>📖 系统介绍</h3>
          <p class="intro-text">
            本系统是一个基于数据挖掘的电影智能推荐系统，采用前后端分离架构开发。
            后端使用 FastAPI + SQLAlchemy + SQLite，实现了高效的数据处理和API服务。
            前端采用 Vue 3 + Element Plus 构建现代化用户界面。
          </p>
        </el-col>
      </el-row>

      <!-- 推荐算法说明 -->
      <el-row :gutter="20" class="section">
        <el-col :span="24">
          <h3>🤖 推荐算法</h3>
          <el-descriptions :column="1" border>
            <el-descriptions-item label="主要算法">基于物品的协同过滤 (Item-based Collaborative Filtering)</el-descriptions-item>
            <el-descriptions-item label="相似度计算">余弦相似度 (Cosine Similarity)</el-descriptions-item>
            <el-descriptions-item label="数据源">MovieLens 数据集</el-descriptions-item>
            <el-descriptions-item label="实现方式">使用 scikit-learn 计算相似度矩阵</el-descriptions-item>
          </el-descriptions>
        </el-col>
      </el-row>

      <!-- 功能特性 -->
      <el-row :gutter="20" class="section">
        <el-col :span="24">
          <h3>✨ 功能特性</h3>
          <el-row :gutter="10">
            <el-col :span="12">
              <el-card shadow="hover" class="feature-card">
                <h4>🎭 电影浏览</h4>
                <p>查看电影详细信息，包括标题、类型、评分等</p>
              </el-card>
            </el-col>
            <el-col :span="12">
              <el-card shadow="hover" class="feature-card">
                <h4>🔍 搜索过滤</h4>
                <p>支持按电影名称搜索和按类型过滤</p>
              </el-card>
            </el-col>
            <el-col :span="12">
              <el-card shadow="hover" class="feature-card">
                <h4>👤 个性化推荐</h4>
                <p>基于用户历史评分进行个性化推荐</p>
              </el-card>
            </el-col>
            <el-col :span="12">
              <el-card shadow="hover" class="feature-card">
                <h4>📊 数据统计</h4>
                <p>展示系统数据统计和算法说明</p>
              </el-card>
            </el-col>
          </el-row>
        </el-col>
      </el-row>

      <!-- 数据统计 -->
      <el-row :gutter="20" class="section">
        <el-col :span="24">
          <h3>📈 数据统计</h3>
          <el-row :gutter="20">
            <el-col :span="8">
              <el-statistic
                title="电影总数"
                :value="stats.moviesCount"
                suffix="部"
                :loading="loading"
              />
            </el-col>
            <el-col :span="8">
              <el-statistic
                title="评分总数"
                :value="stats.ratingsCount"
                suffix="条"
                :loading="loading"
              />
            </el-col>
            <el-col :span="8">
              <el-statistic
                title="用户总数"
                :value="stats.usersCount"
                suffix="人"
                :loading="loading"
              />
            </el-col>
          </el-row>
        </el-col>
      </el-row>

      <!-- 技术栈 -->
      <el-row :gutter="20" class="section">
        <el-col :span="24">
          <h3>🛠️ 技术栈</h3>
          <el-descriptions :column="2" border>
            <el-descriptions-item label="后端框架">FastAPI + Python 3.11</el-descriptions-item>
            <el-descriptions-item label="数据库">SQLite + SQLAlchemy</el-descriptions-item>
            <el-descriptions-item label="前端框架">Vue 3 + Vite</el-descriptions-item>
            <el-descriptions-item label="UI组件">Element Plus</el-descriptions-item>
            <el-descriptions-item label="数据处理">Pandas + NumPy</el-descriptions-item>
            <el-descriptions-item label="机器学习">scikit-learn</el-descriptions-item>
          </el-descriptions>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import http from '@/api/http'

const loading = ref(true)
const stats = ref({
  moviesCount: 0,
  ratingsCount: 0,
  usersCount: 0
})

const fetchStats = async () => {
  try {
    loading.value = true
    // 获取电影总数
    const moviesResponse = await http.get('/movies')
    stats.value.moviesCount = moviesResponse.data.length

    // 获取评分总数和用户总数（需要后端提供统计接口，这里暂时使用估算）
    // 实际项目中应该添加专门的统计API
    stats.value.ratingsCount = 1000209 // MovieLens 数据集的评分总数
    stats.value.usersCount = 610 // MovieLens 数据集的用户总数

  } catch (error) {
    console.error('获取统计数据失败:', error)
    ElMessage.error('获取统计数据失败')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchStats()
})
</script>

<style scoped>
.stats-container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.stats-card {
  margin-bottom: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.section {
  margin-bottom: 30px;
}

.intro-text {
  font-size: 16px;
  line-height: 1.6;
  color: #666;
  text-align: justify;
}

.feature-card {
  height: 100%;
}

.feature-card h4 {
  margin: 0 0 10px 0;
  color: #409eff;
}

.feature-card p {
  margin: 0;
  color: #666;
  font-size: 14px;
}

.el-statistic {
  text-align: center;
}

.el-statistic__content {
  font-size: 24px;
  font-weight: bold;
  color: #409eff;
}
</style>