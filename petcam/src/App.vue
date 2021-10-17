<template>
  <v-app>
    <!-- 툴바 꾸미기 -->
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="drawer=!drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>PetCam </v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- 우측 아이콘 -->
      <v-btn icon @click="$router.push({name:'Home'})">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-btn icon v-if='isLogin' @click="logout">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
      <v-btn icon v-else: to="{name:'Login'}">
        <v-icon>mdi-login</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <!-- 내비게이션 -->
    <v-navigation-drawer absolute v-model="drawer" temporary>
      <v-list dense nav>
        <v-list-item v-for="page in pages" :key="page.name" :to="{name:page.name}" exact>
          <v-list-item-icon>
            <v-icon>{{page.icon}}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{page.title}}</v-list-item-title>
          </v-list-item-content>

        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    
    <!-- 내용 영역 -->
    <v-main>
      <v-slide-x-transition mode="out-in">
        <router-view></router-view>
      </v-slide-x-transition>
    </v-main>

    <!-- 푸터 꾸미기 -->
    <v-footer color="secondary" fixed dark>
      <div class="mx-auto">created by 3조</div>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    drawer:false,
    pages: [
      {title: 'Home', name:'Home', icon:'mdi-home'},
      {title: 'Mqtt 모니터링', name:'Mqtt', icon:'mdi-access-point-network'},
      {title: '보안카메라', name:'SecureCamera', icon:'mdi-video'},
    ]
    
  }),
};
</script>
