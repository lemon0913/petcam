import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  //{path: '/', name: 'Home', component: Home},
  // { path: '/login', name: 'Login', 
  //   component: () => import('../views/Login.vue') },
  {path:'/mqtt', name:'Mqtt', 
    component: () => import('../views/Mqtt.vue')},
  {path:'/securecamera', name:'SecureCamera',
    component: () => import('../views/SecureCamera.vue')},
  { path: '/', name: 'Login', 
   component: () => import('../views/Login.vue') },
  { path: '/Home', name: 'Home', component: Home },
  
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
