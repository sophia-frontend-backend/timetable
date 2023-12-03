<template>
  <header class="page-header">
    <nav>
      <ul class="main-nav">
      </ul>
    </nav>
    <h1><span>時間割</span></h1>
  </header>

  <router-view></router-view>

</template>

<script>
import { mapActions } from 'vuex';

export default {
  created() {
    // アプリケーション起動時にデータを取得
    this.fetchDataFromBackend();
    console.log('fetchDataFromBackend called');
  },
  methods: {
    ...mapActions(['fetchDataFromBackend'])
  }
};
</script>
<style scoped>
h1{
  text-align: center;
}
</style>