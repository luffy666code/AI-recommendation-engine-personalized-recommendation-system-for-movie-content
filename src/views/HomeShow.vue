<template>
  <div class="home-show">
    <Navbar />
    <Banner />

    <div class="content-wrapper">
      <MovieSection title="热门电影" :movies="mockData.hotMovies" />
      <MovieSection title="热门电视剧" :movies="mockData.hotTV" />
      <MovieSection title="热门综艺" :movies="mockData.hotVariety" />
      <MovieSection title="动漫推荐" :movies="mockData.anime" />
    </div>

    <Footer />
  </div>
</template>

<script setup>
import Navbar from '@/components/Navbar.vue'
import Banner from '@/components/Banner.vue'
import MovieSection from '@/components/MovieSection.vue'
import Footer from '@/components/Footer.vue'
import { mockMovies } from '@/mock/movies.js'

const mockData = mockMovies
</script>

<style scoped>
.home-show {
  background-color: #f2f5f9;
  min-height: 100vh;
}
.content-wrapper {
  max-width: 1200px;
  margin: 20px auto;
  padding: 0 15px;
}

@media (max-width: 900px) {
  .home-navbar {
    flex-wrap: wrap;
    padding: 10px 12px;
  }
  .home-navbar-center {
    margin-top: 8px;
    width: 100%;
    justify-content: center;
  }
  .home-navbar-right {
    margin-top: 8px;
    width: 100%;
    text-align: right;
  }
  .movie-list {
    overflow-x: scroll;
  }
}
</style>