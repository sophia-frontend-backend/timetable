<template>
    <div v-if="showForm">
      <h2>授業情報編集フォーム</h2>
      <label for="classname">授業名：</label>
      <input v-model="editedClassInfo.classname" id="classname" type="text" required>
      <br>
  
      <label for="professor">教授名：</label>
      <input v-model="editedClassInfo.professor" id="professor" type="text" required>
      <br>
  
      <label for="room">教室：</label>
      <input v-model="editedClassInfo.room" id="room" type="text" required>
      <br>
  
      <button @click="updateClassInfo">更新</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      classInfo: Object, // 親コンポーネントからデータを受け取る
    },
    data() {
      return {
        showForm: false,
        editedClassInfo: {
          classname: '',
          professor: '',
          room: ''
        }
      };
    },
    methods: {
      updateClassInfo() {
        // フォームのバリデーション
        if (!this.editedClassInfo.classname || !this.editedClassInfo.professor || !this.editedClassInfo.room) {
          console.error('全ての項目を入力してください。');
          return;
        }
  
        // 親コンポーネントに更新が成功したことと更新データを通知
        this.$emit('update-class-info', this.editedClassInfo);
  
        // フォームを非表示にする
        this.showForm = false;
  
        // フォームをクリア
        this.editedClassInfo = {
          classname: '',
          professor: '',
          room: ''
        };
      }
    }
  };
  </script>
  