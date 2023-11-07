<template>
    <div>
      <h2>授業情報入力フォーム</h2>
      <form @submit.prevent="submitClassInfo">
        <label for="date">曜日：</label>
        <select v-model="date" id="date">
          <option value="月曜日">月曜日</option>
          <option value="火曜日">火曜日</option>
          <option value="水曜日">水曜日</option>
          <option value="木曜日">木曜日</option>
          <option value="金曜日">金曜日</option>
        </select>
        <br>

        <label for="time">時限：</label>
        <select v-model="period" id="period">
          <option value="1限">1限</option>
          <option value="2限">2限</option>
          <option value="3限">3限</option>
          <option value="4限">4限</option>
          <option value="5限">5限</option>
          <option value="6限">6限</option>
        </select>
        <br>
  
        <label for="className">授業名：</label>
        <input v-model="className" id="className" type="text">
        <br>
  
        <label for="professor">教授名：</label>
        <input v-model="professor" id="professor" type="text">
        <br>
  
        <label for="room">教室：</label>
        <input v-model="room" id="room" type="text">
        <br>
  
        <button type="submit">登録</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        day: '月曜日',
        time: '',
        className: '',
        professor: '',
        room: ''
      };
    },
    methods: {
      async submitClassInfo() {
        const classInfo = {
          day: this.day,
          time: this.time,
          className: this.className,
          professor: this.professor,
          room: this.room
        };
  
        try {
          const response = await axios.post('/api/class-info', classInfo);
          console.log('データが送信されました:', response.data);
          // 成功メッセージなどの処理を追加
        } catch (error) {
          console.error('データ送信中にエラーが発生しました:', error);
          // エラーメッセージなどの処理を追加
        }
      }
    }
  };
  </script>