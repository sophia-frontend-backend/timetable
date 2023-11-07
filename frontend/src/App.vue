<template>
  <header class="page-header">
    <nav>
      <ul class="main-nav">
        <li class="item">
          <router-link to="/">
            ホーム
          </router-link>
        </li>
        <li class="item">
          <router-link to="/register">
            時間割登録
          </router-link>
        </li>
      </ul>
    </nav>
  </header>
  <img alt="Vue logo" src="./assets/logo.png" />

  <router-view></router-view>

</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>
