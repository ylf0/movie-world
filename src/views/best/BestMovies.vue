<template>
  <div class="best-main">
    <h2>电影排行</h2>
    <ol>
      <li v-for="(movie, index) in movies" :key="index" ref="list">
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
              <span @click="like(movie, index)">喜欢😍</span>
              <span @click="dislike(movie, index)">不爱😷</span>
            </div>
          </div>
        </div>
      </li>
    </ol>
    <div class="recommend">
      <button @click="recommend">推荐电影</button>
    </div>
    <Pagination v-if="showPag" :getData="getData" :pageCount="pageCount"/>
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
      showPag: false,
      movies: [],
      allTypeArr: [],
      allMovieOrder: [],
      fitOptions: [],
      enjoy_type: null,
      enjoy_order: null,
      verifySet: null,
      typeArr: [],
      pageCount: 0
    }
  },
  created () {
    this.enjoy_type = new Set()
    this.enjoy_order = new Set()
    this.verifySet = new Set()
    this.$http.post('/api/movie/getMovie', { count: 0 }, {}).then((response) => {
      this.movies = response.body
    })
    this.$http.get('/api/movie/totalCount').then((response) => {
      this.pageCount = Math.round((response.body) / 10)
      if (this.pageCount) this.showPag = true
    })
  },
  methods: {
    getData (index) {
      this.$http.post('/api/movie/getMovie', { count: index * 10 }, {}).then((response) => {
        this.movies = response.body
      })
    },
    like (movie, index) {
      movie.enjoy = !movie.enjoy
      if (movie.enjoy) {
        this.$refs.list[index].setAttribute('style', 'background-color: rgb(255, 0, 121); color: white')
        this.enjoy_type.add(movie.movie_type)
        this.enjoy_order.add(movie.order)
      } else {
        this.$refs.list[index].setAttribute('style', 'background-color: none')
        this.enjoy_type.delete(movie.movie_type)
        this.enjoy_order.delete(movie.order)
      }
    },
    dislike (movie, index) {
      this.$refs.list[index].setAttribute('style', 'display: none')
      if (movie.enjoy) {
        this.enjoy_type.delete(movie.movie_type)
        this.enjoy_order.delete(movie.order)
      }
    },
    recommend () {
      [...this.enjoy_type].forEach((item) => {
        const index = item.lastIndexOf('/')
        item.slice(index + 2).split(' ').forEach((type) => {
          this.allTypeArr.push(type)
        })
      })
      this.typeArr = [...new Set(this.allTypeArr)]
      this.movies = []
      this.showPag = false
      this.typeArr.forEach((item, index) => {
        this.$http.post('/api/movie/recommend', { type: item }, {}).then((response) => {
          response.body.forEach((item) => {
            this.allMovieOrder.push(item.order)
          })
          if (index === this.typeArr.length - 1) {
            this.allMovieOrder.forEach((order) => {
              if (this.verifySet.has(order) && !this.enjoy_order.has(order)) {
                this.$http.post('/api/movie/byOrder', { order: order }, {}).then((response) => {
                  this.movies.push(response.body[0])
                })
              } else {
                this.verifySet.add(order)
              }
            })
          }
        })
      })
      this.allTypeArr = []
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
  .recommend {
    position: fixed;
    align-self: flex-end;
    top: 200px;
    right: 30px;
    button {
      width: 90px;
      height: 30px;
      border: none;
      border-radius: 6px;
      font-size: 14px;
      letter-spacing: 1.2px;
      color: white;
      background-color: rgb(14, 137, 237);
      outline: none;
      cursor: pointer;
    }
  }
}
</style>
