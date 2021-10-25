import axios from 'axios';
import store from '@/store/index.js';

let instance = axios.create({})  //axios 인스턴스 생성

function setInterceptors(instance) {
    instance.interceptors.request.use( // login API 요청후
        function(config) {
            // 요청 시 마다 자동으로 헤더 세팅
            // Authorization: jwt <실제 JWT 값>
            console.log('intercepter', store.state.user)
            if(store.state.user) {
                config.headers.Authorization = `jwt ${store.state.user.jwt}`;
            }
            return config;
        },
        function(error) {
            return Promise.reject(error);
        },
    );
    // Add a response interceptor
    instance.interceptors.response.use(
        function(response) {
            return response;
        },
        function(error) {
            return Promise.reject(error);
        },
    );
    return instance; 
}

setInterceptors(instance)

export default instance