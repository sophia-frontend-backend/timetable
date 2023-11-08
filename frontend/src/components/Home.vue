<template>
    <div>
      <ul>
        <li v-for="info in classInfo" :key="info.id">{{ info.className }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import { mapState } from 'vuex';
  
  export default {
    computed: {
      ...mapState(['classInfo'])
    }
  };
  </script>