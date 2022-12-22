import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  // Product account information for head role
  {
    path: '/painfoh',
    name: 'PAInfoH',
    component: () => import('../views/PAInfoH.vue')
  },
  // Product account information for sale role
  {
    path: '/painfos',
    name: 'PAInfoS',
    component: () => import('../views/PAInfoS.vue')
  },
]

const router = new VueRouter({
  routes,
  mode: "history"
})

export default router
