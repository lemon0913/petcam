<template>
    <div>
        <v-icon x-large class="mr-3 float-left" 
             :color="color">{{icon}}</v-icon>
        <div  class="font-weight-bold">남은 물</div>
        <span>{{value}}cm</span>
    </div>
</template>

<script>
export default {
    name: 'Watersensor',
    props: ['value'],
    data() {
        return {
            icons: [
                'mdi-water', 
                'mdi-water-off', 
            ],
            colors: [ 'blue', 'red' ],
        }
    },

    computed: {
        color() {
            return this.colors[this.index]
        },
        icon() {
            return this.icons[this.index]
        },
        index() {
            if (this.value >= 2 ) return 0
            else return 1
        },
    }
}
</script>
