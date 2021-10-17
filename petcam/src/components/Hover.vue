<template>
    <div @mouseenter="runDelay(true)" @mouseleave="runDelay(false)">
        <slot :hover="hover"></slot>
    </div>
</template>

<script>
export default {
    name: 'Hover',

    data() {
        return {
            hover: false,
            openTimeout: null,
            closeTimeout: null,
        };
    },

    mounted() {
        
    },
    created() {
        this.hover = this.value
    },

    methods: {
        runDelay(hover) {
            if (this.disabled) return 

            clearTimeout(this.openTimeout)
            clearTimeout(this.closeTimeout)
            this['${hover ? "open" : "close"}Timeout'] = setTimeout(() => {
                this.hover = hover
            }, parseInt(this['${hover ? "open" : "close"}Delay']))
        },

        // onMouseEnter() {
        //     if (this.disabled) return 
            
        //     clearTimeout(this.openTimeout)
        //     clearTimeout(this.closeTimeout)
        //     this.openTimeout = setTimeout(() => {
        //         this.hover = true
        //     }, parseInt(this.openDelay))
            
        // },
        // onMouseLeave() {
        //     if (this.disabled) return 
            
        //     clearTimeout(this.openTimeout)
        //     clearTimeout(this.closeTimeout)
        //     this.closeTimeout = setTimeout(() => {
        //         this.hover = false
        //     }, parseInt(this.closeDelay))
        // },
    },

    props: {
        closeDelay: {
            type: [Number, String],
            default: 0,
        },
        openDelay: {
            type: [Number, String],
            default: 0,
        },
        disabled: {
            type:Boolean,
            default : false,
        },
        value: {
            type:Boolean,
            default : false,
        },

    },
};
</script>

<style lang="scss" scoped>

</style>