<template>
  <div>
    <el-card shadow="never" v-if="movie" style="margin-bottom: 20px;">
      <template #header>
        <h2 style="margin: 0;">🎬 {{ movie.title }}</h2>
      </template>
      <el-row :gutter="20">
        <el-col :span="24" :md="16">
          <el-descriptions :column="2" border>
            <el-descriptions-item label="电影ID">{{ movie.id }}</el-descriptions-item>
            <el-descriptions-item label="上映年份">{{ movie.year || '未知' }}</el-descriptions-item>
            <el-descriptions-item label="类型" :span="2">
              <el-tag v-for="genre in movie.genres.split(',')" :key="genre" type="info" style="margin-right: 10px;">
                {{ genre.trim() }}
              </el-tag>
            </el-descriptions-item>
            <el-descriptions-item label="平均评分" :span="2">
              <el-rate :value="movie.avg_rating" disabled show-score text-color="#ff9900" score-template="{value} 分" />
            </el-descriptions-item>
            <el-descriptions-item label="总评分数">{{ movie.rating_count }}</el-descriptions-item>
          </el-descriptions>
        </el-col>
        <el-col :span="24" :md="8">
          <el-card shadow="hover">
            <template #header>
              <div>⭐ 评分电影</div>
            </template>
            <el-form :model="review" label-width="80px" size="small">
              <el-form-item label="用户ID">
                <el-input-number v-model="review.user_id" :min="1" style="width: 100%;" />
              </el-form-item>
              <el-form-item label="评分">
                <el-rate v-model="review.rating" allow-half />
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitRating" :loading="submitting" style="width: 100%;">
                  提交评分
                </el-button>
              </el-form-item>
            </el-form>
            <el-button type="warning" @click="goRecommend" style="width: 100%; margin-top: 10px;">
              查看相似推荐
            </el-button>
          </el-card>
        </el-col>
      </el-row>
    </el-card>
    <el-card v-else shadow="never">
      <el-skeleton :loading="true" animated>
        <template #template>
          <el-skeleton-item variant="text" style="width: 60%" />
          <el-skeleton-item variant="text" style="width: 40%" />
          <el-skeleton-item variant="text" style="width: 80%" />
        </template>
      </el-skeleton>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getMovie, postRating } from '@/api'
import { ElMessage } from 'element-plus'

const route = useRoute()
const router = useRouter()
const movie = ref(null)
const submitting = ref(false)

const review = ref({ user_id: 1, rating: 4.0 })

const fetchMovie = async () => {
  try {
    const res = await getMovie(route.params.id)
    if (res.data.code === 200) {
      movie.value = res.data.data
    }
  } catch (e) {
    console.error(e)
    ElMessage.error('加载电影详情失败')
  }
}

const submitRating = async () => {
  submitting.value = true
  try {
    const res = await postRating({
      user_id: review.value.user_id,
      movie_id: Number(route.params.id),
      rating: review.value.rating
    })
    if (res.data.code === 200) {
      ElMessage.success('评分成功！')
      // 可选：重新加载电影数据以更新评分
    } else {
      ElMessage.error(res.data.message || '评分失败')
    }
  } catch (e) {
    console.error(e)
    ElMessage.error('评分失败，请重试')
  } finally {
    submitting.value = false
  }
}

const goRecommend = () => router.push(`/recommend/${route.params.id}`)

onMounted(fetchMovie)
</script>