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

        <label for="period">時限：</label>
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
  
        <button type="register">登録</button>
      </form>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      date: 'null',
      period: 'null',
      className: '',
      professor: '',
      room: ''
    };
  },
  methods: {
    submitClassInfo() {
      const classInfo = {
        date: this.date,
        period: this.period,
        className: this.className,
        professor: this.professor,
        room: this.room
      };

      axios.post('http://127.0.0.1:5000', classInfo)
        .then(response => {
          console.log('時間割が登録できました:', response.data);
          // postが成功した場合の処理
        })
        .catch(error => {
          console.error('時間割が登録できませんでした:', error);
          // postが失敗した場合の処理
        });
    }
  }
};
</script>