<template>
  <div class="home-banner">
    <el-carousel height="380px" trigger="click" indicator-position="outside" :interval="3500" arrow="always">
      <el-carousel-item v-for="item in banners" :key="item.id">
        <img :src="item.image" :alt="item.title" loading="lazy" />
        <div class="banner-text">{{ item.title }}</div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const banners = ref([
  { id: 1, title: '推荐：经典电影合集', image: 'https://via.placeholder.com/1200x380?text=推荐1' },
  { id: 2, title: '热播剧目更新', image: 'https://via.placeholder.com/1200x380?text=推荐2' },
  { id: 3, title: '全新综艺上线', image: 'https://via.placeholder.com/1200x380?text=推荐3' },
  { id: 4, title: '动漫精选推荐', image: 'https://via.placeholder.com/1200x380?text=推荐4' }
])
</script>

<style scoped>
.home-banner img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.banner-text {
  position: absolute;
  bottom: 20px;
  left: 50px;
  color: #fff;
  font-size: 1.8rem;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.8);
}
</style>