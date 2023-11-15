<template>
    <div>
      <h2>授業情報修正フォーム</h2>
      <label for="date">曜日：</label>
      <select v-model="classInfo.date" id="date">
        <option value="月曜日">月曜日</option>
        <option value="火曜日">火曜日</option>
        <option value="水曜日">水曜日</option>
        <option value="木曜日">木曜日</option>
        <option value="金曜日">金曜日</option>
      </select>
      <br>
  
      <label for="period">時限：</label>
      <select v-model="classInfo.period" id="period">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
      </select>
      <br>
  
      <label for="classname">授業名：</label>
      <input v-model="classInfo.classname" id="classname" type="text" required>
      <br>
  
      <label for="professor">教授名：</label>
      <input v-model="classInfo.professor" id="professor" type="text" required>
      <br>
  
      <label for="room">教室：</label>
      <input v-model="classInfo.room" id="room" type="text" required>
      <br>
  
      <button @click="updateClassInfo">更新</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        classInfo: {
          date: null,
          period: null,
          classname: '',
          professor: '',
          room: ''
        }
      };
    },
    methods: {
      async updateClassInfo() {
        // フォームのバリデーション
        if (!this.classInfo.date || !this.classInfo.period || !this.classInfo.classname || !this.classInfo.professor || !this.classInfo.room) {
          console.error('全ての項目を入力してください。');
          return;
        }
  
        // サーバーに送信するデータ
        const updatedInfo = {
          date: this.classInfo.date,
          period: this.classInfo.period,
          classname: this.classInfo.classname,
          professor: this.classInfo.professor,
          room: this.classInfo.room
          // 更新したい他のプロパティもここに含める
        };
  
        try {
          // PUT リクエスト
          const response = await axios.put(`http://127.0.0.1:5000/${this.classInfo.date}/${this.classInfo.period}`, updatedInfo);
  
          console.log('データが更新されました:', response.data);
  
          // 更新が成功した場合、フォームをクリア
          this.clearForm();
        } catch (error) {
          console.error('データの更新に失敗しました:', error);
          // 更新が失敗した場合の処理
        }
      },
      clearForm() {
        // フォームをクリア
        this.classInfo = {
          date: null,
          period: null,
          classname: '',
          professor: '',
          room: ''
        };
      }
    }
  };
  </script>
  