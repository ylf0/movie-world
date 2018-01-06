<template>
  <div class="daily-main">
    <div class="bg-image">
      <img src="static/bg.jpg"/>
    </div>
    <Nav class="navbar"/>
  </div>
</template>

<script>
import Nav from '@/components/nav'

export default {
  name: 'Daily',
  components: {
    Nav
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
}
</style>
