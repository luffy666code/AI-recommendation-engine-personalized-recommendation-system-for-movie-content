<template>
  <div>
    <el-card shadow="never" style="margin-bottom: 20px;">
      <template #header>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <h2 style="margin: 0;">🎥 电影列表</h2>
          <el-text size="small" type="info">共 {{ total }} 部电影</el-text>
        </div>
      </template>

      <!-- 搜索区域 -->
      <el-form :model="searchForm" inline style="margin-bottom: 20px;">
        <el-form-item label="关键词">
          <el-input v-model="searchForm.keyword" placeholder="输入电影名称" style="width: 200px;" />
        </el-form-item>
        <el-form-item label="类型">
          <el-select v-model="searchForm.genre" placeholder="选择电影类型" style="width: 150px;" clearable>
            <el-option v-for="genre in genres" :key="genre" :label="genre" :value="genre" />
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="searchMovies">搜索</el-button>
          <el-button @click="resetSearch">重置</el-button>
        </el-form-item>
      </el-form>

      <!-- 电影列表 -->
      <el-table v-if="movies.length > 0" :data="movies" stripe style="width:100%" :header-cell-style="{ background: '#f5f5f5' }">
        <el-table-column prop="id" label="ID" width="80" align="center" />
        <el-table-column prop="title" label="电影标题" min-width="200" />
        <el-table-column prop="year" label="年份" width="100" align="center" />
        <el-table-column prop="genres" label="类型" min-width="150">
          <template #default="{ row }">
            <el-tag v-for="genre in row.genres.split(',')" :key="genre" size="small" style="margin-right: 5px;">
              {{ genre.trim() }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="avg_rating" label="平均评分" width="120" align="center">
          <template #default="{ row }">
            <el-rate :value="row.avg_rating" disabled show-score text-color="#ff9900" score-template="{value}" />
          </template>
        </el-table-column>
        <el-table-column prop="rating_count" label="评分数" width="120" align="center" />
        <el-table-column label="操作" width="200" align="center">
          <template #default="{ row }">
            <el-button type="primary" size="small" @click="detail(row.id)">详情</el-button>
            <el-button type="warning" size="small" @click="recommend(row.id)">相似推荐</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 空状态 -->
      <el-empty v-else description="暂无电影数据，请调整搜索条件" />

      <!-- 分页 -->
      <el-pagination
        v-if="total > pageSize"
        v-model:current-page="currentPage"
        :page-size="pageSize"
        :total="total"
        layout="prev, pager, next"
        style="margin-top: 20px; text-align: center;"
        @current-change="handlePageChange"
      />
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { getMovies } from '@/api'
import { ElMessage } from 'element-plus'

const movies = ref([])
const router = useRouter()
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(0)
const searchForm = ref({ keyword: '', genre: '' })
const genres = ref(['Action', 'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'])

const fetchMovies = async () => {
  try {
    const params = {
      keyword: searchForm.value.keyword || undefined,
      genre: searchForm.value.genre || undefined,
      page: currentPage.value,
      page_size: pageSize.value
    }
    const res = await getMovies(params)
    if (res.data.code === 200) {
      movies.value = res.data.data.list || []
      total.value = res.data.data.total || 0
    } else {
      ElMessage.error(res.data.message || '获取电影列表失败')
    }
  } catch (e) {
    console.error(e)
    ElMessage.error('获取电影列表失败，请重试')
  }
}

const searchMovies = () => {
  currentPage.value = 1
  fetchMovies()
}

const resetSearch = () => {
  searchForm.value = { keyword: '', genre: '' }
  currentPage.value = 1
  fetchMovies()
}

const handlePageChange = (page) => {
  currentPage.value = page
  fetchMovies()
}

const detail = (id) => router.push(`/movies/${id}`)
const recommend = (id) => router.push(`/recommend/${id}`)

onMounted(fetchMovies)

// 监听搜索表单变化，但不自动搜索，避免频繁请求
</script>