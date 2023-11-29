<template>
  <div class="container mt-5">
    <h2 class="mb-4">授業情報入力フォーム</h2>
    <form @submit.prevent="submitClassInfo">
      <div class="mb-3">
        <label for="classname" class="form-label">授業名：</label>
        <input v-model="classname" id="classname" type="text" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="professor" class="form-label">教授名：</label>
        <input v-model="professor" id="professor" type="text" class="form-control">
      </div>

      <div class="mb-3">
        <label for="room" class="form-label">教室：</label>
        <input v-model="room" id="room" type="text" class="form-control">
      </div>

      <div class="mb-3">
        <button type="submit" class="btn btn-primary">登録</button>
        <button type="button" @click="deleteClassInfo" class="btn btn-danger mx-3">削除</button>
        <router-link to="/" class="btn btn-secondary">ホーム</router-link>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      date: null,
      period: null,
      classname: '',
      professor: '',
      room: '',
      disabled: true,
    };
  },
  created() {
    this.date = this.$route.query.date;
    this.period = this.$route.query.period;
    this.fetchDataFromBackend();
  },
  watch: {
    date() {
      this.disabled = false;
    },
    period() {
      this.disabled = false;
    },
  },
  methods: {
    ...mapActions(['fetchDataFromBackend', 'changeTable', 'deleteTable','updateCellContents']),

    async submitClassInfo() {
      try {
        const updatedData = {
          date: this.date,
          period: this.period,
          classname: this.classname,
          professor: this.professor,
          room: this.room
        };

        await this.changeTable(updatedData);


        // フォームをクリア
        this.classname = '';
        this.professor = '';
        this.room = '';
        this.disabled = true;

        // データを再取得
        await this.fetchDataFromBackend();
        
        // ホームに戻る
        this.$router.push('/');
      } catch (error) {
        console.error('データの更新に失敗しました:', error);
      }
    },

    async deleteClassInfo() {
      try {
        await this.deleteTable({ date: this.date, period: this.period });

        // データが変更されたので、再度データを取得
        await this.fetchDataFromBackend();

        // ホームに戻る
        this.$router.push('/');
      } catch (error) {
        console.error('データの削除に失敗しました:', error);
      }
    }
  }
}
</script>
