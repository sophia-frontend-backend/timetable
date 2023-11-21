<!-- DeleteButton.vue -->

<template>
    <button @click="deleteItem">削除</button>
  </template>
  
  <script>
  export default {
    methods: {
      deleteItem() {
        // 削除ボタンがクリックされたことを通知
        this.$emit('delete');
      }
    }
  };
  </script>
  