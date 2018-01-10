<template>
  <div class="nav-main">
    <span class="brand">电影推荐</span>
    <div class="search">
      <input class="search" placeholder="🔍  搜索电影" v-model="searchWord" @change="search(searchWord)"/>
      <ul v-if="matchMovies.length">
        <li v-for="name in matchMovies" :key="name">{{ name }}</li>
      </ul>
    </div>
    <ul class="functions">
      <li v-for="item in links" :key="item.name"><a :href="item.href"> {{ item.name }} </a></li>
    </ul>
  </div>  
</template>

<script>
export default {
  name: 'Nav',
  props: {
    search: { type: Function },
    matchMovies: {
      type: Array,
      default: () => []
    }
  },
  data () {
    return {
      searchWord: '',
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
  .functions {
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
  .search {
    display: flex;
    flex-direction: column;
    ul {
      position: relative;
      top: -6px;
      padding: 10px;
      border-radius: 6px;
      background-color: white;
      li {
        padding: 4px;
        padding-right: 0;
        color: gray;
        cursor: pointer;
        list-style: none;
        &:hover {
          color: rgb(71, 171, 245);
          background-color: rgb(245, 245, 245);
        }
      }
    }
  }
}
</style>
