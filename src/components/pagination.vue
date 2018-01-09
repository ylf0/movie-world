<template>
  <div class="pagination-main">
    <div class="pag-button" v-for="(item, index) in paginations" :key="item">
      <button @click="getData(index)">{{ index + 1 }}</button>
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
      next: false
    }
  },
  props: {
    pageCount: {
      type: Number,
      default: 0
    },
    getData: {
      type: Function
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
    background-color: rgb(14, 137, 237);
    outline: none;
  }
}
</style>
