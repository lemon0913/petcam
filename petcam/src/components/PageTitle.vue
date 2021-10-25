<template>
    <div>
        <h2 class="orange--text darken-4">
            <v-icon size="1.5em" color="orange darken-2">{{icon}}</v-icon>
            <slot></slot>
        </h2>
    </div>
</template>

<script>
export default {
    name: 'Pagetitle',
    props: ['icon'],

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