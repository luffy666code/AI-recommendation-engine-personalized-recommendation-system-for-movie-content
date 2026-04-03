<template>
  <section class="movie-section">
    <div class="section-header">
      <h3>{{ title }}</h3>
      <span>更多 ></span>
    </div>
    <div class="movie-list" ref="listContainer">
      <MovieCard v-for="item in movies" :key="item.id" :movie="item" />
    </div>
  </section>
</template>

<script setup>
import { defineProps, ref } from 'vue'
import MovieCard from './MovieCard.vue'

const props = defineProps({
  title: { type: String, required: true },
  movies: { type: Array, required: true }
})

const listContainer = ref(null)
</script>

<style scoped>
.movie-section {
  margin: 20px 0;
}
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.section-header h3 {
  margin: 0;
  font-size: 1.25rem;
}
.section-header span {
  color: #409eff;
  font-size: 0.85rem;
}
.movie-list {
  display: flex;
  overflow-x: auto;
  padding-bottom: 10px;
  gap: 10px;
}
.movie-list::-webkit-scrollbar {
  height: 8px;
}
.movie-list::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 5px;
}
</style>