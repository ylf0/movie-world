<template>
  <div class="daily-main">
    <div class="bg-image">
      <img src="static/bg.jpg"/>
    </div>
    <Nav class="navbar"/>
    <div class="movie-info">
      <span class="title">电影信息</span><br>
      <span class="subtitle">电影简介</span>
      <div class="operation">
        <ul>
          <li v-for="item in operations" :key="item">{{ item }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import Nav from '@/components/nav'

export default {
  name: 'Daily',
  components: {
    Nav
  },
  data () {
    return {
      operations: ['⇤', '🗑', '❤️', '⇥']
    }
  }
}
</script>

<style lang="less" scoped>
.daily-main {
  .bg-image {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    img {
      width: 100%;
      height: 100%;
      background-size: cover;
      background-position: center;
    }
  }
  .navbar {
    position: absolute;
    top: 0px;
  }
  .movie-info {
    position: absolute;
    top: 520px;
    left: 200px;
    border: 1px solid #8C8C8C;
    border-radius: 8px;
    padding: 30px 20px;
    text-align: center;
    // 设置半透明度，同时不影响文字；
    background: rgba(140, 140, 140, 0.6);
    span {
      color: white;
    }
    .title {
      font-size: 22px;
    }
    .subtitle {
      font-size: 20px;
    }
    ul {
      li {
        margin-right: 40px;
        float: left;
        list-style: none;
        cursor: pointer;
      }
    }
  }
}
</style>
