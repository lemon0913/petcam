<template>
    <div>
        <page-title icon="mdi-food-drumstick">급식기</page-title>

        <div class="my-3">
            <div v-for="(devices, place) in sensors" :key="place">
                <page-title class="mt-5" icon="mdi-water-plus">{{place}}</page-title>

                <hr class="mt-1 mb-3">

                <v-row >  
                    <v-col class="pa-3" cols="6" sm="4" 
                        v-for="(value, device) in devices" :key="device">
                        <Watersensor v-if="device==='water'" :value="value"></Watersensor>
                        

                    
                    </v-col>
                </v-row>
            </div>

        </div>
        <hr class="mt-1 mb-3">
        <hr class="mt-1 mb-3">
        <div class="my-3">

        </div>
    </div>
</template>

<script>
import Watersensor from '../components/sensors/Watersensor.vue';
export default {
    components: { Watersensor },
    name: 'Mqtt',

    data() {
        return { 
            sensors: {
                '물 통': {
                    'water': {} 
                }
            },

            servo: {
                '사료': {
                    'food': 1
                }
            }  
        }
    },
    mqtt: {
        'iot/hong/sensors' : function(value, topic) {
            console.log(topic, value)
            this.sensors = {
                '물 통': {
                    'water': value
                }
            }
        }
    },

    mounted() {
        // 구독 신청
        this.$mqtt.subscribe('iot/hong/sensors')
        
    },

    unmounted() {
        // 구독 해제
        this.$mqtt.unsubscribe('iot/hong/sensors')
        
    },

};

</script>

<style lang="scss" scoped>

</style>