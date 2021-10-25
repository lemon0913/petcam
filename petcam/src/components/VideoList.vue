<template>
  <div>
    <v-btn class="float-right" color="primary" icon @click="load"><v-icon>mdi-refresh</v-icon></v-btn>
    <ul class="mt-3">
      <li v-for="(file, ix) in fileList" :key="ix" @click="video=file" 
        :class="{active: video ===file}">
        {{file.filename}}
      </li>
    </ul>
    <video v-if="video.video_file" :src="video.video_file" class="video" controls autoplay></video>
  </div>
</template>
<script>
  import axios from '@/util/api'

  export default {
    name: 'VideoList',
    data() {
      return {
        video: {},
        fileList: [
          // { name: 'video1.mp4', url: 'https://picsum.photos/640/480?random=5'},
          // { name: 'video2.mp4', url: 'https://picsum.photos/640/480?random=6'},
          // { name: 'video3.mp4', url: 'https://picsum.photos/640/480?random=7'},
          // { name: 'video4.mp4', url: 'https://picsum.photos/640/480?random=8'},
        ]
      }
    },
    methods: {
      async load() {

        try {
          let {data} = await axios.get('/api/video')
          console.log(data)
          this.fileList = data.results
        } catch (e) {
          console.log('에러 : ', e)
        }
      }
      // 서버로 부터 목록 얻어야 함.

    },
    async mounted() {
      this.load()
    }
  }
</script>

<style scoped>
.active{
  color: red;
  font-weight: bolder;
}
</style>
