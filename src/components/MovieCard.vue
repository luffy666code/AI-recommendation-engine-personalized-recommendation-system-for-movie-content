<template>
  <div class="movie-card">
    <img :src="movie.cover" :alt="movie.title" loading="lazy" />
    <div class="movie-info">
      <h4>{{ movie.title }}</h4>
      <p>{{ movie.type }} · {{ movie.year }}</p>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.movie-card {
  width: 180px;
  margin-right: 12px;
  border-radius: 10px;
  overflow: hidden;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  cursor: pointer;
}
.movie-card:hover {
  transform: scale(1.03);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}
.movie-card img {
  width: 100%;
  height: 250px;
  object-fit: cover;
}
.movie-info {
  padding: 10px;
}
.movie-info h4 {
  margin: 0;
  font-size: 1rem;
  line-height: 1.3;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.movie-info p {
  margin: 6px 0 0;
  font-size: 0.85rem;
  color: #888;
}
</style>