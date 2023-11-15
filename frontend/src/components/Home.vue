<template>
  <div>
    <ul>
      <li v-for="info in ClassInfo" :key="info.id">{{ info.className }} - {{ info.professor }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  computed: {
    ...mapState(['ClassInfo'])
  },
  created() {
    this.fetchDataFromBackend(); // データをバックエンドから取得
  },
  methods: {
    ...mapActions(['fetchDataFromBackend'])
  }
};
</script>
