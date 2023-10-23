import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import List from '../components/List.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      //component: () => import('../views/AboutView.vue')
    },
    {
      path: '/list',
      name: 'list',
      component: List,
    },
    {
      path: '/folio/:id',
      name: 'folio',
      component: 'GetFolioById' 
    }
  ]
})

export default router
