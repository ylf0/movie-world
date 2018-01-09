<template>
  <div class="nav-main">
    <span class="brand">电影推荐</span>
    <input class="search" placeholder="🔍  搜索电影"/>
    <ul>
      <li v-for="item in links" :key="item.name"><a :href="item.href"> {{ item.name }} </a></li>
    </ul>
  </div>  
</template>

<script>
export default {
  name: 'Nav',
  data () {
    return {
      links: [
        { name: 'fun function😆', href: '/' },
        { name: '电影排行🎥', href: '#/best-movie' },
        { name: '电影专辑🎬', href: '/' },
        { name: '个人主页👤', href: '/' }
      ]
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
      a {
        text-decoration: none;
        color: white;
      }
    }
  }
}
</style>
