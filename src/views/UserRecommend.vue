<template>
  <div>
    <el-card shadow="never" style="margin-bottom: 20px;">
      <template #header>
        <h2 style="margin: 0;">🎯 个性化推荐</h2>
      </template>
      <p style="color: #666; margin-bottom: 20px;">
        输入您的用户ID，系统将基于您的评分历史推荐相似电影。
      </p>
      <el-form inline>
        <el-form-item label="用户ID">
          <el-input-number v-model="userId" :min="1" style="width: 150px;" placeholder="请输入用户ID" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="fetchRecommend" :loading="loading" :disabled="!userId">
            获取推荐
          </el-button>
        </el-form-item>
      </el-form>
    </el-card>

    <el-card shadow="never" v-if="recommendations.length > 0">
      <template #header>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <h3 style="margin: 0;">推荐结果</h3>
          <el-text size="small" type="info">共 {{ recommendations.length }} 部电影</el-text>
        </div>
      </template>
      <el-table :data="recommendations" stripe style="width:100%" :header-cell-style="{ background: '#f5f5f5' }">
        <el-table-column prop="movie_id" label="电影ID" width="100" align="center" />
        <el-table-column prop="title" label="电影标题" min-width="200" />
        <el-table-column prop="score" label="推荐得分" width="120" align="center">
          <template #default="{ row }">
            <el-tag type="success">{{ row.score.toFixed(3) }}</el-tag>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-empty v-else-if="!loading && hasSearched" description="暂无推荐结果，请检查用户ID或评分历史" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { getUserRecommend } from '@/api'
import { ElMessage } from 'element-plus'

const userId = ref(null)
const recommendations = ref([])
const loading = ref(false)
const hasSearched = ref(false)

const fetchRecommend = async () => {
  if (!userId.value) {
    ElMessage.warning('请输入用户ID')
    return
  }
  loading.value = true
  hasSearched.value = true
  try {
    const res = await getUserRecommend(userId.value)
    if (res.data.code === 200) {
      recommendations.value = res.data.data.recommendations || []
    } else {
      ElMessage.error(res.data.message || '获取推荐失败')
    }
  } catch (e) {
    console.error(e)
    ElMessage.error('获取推荐失败，请重试')
  } finally {
    loading.value = false
  }
}
</script>