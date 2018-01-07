<template>
  <div class="nav-main">
    <span class="brand">电影世界</span>
    <input class="search" placeholder="🔍  搜索电影"/>
    <ul>
      <li v-for="item in links" :key="item">{{ item }}</li>
    </ul>
  </div>  
</template>

<script>
export default {
  name: 'Nav',
  data () {
    return {
      links: ['fun function😆', '电影排行🎥', '电影专辑🎬', '个人主页👤']
    }
  }
}
</script>

<style lang="less" scoped>
.nav-main {
  display: flex;
  margin: 20px 0px;
  width: 100%;
  color: white;
  letter-spacing: 1.2px;
  justify-content: space-between;
  .brand {
    margin-left: 100px;
    font-size: 22px;
  }
  input {
    width: 220px;
    height: 30px;
    padding: 0px 20px;
    font-size: 16px;
    background-color: #D8D8D8;
    outline: none;
    border-radius: 8px;
    border: 1px solid gray;
  }
  ul {
    margin: 0 40px 0 0;
    li {
      float: left;
      margin-right: 60px;
      list-style: none;
      cursor: pointer;
    }
  }
}
</style>
