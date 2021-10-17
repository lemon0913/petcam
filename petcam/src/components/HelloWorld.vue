<template>
  <div>
    <v-container class="grey lighten-5">
      <v-row>
        <v-col :sm="6" v-for="page in pages" :key="page.name" :to="{name:page.name}" exact>        
          <v-hover>
            <v-card
              slot-scope="{ hover }"
              :class="`elevation-${hover ? 12 : 2}`"
              width="150"
              height="150"
              @click="$router.push(page.name)"        
            >
              <v-card-title>
                <v-icon size="4em" color="indigo darken-2">{{page.icon}}</v-icon>
              </v-card-title>

              <v-card-text>
                <div class="font-weight-bold">
                    {{page.title}}
                </div>
              </v-card-text>
            </v-card>
          </v-hover>
        </v-col> 
      </v-row>
    </v-container> 
  
        
  
  </div>  
</template>

<script>
  export default {
    
    name: 'HelloWorld',
    data: () => ({
        pages: [
          
          {title: 'Mqtt 모니터링', name:'Mqtt', icon:'mdi-access-point-network'},
          {title: '보안카메라', name:'SecureCamera', icon:'mdi-video'},
        ]
        
      }),

    methods: {
      
    }
  };

</script>

<style scoped>
</style>
