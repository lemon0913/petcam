<template>
    <div>
         <page>
            <page-title icon="mdi-login" class="mx-auto">로그인</page-title>
            <v-form @submit.prevent="login({username, password})">
                <v-row class="login">
                    <v-col cols="8" class="mx-auto">
                        <v-text-field v-model="username" label="username"
                            prepend-icon="mdi-account" required></v-text-field>
                    </v-col>
                
                    <v-col cols="8" class="mx-auto">
                        <v-text-field type="password" v-model="password" label="password"
                            prepend-icon="mdi-account-lock" ></v-text-field>
                    </v-col>
                
                    <v-col cols="8" class="mx-auto red--text" v-if="error">
                        <v-icon color="red">mdi-information</v-icon> {{error.message}}
                    </v-col>

                    <v-col cols="8" class="mx-auto">
                        <v-btn type="submit" color="orange darken-2" block :disabled="!isValid">
                            <body-1 class="white--text">
                                <v-icon class="mr-3">mdi-login</v-icon> 로그인
                            </body-1>
                        </v-btn>
                    </v-col>
                    
                    <v-col cols="8" class="mx-auto">
                        <v-btn color="orange darken-2" block>
                            <body-1 class="white--text">
                                <v-icon class="mr-3">mdi-account-plus</v-icon> 회원가입
                            </body-1>
                        </v-btn>
                    </v-col>
                </v-row>
            </v-form>
        </page>
    </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex';
export default {
    name: 'Login',

    data() {
        return {
            // username: undefined,
            // password: undefined
            username: 'hong',
            password: '1234'
        };
    },
    computed: {
        ...mapState(['error']),

        isValid() {
            return !!this.username&& !!this.password
        }
    },

    mounted() {
        this.setError()        
    },

    unmounted() {
        this.setError()
    },

    methods: {
        ...mapMutations(['setError']),
        ...mapActions(['login'])        
    },
};
</script>

<style lang="scss" scoped>

</style>