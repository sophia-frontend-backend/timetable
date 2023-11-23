<template>
  <div>
    <h2>授業情報入力フォーム</h2>
    <form @submit.prevent="submitClassInfo">
      <p>曜日：{{ date }}</p>
      <br>

      <p>時限：{{ period }}</p>
      <br>
  
      <label for="classname">授業名：</label>
      <input v-model="classname" id="classname" type="text" required>
      <br>

      <label for="professor">教授名：</label>
      <input v-model="professor" id="professor" type="text" required>
      <br>

      <label for="room">教室：</label>
      <input v-model="room" id="room" type="text" required>
      <br>

      <button type="submit">登録</button>
      <button type="button" @click="deleteClassInfo">削除</button>
      <router-link to="/"><button>ホーム</button></router-link>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      date: null,
      period: null,
      classname: '',
      professor: '',
      room: '',
      disabled: true, // dateとperiodの選択を無効にする
    };
  },
  created() {
    // URL パラメータから date と period を取得
    this.date = this.$route.query.date;
    this.period = this.$route.query.period;
    this.fetchDataFromBackend(); // 既存データを取得
  },
  watch: {
    // dateとperiodが変更されたらdisabledを解除
    date() {
      this.disabled = false;
    },
    period() {
      this.disabled = false;
    },
  },
  methods: {
    async fetchDataFromBackend() {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/timetable/${this.date}/${this.period}`);
        const existingData = response.data;
        

        // 既存データがある場合はフォームにセット
        if (existingData) {
          this.classname = existingData.classname;
          this.professor = existingData.professor;
          this.room = existingData.room;
        }
      } catch (error) {
        console.error('データの取得に失敗しました:', error);
      }
    },
    submitClassInfo() {
      // フォームのバリデーションは省略

      const ClassInfo = {
        date: this.date,
        period: this.period,
        classname: this.classname,
        professor: this.professor,
        room: this.room
      };

    axios.put(`http://127.0.0.1:5000/timetable/${this.date}/${this.period}`, ClassInfo)
      .then(async response => {
        console.log('PUTされたデータ:', ClassInfo);
        console.log('時間割が更新できました:', response.data);

        // フォームをクリア
        this.classname = '';
        this.professor = '';
        this.room = '';
        this.disabled = true; // dateとperiodの選択を再び無効にする

        // データを再取得
        await this.fetchDataFromBackend();

        // コンソールにデータを表示
        console.log('更新後のデータ:', this.ClassInfo);

        // ホームに戻る
        this.$router.push('/');
      })
      .catch(error => {
        console.error('時間割が更新できませんでした:', error);
        // putが失敗した場合の処理
      });
    },
    deleteClassInfo() {
      // フォームのバリデーションは省略

      axios.put(`http://127.0.0.1:5000/timetable/${this.date}/${this.period}`, {
        classname: '',
        professor: '',
        room: ''
      })
        .then(response => {
          console.log('時間割が削除されました:', response.data);

          // 削除後の処理を追加（例えば、画面をリロードするなど）

          // データを再取得
          this.fetchDataFromBackend();

          this.$router.push('/');
        })
        .catch(error => {
          console.error('時間割が削除できませんでした:', error);
          // putが失敗した場合の処理
        });
    }
  }
};
</script>
