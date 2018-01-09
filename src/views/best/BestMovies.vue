<template>
  <div class="best-main">
    <h2>电影排行</h2>
    <ol>
      <li v-for="(movie, index) in movies" :key="index">
        <div class="item">
          <div class="pic">
            <em>{{ movie.order }}</em>
            <img :src="movie.img_src" :alt="movie.title"/>
          </div>
          <div class="info">
            <div>
              <span>{{ movie.title }}</span><br>
            </div>
            <div>
              <span>{{ movie.info }}</span><br>
            </div>
            <div>
              <span>{{ movie.movie_type }}</span><br>
            </div>
            <div>
              <span>{{ movie.star }}分</span>
              <span>{{ movie.votes }}</span><br>
            </div>
            <div>
              <q> {{ movie.quote }} </q>
            </div>
          </div>
          <div class="place">
            <div class="operations">
              <span>喜欢😍</span>
              <span>不爱😷</span>
            </div>
          </div>
        </div>
      </li>
    </ol>
    <Pagination :getData="getData"/>
  </div>
</template>

<script>
import Pagination from '@/components/pagination'

import Vue from 'vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)

export default {
  name: 'Best',
  components: {
    Pagination
  },
  data () {
    return {
      movies: [],
      pageCount: 0
    }
  },
  created () {
    this.$http.post('/api/movie/getMovie', { count: 0 }, {}).then((response) => {
      this.movies = response.body
    })
    this.$http.get('/api/movie/totalCount').then((response) => {
      this.pageCount = Math.round((response.body) / 10)
    })
  },
  methods: {
    getData (index) {
      this.$http.post('/api/movie/getMovie', { count: index * 10 }, {}).then((response) => {
        this.movies = response.body
      })
    }
  }
}
</script>

<style lang="less" scoped>
.best-main {
  display: flex;
  flex-direction: column;
  align-items: center;
  ol {
    border-top: 1px dashed #ccc;
    list-style: none;
    li {
      padding: 12px 0;
      border-bottom: 1px dashed #ccc;
      .pic {
        margin-right: 40px;
        em {
          float: left;
          padding: 0 20px 0 10px;
        }
        img {
          width: 100px;
        }
      }
      .item {
        display: flex;
        .info {
          div {
            padding: 4px 0;
          }
        }
        .place {
          width: 200px;
        }
        .operations {
          display: none;
          margin-left: 20px;
          padding: 60px 20px;
          span {
            padding: 0 10px;
            cursor: pointer;
          }
        }
        &:hover {
          .operations {
            display: block;
          }
        }
      }
    }
  }
}
</style>
