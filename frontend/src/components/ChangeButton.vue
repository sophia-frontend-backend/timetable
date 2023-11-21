<template>
  <button @click="showEditForm">変更</button>
</template>

<script>
export default {
  methods: {
    showEditForm() {
      // 親コンポーネントに変更ボタンがクリックされたことを通知
      this.$emit('show-edit-form');
    }
  }
};
</script>