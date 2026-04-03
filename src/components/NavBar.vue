<template>
  <header class="home-navbar">
    <div class="home-navbar-left">🎬 电影推荐系统</div>
    <nav class="home-navbar-center">
      <a href="#" :class="{ active: selected === '首页' }" @click.prevent="select('首页')">首页</a>
      <a href="#" :class="{ active: selected === '电影' }" @click.prevent="select('电影')">电影</a>
      <a href="#" :class="{ active: selected === '电视剧' }" @click.prevent="select('电视剧')">电视剧</a>
      <a href="#" :class="{ active: selected === '综艺' }" @click.prevent="select('综艺')">综艺</a>
      <a href="#" :class="{ active: selected === '动漫' }" @click.prevent="select('动漫')">动漫</a>
    </nav>
    <div class="home-navbar-right">游客</div>
  </header>
</template>

<script setup>
import { ref } from 'vue'
const selected = ref('首页')

const select = (name) => {
  selected.value = name
}
</script>

<style scoped>
.home-navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 2rem;
  background: linear-gradient(90deg, #16222a, #3a6073);
  color: #fff;
  position: sticky;
  top: 0;
  z-index: 999;
}
.home-navbar-left {
  font-size: 1.2rem;
  font-weight: bold;
}
.home-navbar-center a {
  margin: 0 12px;
  color: #fff;
  text-decoration: none;
  font-size: 0.95rem;
  transition: color 0.2s ease;
}
.home-navbar-center a:hover {
  color: #ffd04b;
}
.home-navbar-center a.active {
  color: #ffd04b;
  border-bottom: 2px solid #ffd04b;
  padding-bottom: 2px;
}
.home-navbar-right {
  font-size: 0.95rem;
}
</style>
