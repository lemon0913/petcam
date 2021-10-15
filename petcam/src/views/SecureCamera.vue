<template>
    <div class="mb-10">
        <page-title icon="mdi-video">실시간 카메라</page-title>

        
        <remote-camera url="http://192.168.0.9:8000/mjpeg/stream/" max-width="640"></remote-camera>
        <!-- <remote-camera url="https://picsum.photos/seed/picsum/640/480" max-width="640"></remote-camera> -->
        
    </div>
</template>

<script>
export default {
    name: 'Securecamera',

    data() {
        return {
            
        };
    },

    mounted() {
        
    },

    methods: {
        
    },
};
</script>

<style lang="scss" scoped>

</style>