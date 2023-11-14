<template>
    <div>
      <ul>
        <li v-for="info in ClassInfo" :key="info.id">{{ info.classname }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import { mapState } from 'vuex';
  
  export default {
    computed: {
      ...mapState(['ClassInfo'])
    }
  };
  </script>