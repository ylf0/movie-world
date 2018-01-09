import Vue from 'vue'
import Router from 'vue-router'
import Daily from '@/views/daily/Daily'
import Best from '@/views/best/BestMovies'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Daily',
      component: Daily
    },
    {
      path: '/best-movie',
      name: 'Best',
      component: Best
    }
  ]
})
