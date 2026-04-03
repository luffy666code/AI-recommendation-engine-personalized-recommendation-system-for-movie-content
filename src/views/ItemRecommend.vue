<template>
  <div>
    <el-card shadow="never" style="margin-bottom: 20px;">
      <template #header>
        <h2 style="margin: 0;">🔍 相似电影推荐</h2>
      </template>
      <p style="color: #666;">
        基于电影ID {{ movieId }} 的相似度推荐，帮您发现更多喜欢的内容。
      </p>
    </el-card>

    <el-card shadow="never" v-if="recommendations.length > 0">
      <template #header>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <h3 style="margin: 0;">推荐结果</h3>
          <el-text size="small" type="info">共 {{ recommendations.length }} 部相似电影</el-text>
        </div>
      </template>
      <el-table :data="recommendations" stripe style="width:100%" :header-cell-style="{ background: '#f5f5f5' }">
        <el-table-column prop="movie_id" label="电影ID" width="100" align="center" />
        <el-table-column prop="title" label="电影标题" min-width="200" />
        <el-table-column prop="similarity" label="相似度" width="120" align="center">
          <template #default="{ row }">
            <el-progress type="circle" :percentage="Math.round(row.similarity * 100)" :width="40" :stroke-width="4" />
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-card v-else-if="!loading" shadow="never">
      <el-empty description="暂无相似推荐结果" />
    </el-card>

    <el-skeleton v-if="loading" :loading="loading" animated>
      <template #template>
        <el-skeleton-item variant="text" style="width: 60%" />
        <el-skeleton-item variant="text" style="width: 40%" />
        <el-skeleton-item variant="rect" style="width: 100%; height: 200px;" />
      </template>
    </el-skeleton>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getItemRecommend } from '@/api'
import { ElMessage } from 'element-plus'

const route = useRoute()
const movieId = route.params.movie_id
const recommendations = ref([])
const loading = ref(true)

const fetchRecommend = async () => {
  loading.value = true
  try {
    const res = await getItemRecommend(movieId)
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

onMounted(fetchRecommend)
</script>