import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import './plugins/components'
import VueMqtt from 'vue-mqtt';

Vue.use(VueMqtt, 'ws://192.168.219.150:9001/ws', 
    {clientID:  "clientID-" + parseInt(Math.random() * 1000) });



Vue.use(require('vue-moment'))

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
