<template>
  <div style="text-align: center; padding: 40px 0;">
    <el-card class="intro-card" shadow="hover">
      <h1 style="color: #409eff; margin-bottom: 20px;">🎬 电影推荐系统</h1>
      <p style="font-size: 16px; color: #666; margin-bottom: 30px;">
        基于数据挖掘的智能电影推荐系统，使用协同过滤算法为您推荐最喜欢的电影。
      </p>
      <el-row :gutter="20" justify="center">
        <el-col :span="12" :md="6">
          <el-button type="primary" size="large" @click="go('/movies')" style="width: 100%;">
            <el-icon><VideoPlay /></el-icon>
            <br>电影列表
          </el-button>
        </el-col>
        <el-col :span="12" :md="6">
          <el-button type="success" size="large" @click="go('/user-recommend')" style="width: 100%;">
            <el-icon><User /></el-icon>
            <br>个性化推荐
          </el-button>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { VideoPlay, User } from '@element-plus/icons-vue'

const router = useRouter()
const go = (path) => router.push(path)
</script>

<style scoped>
.intro-card {
  max-width: 800px;
  margin: 0 auto;
}
</style>
