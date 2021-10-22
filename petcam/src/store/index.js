import Vue from 'vue'
import Vuex from 'vuex'
import axios from '@/util/api'
import jwt_decode from "jwt-decode";
import router from '../router';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: undefined,
    error : undefined
  },
  getters: {
    isLogin(state) {
      return !!state.user
    }
  },
  mutations: {
    restore(state, user) {
      state.user = user
    },
    login(state, user) {
      state.user = user
      localStorage.setItem('user', JSON.stringify(user))
      router.push({name: 'Home'})
    },
    logout(state) {
      state.user = {}
      localStorage.setItem('user', '')
      router.go({name: 'Home'}) // 새로 초기화 됨
    },
    setError(state, e) {
      state.error = e
    }
  },
  actions: {
    async login(context, userInfo) {
      context.commit('setError')
      console.log('login', userInfo)
      try {
        let {data} = await axios.post('/api/login', userInfo)
        console.log(data)
        let token = data.token
        let user = jwt_decode(token);
        user.jwt = token;
        console.log(user)
      
        let now = parseInt(Date.now()/1000)
        let remain = (user.exp - now) / 3600 // 남은 만기 시간
        console.log(now, user.exp, remain)
        context.commit('login', user)
      } catch(e) {
        console.log('로그인 실패')
        context.commit('setError',
        {message: '사용자 ID 또는 비밀번호가 맞지 않습니다.'})
      }
  },
  async verify(context, token) {
    let {data} = await axios.post('/api/login/verify', {token})
    return data.token 
  }
},
  modules: {
  }
})
