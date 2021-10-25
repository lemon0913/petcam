<template>
  <div>
    <page-title icon="mdi-video">보안 카메라</page-title>

    <v-tabs class="mt-3" v-model="tab">
      <v-tab >
        <page-title icon="mdi-camera-wireless" class="my-3">실시간</page-title>
      </v-tab>
      <!-- <v-tab >
        <page-title icon="mdi-camera" class="my-3">스냅샷</page-title>
      </v-tab> -->
      <v-tab>
        <page-title icon="mdi-file-video" class="my-3">녹화영상</page-title>
      </v-tab>
    </v-tabs>
   
    <remote-camera  v-if="tab==0" url="http://192.168.0.9:8000/mjpeg/stream/" max-width="640"></remote-camera>
    <!-- <snapshot-list v-if="tab==1"></snapshot-list> -->
    <video-list v-if="tab==1"></video-list>

  </div>
</template>

<script>
export default {
  name: 'SecureCamera',
  data() {
    return {
      tab: 0,

    };
  },
};
</script>

<style scoped>
</style>
