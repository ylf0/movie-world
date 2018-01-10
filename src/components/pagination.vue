<template>
  <div class="pagination-main">
    <div class="pag-button" v-for="(item, index) in paginations" :key="item">
      <button @click="getData(index)" ref="pagination">{{ index + 1 }}</button>
    </div>
    <div class="pag-button">
      <button v-if="next" @click="more">more</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Pagination',
  data () {
    return {
      paginations: [],
      next: false,
      test: ''
    }
  },
  props: {
    pageCount: {
      type: Number,
      default: 0
    },
    currentPage: {
      type: Number,
      default: 0
    },
    getData: {
      type: Function
    }
  },
  created () {
    if (this.pageCount > 10) {
      this.paginations.length = 10
      this.next = true
    } else {
      this.paginations.length = this.pageCount
    }
  },
  methods: {
    more () {
      this.next = false
      this.paginations.length = this.pageCount
    }
  },
  watch: {
    pageCount () {
      if (this.pageCount > 10) {
        this.paginations.length = 10
        this.next = true
      } else {
        this.paginations.length = this.pageCount
      }
    },
    currentPage (val) {
      this.$refs.pagination.forEach((item) => {
        item.setAttribute('style', 'background-color: none;')
      })
      this.$refs.pagination[val].setAttribute('style', 'background-color: rgb(14, 137, 237);')
    }
  }
}
</script>

<style lang="less" scoped>
.pagination-main {
  display: flex;
  // width: 70%;
  // justify-content: flex-end;
  .pag-button {
    padding: 10px 6px 40px 6px;
    button {
      cursor: pointer;
    }
  }
  button {
    width: 41px;
    height: 22px;
    border: none;
    border-radius: 3px;
    color: white;
    background-color: rgb(188, 194, 201);
    outline: none;
  }
}
</style>
