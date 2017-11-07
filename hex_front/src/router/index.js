import Vue from 'vue'
import Router from 'vue-router'
import result from '@/components/result'
import login from '@/components/login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/result',
      name: 'result',
      component: result
    }
  ]
})
