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

  <router-view></router-view>

</template>

<script>
import { mapActions } from 'vuex';

export default {
  created() {
    // アプリケーション起動時にデータを取得
    this.fetchClassInfo();
    console.log('fetchClassInfo called');
  },
  methods: {
    ...mapActions(['fetchClassInfo'])
  }
};
</script>