import Vue from "vue"
import PageTitle from '../components/PageTitle.vue'
import VueKnob from '@websanova/vue-knob'
import RemoteCamera from "../components/device/RemoteCamera.vue"
import VideoList from '@/components/VideoList.vue'
import Watersensor from '@/components/sensors/Watersensor.vue'




//전역 컴포넌트 등록
Vue.component('PageTitle', PageTitle)
Vue.component('knob', VueKnob)
Vue.component('RemoteCamera', RemoteCamera)
Vue.component('video-list', VideoList)
Vue.component('Watersonsor', Watersensor)

