<template>
  <el-container style="min-height: 100vh; background-color: #f5f5f5;">
    <el-header style="background-color: #001529; padding: 0;">
      <NavBar />
    </el-header>
    <el-main style="padding: 20px;">
      <el-row justify="center">
        <el-col :span="24" :lg="20" :xl="18">
          <router-view />
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script setup>
import NavBar from './components/NavBar.vue'
</script>

<style>
body {
  margin: 0;
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}
</style>
